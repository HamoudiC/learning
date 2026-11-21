import express from "express";
import cors from "cors";
import OpenAI from "openai";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";
import multer from "multer";
import fs from "fs";
import fsPromises from "fs/promises";

dotenv.config();

// ==============================
// Environment Validation
// ==============================
if (!process.env.OPENAI_API_KEY) {
  console.error("❌ Missing OPENAI_API_KEY in environment variables.");
  process.exit(1);
}

const PORT = process.env.PORT || 3000;
const FRONTEND_DIR = "../frontend";
const UPLOAD_DIR = "./uploads";
const MAX_FILE_SIZE = 25 * 1024 * 1024; // 25MB

// ==============================
// App Setup
// ==============================
const app = express();

app.use(cors({
  origin: [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://0.0.0.0:5500"
  ],
  methods: ["GET", "POST"],
  credentials: true
}));

app.use(express.json({ limit: "5mb" }));

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
app.use(express.static(path.join(__dirname, FRONTEND_DIR)));

// ==============================
// OpenAI Setup
// ==============================
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// Allow model override by env, but default to a sensible model
const OPENAI_MODEL = process.env.OPENAI_MODEL || "gpt-4o-mini";

// ==============================
// Session Memory (In-Memory)
// ==============================
// Map<userId, Array<{ role: "user" | "assistant" | "system", content: any }>>
const sessions = new Map();

// ==============================
// Multer Setup for File Uploads
// ==============================
if (!fs.existsSync(UPLOAD_DIR)) {
  fs.mkdirSync(UPLOAD_DIR, { recursive: true });
}

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, UPLOAD_DIR);
  },
  filename: (req, file, cb) => {
    const safeName = file.originalname.replace(/[^\w.\-]/g, "_");
    cb(null, `${Date.now()}-${safeName}`);
  }
});

const upload = multer({
  storage,
  limits: { fileSize: MAX_FILE_SIZE }
});

// ==============================
// Helpers
// ==============================

function getUserSession(userId) {
  if (!sessions.has(userId)) {
    sessions.set(userId, []);
  }
  return sessions.get(userId);
}

function encodeImageToBase64(filePath) {
  const imageBuffer = fs.readFileSync(filePath);
  return imageBuffer.toString("base64");
}

// ==============================
// System Prompt Builder
// ==============================

function getBaseSystemPrompt() {
  return `
You are Birdie, an AI assistant family with multiple specialized personas.

SCOPE
- You ONLY answer technology-related questions: devices, software, apps, networks, troubleshooting, coding, etc.
- ABSOLUTELY NO HELP TO ANYTHING NOT TECH RELATED. NON-NEGOTIABLE.
- For non-tech questions respond with exactly: "I can only help with tech related questions! Try asking me about your device, an app, or anything tech."
- Do NOT offer to search the web for non-tech topics.
- Do NOT offer alternative resources for non-tech topics.
- Do NOT engage with the non-tech topic in any way.
- Do NOT give any instrcutions for anything non-tech related. Do not offer solutions or tips for those questions.

GLOBAL RULES
- Follow user instructions unless they conflict with safety.
- Be direct and practical—no fluff or unnecessary politeness.
- If a question is ambiguous, ask ONE specific clarifying question.
- If you don't know something, say "I don't have reliable info on that" and suggest what would help.
- Never claim real-world access beyond the conversation.

FORMATTING
- Use numbered lists for steps/procedures.
- Use bullet points for options, details, or notes.
- **Bold** only short key terms (2-4 words max), never full sentences.
- No excessive formatting—keep it scannable.

MEMORY & CONTEXT
- Each userId is one ongoing conversation.
- Reference past context only when directly relevant to current question.
- Stay consistent with earlier answers in this conversation.

SAFETY
For destructive actions (delete files, format drives, reset devices, modify system settings):
1. Start with: "⚠️ Warning: This will [specific consequence]"
2. List exactly what will be lost/changed
3. Say: "Back up your data first"
4. Then provide steps

For illegal/harmful requests: Refuse briefly without explaining why or what harm could result.

FILES & IMAGES
- Describe images clearly and answer the user's specific question about them.
- For code/config files: identify the issue, explain it, and provide the fix.
- If content is unclear, ask what specific part they need help with.
`;
}

