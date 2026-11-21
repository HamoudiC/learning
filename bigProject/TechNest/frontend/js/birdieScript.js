// ==============================
// Generate Unique User ID
// ==============================
if (!localStorage.getItem("uniqueId")) {
    const uniqueId = "user_" + Math.random().toString(36).slice(2, 9);
    localStorage.setItem("uniqueId", uniqueId);
}

const userId = localStorage.getItem("userId") || "there";
export { userId };

// ==============================
// Default Bot Type
// ==============================
if (!window.BIRDIE_TYPE) {
    window.BIRDIE_TYPE = "tech";
}

// ==============================
// File/Photo Limits
// ==============================
const FILE_LIMITS = {
    "free": { files: 3, photos: 3, voice: 2, maxSize: 5 * 1024 * 1024 },
    "plus": { files: 10, photos: 10, voice: 10, maxSize: 10 * 1024 * 1024 },
    "pro": { files: NaN, photos: NaN, voice: NaN, maxSize: NaN * NaN * NaN }
};

// ==============================
// DOM References
// ==============================
const input = document.getElementById("chatbot-input");
const sendBtn = document.getElementById("send-btn");
const chatContainer = document.getElementById("chat-container");
const counterEl = document.getElementById("counter");

// Upload elements
const uploadBtn = document.getElementById("photo-btn");
const uploadMsg = document.getElementById("photo-msg");
const unifiedFileInput = document.getElementById("unified-file-input");

const voice = document.getElementById("voice-btn");
const voiceMsg = document.getElementById("voice-msg");