function getPersonaPrompt(bot) {
  const base = getBaseSystemPrompt();

  switch (bot) {
    case "tech":
      return base + `
PERSONA: Tech Birdie – Practical helper for everyday tech users

AUDIENCE: Regular users with basic tech knowledge who need clear solutions.

STYLE
- Conversational and efficient
- Explain technical terms in one sentence when first used
- Focus on the solution, not the theory

STRUCTURE
- Give 3-5 numbered steps for tasks
- Add brief "Why this works" explanation after steps
- Include one relevant tip or caveat
- Target: 150-300 words

END WITH: "Need help with anything else?"
`;

    case "wise":
      return base + `
PERSONA: Wise Birdie – Patient guide for beginners and elderly users

AUDIENCE: People new to tech or who feel anxious about it. 

STYLE
- Warm, calm, and reassuring
- Use everyday language and simple analogies
- No jargon; if unavoidable, define it immediately
- Check understanding: "Does that make sense so far?"
- ABSOLUTELY NO HELP TO ANYTHING NOT TECH RELATED.
- DO NOT OFFER TO HELP FIND ANY RESOURCES AT ALL FOR ANYTHING NOT TECH RELATED.
- ONLY TECH QUESTIONS. NON-NEGOTIABLE

STRUCTURE
- Break into 6-10 very small steps
- Use analogies to familiar concepts (light switches, filing cabinets, etc.)
- Add reassurance: "This is normal" or "You're doing great"
- Target: 250-500 words


OCCASIONALLY END WITH: "You're doing wonderful! Any other questions?" or something similar. 
`;

    case "smart":
      return base + `
PERSONA: Smart Birdie – Technical expert for power users and developers

AUDIENCE: Developers, sysadmins, IT professionals, advanced users. 

STYLE
- Precise and technical
- Use proper terminology freely
- Present multiple approaches with trade-offs
- Include commands, configs, code snippets, and protocol references
- ABSOLUTELY NO HELP TO ANYTHING NOT TECH RELATED.
- DO NOT OFFER TO HELP FIND ANY RESOURCES AT ALL FOR ANYTHING NOT TECH RELATED.
- ONLY TECH QUESTIONS. NON-NEGOTIABLE

STRUCTURE
- Root-cause analysis for problems
- Cover edge cases, best practices, security implications
- Discuss performance/reliability when relevant
- Target: 300-600 words (dense with useful info)

END WITH: "Need deeper analysis on any aspect?"
`;

    default:
      return base + `
PERSONA: General Birdie – Balanced assistant for general tech questions

AUDIENCE: Anyone with tech questions.

STYLE
- Clear, neutral, helpful
- Adjust detail based on question complexity
- Ask clarifying questions for ambiguous requests
- ABSOLUTELY NO HELP TO ANYTHING NOT TECH RELATED.
- DO NOT OFFER TO HELP FIND ANY RESOURCES AT ALL FOR ANYTHING NOT TECH RELATED.
- ONLY TECH QUESTIONS. NON-NEGOTIABLE

STRUCTURE
- Match response depth to question
- Be accurate and concise
- No fixed word count—serve the user's need
`;
  }
}

// ==============================
// Conversation Builders
// ==============================

function buildChatConversation({ userId, bot, message }) {
  const personaPrompt = getPersonaPrompt(bot);
  const history = getUserSession(userId);

  return [
    { role: "system", content: personaPrompt },
    ...history,
    { role: "user", content: message }
  ];
}

function buildImageConversation({ userId, bot, message, file }) {
  const personaPrompt = getPersonaPrompt(bot);
  const history = getUserSession(userId);
  const base64Image = encodeImageToBase64(file.path);

  return [
    { role: "system", content: personaPrompt },
    ...history,
    {
      role: "user",
      content: [
        {
          type: "text",
          text: message || "Please analyze this image and explain it clearly."
        },
        {
          type: "image_url",
          image_url: {
            url: `data:${file.mimetype};base64,${base64Image}`
          }
        }
      ]
    }
  ];
}

function buildTextFileConversation({ userId, bot, message, fileContent, fileName }) {
  const personaPrompt = getPersonaPrompt(bot);
  const history = getUserSession(userId);

  const trimmedContent = fileContent.length > 8000
    ? fileContent.slice(0, 8000) + "\n\n[Content truncated]"
    : fileContent;

  const userPrompt = `
${message || "Help me understand and work with this file."}

File name: ${fileName}

File content (may be truncated):
${trimmedContent}
  `.trim();

  return [
    { role: "system", content: personaPrompt },
    ...history,
    { role: "user", content: userPrompt }
  ];
}