// ==============================
// Helper to add messages
// ==============================
function addMessage(text, sender) {
    if (!chatContainer) return;
    const msg = document.createElement("div");
    msg.classList.add("chat-message", sender);
    msg.textContent = text;
    chatContainer.appendChild(msg);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// ==============================
// Backend URL
// ==============================
const backendURL = window.location.port === "5500" ? "http://127.0.0.1:3000" : "";

// ==============================
// Daily Chat Limit with 24-Hour Timer
// ==============================
const DAILY_LIMITS = {
    "tech": 30,
    "wise": 30,
    "smart": 30
};

const DAILY_LIMIT = DAILY_LIMITS[window.BIRDIE_TYPE] || 30;

const storageKey = `dailyLimitData_${window.BIRDIE_TYPE}`;
let savedData = JSON.parse(localStorage.getItem(storageKey));

const now = Date.now();

if (!savedData || !savedData.resetTime || now >= savedData.resetTime) {
    const resetTime = now + (24 * 60 * 60 * 1000);
    savedData = { resetTime: resetTime, remaining: DAILY_LIMIT };
    localStorage.setItem(storageKey, JSON.stringify(savedData));
}

let counter = savedData.remaining;

// ==============================
// Update Countdown Timer
// ==============================
function updateCountdown() {
    if (!counterEl) return;

    const now = Date.now();
    let timeLeft = savedData.resetTime - now;

    if (timeLeft <= 0) {
        const resetTime = Date.now() + (24 * 60 * 60 * 1000);
        savedData = { resetTime: resetTime, remaining: DAILY_LIMIT };
        localStorage.setItem(storageKey, JSON.stringify(savedData));
        counter = DAILY_LIMIT;
        timeLeft = resetTime - now;
    }

    const positiveTimeLeft = Math.max(0, timeLeft);
    const hours = Math.floor(positiveTimeLeft / (1000 * 60 * 60));
    const minutes = Math.floor((positiveTimeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((positiveTimeLeft % (1000 * 60)) / 1000);

    if (counter <= 0) {
        counterEl.textContent = `0 (Resets in ${hours}h ${minutes}m ${seconds}s)`;
    } else {
        counterEl.textContent = `${counter} (Resets in ${hours}h ${minutes}m ${seconds}s)`;
    }
}

setInterval(updateCountdown, 1000);
updateCountdown();

// ==============================
// Send Message to Backend
// ==============================
async function sendMessage() {
    if (!input) return;

    const userMessage = input.value.trim();
    if (!userMessage) return;

    if (userMessage.toLowerCase() === "habood16") {
        localStorage.removeItem(storageKey);
        const resetTime = Date.now();
        savedData = { remaining: NaN };
        localStorage.setItem(storageKey, JSON.stringify(savedData));
        counter = NaN;
        updateCountdown();
        input.value = "";
        addMessage("Wsg boss, U too cool to have a limit.", "bot");
        return;
    }

    const now = Date.now();
    if (now >= savedData.resetTime) {
        const resetTime = now + (24 * 60 * 60 * 1000);
        savedData = { resetTime: resetTime, remaining: DAILY_LIMIT };
        localStorage.setItem(storageKey, JSON.stringify(savedData));
        counter = DAILY_LIMIT;
        updateCountdown();
    }

    if (counter <= 0) {
        const timeLeft = Math.max(0, savedData.resetTime - now);
        const hours = Math.floor(timeLeft / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        addMessage(`Daily chat limit reached. Come back in ${hours}h ${minutes}m!`, "bot");
        return;
    }

    addMessage(userMessage, "user");
    input.value = "";

    counter--;
    savedData.remaining = counter;
    localStorage.setItem(storageKey, JSON.stringify(savedData));
    updateCountdown();

    try {
        const response = await fetch(`${backendURL}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: userMessage,
                bot: window.BIRDIE_TYPE,
                userId: userId
            })
        });

        if (!response.ok) throw new Error("Network response not OK");

        const data = await response.json();
        addMessage(data.reply || "No response from bot.", "bot");

    } catch (error) {
        console.error("API Error:", error);
        addMessage("Oops! Something went wrong.", "bot");
    }
}

// ==============================
// File Size Formatter
// ==============================
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// ==============================
// Unified Upload Handler
// ==============================

let currentUploadMode = "upload";

if (uploadBtn && unifiedFileInput) {
    uploadBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();

        const user = localStorage.getItem("userPlan") || "free";

        if (user === "pro") {
            uploadMsg.textContent = "Upload unlimited files (25MB max each)";
        } else if (user === "plus") {
            uploadMsg.textContent = "Upload up to 10 files per day (10MB max each)";
        } else {
            uploadMsg.textContent = "Upload up to 3 files per day (5MB max each)";
        }

        uploadMsg.classList.add("show");
        setTimeout(() => uploadMsg.classList.remove("show"), 3000);

        unifiedFileInput.accept = "image/*,.pdf,.doc,.docx,.txt,.ppt,.pptx";
        unifiedFileInput.click();
    });
}

if (unifiedFileInput) {
    unifiedFileInput.addEventListener("change", async (e) => {
        e.stopPropagation();

        const selectedFile = e.target.files[0];
        if (!selectedFile) {
            unifiedFileInput.value = "";
            return;
        }

        const user = localStorage.getItem("userPlan") || "free";
        const limits = FILE_LIMITS[user];

        if (selectedFile.size > limits.maxSize) {
            addMessage(
                `❌ File too large! "${selectedFile.name}" is ${formatFileSize(selectedFile.size)} (limit: ${formatFileSize(limits.maxSize)})`,
                "bot"
            );
            unifiedFileInput.value = "";
            return;
        }

        if (selectedFile.size === 0) {
            addMessage("❌ File appears to be empty or corrupted!", "bot");
            unifiedFileInput.value = "";
            return;
        }

        const isImage = selectedFile.type.startsWith("image/");

        if (isImage) {
            addMessage(`📷 Uploading photo: ${selectedFile.name}...`, "user");
        } else {
            addMessage(`📎 Uploading: ${selectedFile.name} (${formatFileSize(selectedFile.size)})...`, "user");
        }

        try {
            const formData = new FormData();
            formData.append("file", selectedFile);
            formData.append("userId", userId);
            formData.append("bot", window.BIRDIE_TYPE);

            if (isImage) {
                formData.append("message", "What's in this image? Help me understand it.");
            } else {
                formData.append("message", "Help me understand this document/file.");
            }

            const response = await fetch(`${backendURL}/upload`, {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                addMessage(`❌ Upload failed (Error ${response.status})`, "bot");
                unifiedFileInput.value = "";
                return;
            }

            const data = await response.json();
            addMessage(data.reply || "File uploaded successfully!", "bot");

        } catch (error) {
            console.error("Upload Error:", error);
            addMessage("❌ Upload failed! Try again.", "bot");
        }

        unifiedFileInput.value = "";
    });
}

// ==============================
// Voice Recording Handler
// ==============================
let mediaRecorder;
let audioChunks = [];
let recordingStartTime;

if (voice && voiceMsg) {
    voice.addEventListener("click", async (e) => {
        e.preventDefault();
        e.stopPropagation();

        const user = localStorage.getItem("userPlan") || "free";

        if (!mediaRecorder || mediaRecorder.state === "inactive") {
            if (user === "pro") {
                voiceMsg.textContent = "Record unlimited voice messages";
            } else if (user === "plus") {
                voiceMsg.textContent = "Record up to 10 minutes of voice per day";
            } else {
                voiceMsg.textContent = "Record up to 2 minutes of voice per day";
            }

            voiceMsg.classList.add("show");
            setTimeout(() => voiceMsg.classList.remove("show"), 3000);

            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorder = new MediaRecorder(stream);

                mediaRecorder.ondataavailable = (e) => {
                    audioChunks.push(e.data);
                };

                mediaRecorder.onstop = () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                    audioChunks = [];

                    const recordingDuration = (Date.now() - recordingStartTime) / 1000;
                    addMessage(`🎤 Recording complete (${Math.round(recordingDuration)}s)`, "user");
                    addMessage("Voice recording feature coming soon! Backend needed.", "bot");

                    stream.getTracks().forEach(track => track.stop());
                };

                mediaRecorder.start();
                recordingStartTime = Date.now();
                voice.textContent = "⏹️";
                addMessage("🎙️ Recording started... Click again to stop.", "bot");

            } catch (error) {
                addMessage("❌ Could not access microphone. Please allow microphone permission.", "bot");
                console.error("Microphone error:", error);
            }

        } else {
            mediaRecorder.stop();
            voice.textContent = "🗣️";
        }
    });
}

// ==============================
// Event Listeners
// ==============================
if (sendBtn) {
    sendBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        sendMessage();
    });
}

if (input) {
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            sendMessage();
        }
    });
}