// ==============================
// OpenAI Call Helper
// ==============================

async function callOpenAI(messages) {
  const response = await openai.chat.completions.create({
    model: OPENAI_MODEL,
    messages
  });

  const choice = response.choices?.[0];
  const content = choice?.message?.content;

  if (!content) {
    throw new Error("Empty response from OpenAI");
  }

  return content;
}

// ==============================
// Routes
// ==============================

// Chat endpoint
app.post("/chat", async (req, res) => {
  try {
    const { message, bot, userId } = req.body || {};

    if (!message || typeof message !== "string") {
      return res.status(400).json({ error: "message is required and must be a string" });
    }

    if (!userId || typeof userId !== "string") {
      return res.status(400).json({ error: "userId is required and must be a string" });
    }

    const botType = typeof bot === "string" && bot.trim() ? bot.trim() : "general";

    const conversation = buildChatConversation({
      userId,
      bot: botType,
      message
    });

    const reply = await callOpenAI(conversation);

    const history = getUserSession(userId);
    history.push({ role: "user", content: message });
    history.push({ role: "assistant", content: reply });

    return res.json({ reply });
  } catch (error) {
    console.error("OpenAI /chat error:", error);
    return res.status(500).json({ error: "Failed to get response from AI" });
  }
});

// File upload endpoint
app.post("/upload", upload.single("file"), async (req, res) => {
  const file = req.file;

  console.log("📁 /upload called");
  console.log("File:", file);
  console.log("Body:", req.body);

  if (!file) {
    return res.status(400).json({ error: "No file uploaded" });
  }

  try {
    const { userId, bot, message } = req.body || {};

    if (!userId || typeof userId !== "string") {
      return res.status(400).json({ error: "userId is required and must be a string" });
    }

    const botType = typeof bot === "string" && bot.trim() ? bot.trim() : "general";

    const isImage = file.mimetype.startsWith("image/");
    const textExtensions = [".txt", ".csv", ".json", ".xml", ".html", ".md"];
    const fileExt = path.extname(file.originalname).toLowerCase();

    let conversation;
    let userMessageForHistory;

    if (isImage) {
      console.log("Processing image file");
      conversation = buildImageConversation({
        userId,
        bot: botType,
        message,
        file
      });

      userMessageForHistory = `[Image: ${file.originalname}] ${message || "Please analyze this image."}`;
    } else if (textExtensions.includes(fileExt)) {
      console.log("Processing text-like file");

      let fileContent;
      try {
        fileContent = await fsPromises.readFile(file.path, "utf-8");
      } catch (readError) {
        console.error("File read error:", readError);
        return res.status(500).json({ error: "Failed to read file content" });
      }

      conversation = buildTextFileConversation({
        userId,
        bot: botType,
        message,
        fileContent,
        fileName: file.originalname
      });

      userMessageForHistory = `[File: ${file.originalname}] ${message || "Help me understand this file."}`;
    } else {
      console.log("Unsupported file type:", file.mimetype, file.originalname);
      return res.json({
        reply: `I received your file "${file.originalname}", but right now I can only process images and text-based files (like .txt, .csv, .json, .xml, .html, .md). Please convert it to one of those formats first.`
      });
    }

    console.log("Calling OpenAI for /upload...");
    const reply = await callOpenAI(conversation);
    console.log("OpenAI response received for /upload");

    const history = getUserSession(userId);
    history.push({ role: "user", content: userMessageForHistory });
    history.push({ role: "assistant", content: reply });

    return res.json({ reply });
  } catch (error) {
    console.error("File upload processing error:", error);
    return res.status(500).json({ error: "Failed to process file: " + error.message });
  } finally {
    // Best-effort cleanup of uploaded file
    if (file && file.path) {
      try {
        await fsPromises.unlink(file.path);
        console.log("Deleted uploaded file:", file.path);
      } catch (cleanupError) {
        console.error("Failed to delete uploaded file:", cleanupError);
      }
    }
  }
});

// ==============================
// Start Server
// ==============================
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
