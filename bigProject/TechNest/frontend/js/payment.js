const plan = ["free", "plus", "pro"];

let user = localStorage.getItem("userPlan") || plan[0];

// ==============================
// DOM Element References
// ==============================
const upgradeBtn = document.getElementById("upgrade");
const planMsg = document.getElementById("planMsg");
const pageName = document.getElementById("pageName");
const pageDisc = document.getElementById("pageDisc");

// Payment page elements
const free = document.getElementById("free");
const plus = document.getElementById("plus");
const pro = document.getElementById("pro");

// Confirm Message
const freeConfirm = document.getElementById("basic-confirmMsg");
const plusConfirm = document.getElementById("plus-confirmMsg");
const proConfirm = document.getElementById("pro-confirmMsg");

// Features List
const freeFeatures = document.getElementById("freeFeatures");
const plusFeatures = document.getElementById("plusFeatures");
const proFeatures = document.getElementById("proFeatures")


// ==============================
// Plan display on button
// ==============================

if(upgradeBtn){
    if(user === plan[0]){
        upgradeBtn.textContent = "UPGRADE PLAN"
        planMsg.textContent = "Ready to enhance your experience?"
    }
    else if(user === plan[1]){
        upgradeBtn.textContent = "Plus Plan Active ✅"
        planMsg.textContent = "Enjoying Plus? Try Pro!";
    }
    else if(user === plan[2]){
        upgradeBtn.textContent = "Pro Plan Active ✅"
        planMsg.textContent = "Thank you for using Pro!";
    }
}

if(pageName){
    if(user === plan[0]){
        pageName.textContent = "Free Mode";
        pageDisc.textContent = "Upgrade your experience!"
    }
    else if(user === plan[1]){
        pageName.textContent = "Plus Mode"
        pageDisc.textContent = "Consider upgrading to Pro!"
    }
    else if(user === plan[2]){
        pageName.textContent = "Pro Mode"
        pageDisc.textContent = "Thanks for using TechNest!"
    }
}

// ==============================
// Function Message based on plan
// ==============================

if(free) {
    free.addEventListener("click", ()=>{
        user = plan[0];
        freeFeatures.textContent = ["30 Messages daily with each bot ✔️\n",
                                    "Upload up to 3 files per day (5MB max each) ✔️\n", 
                                    "Record up to 2 minutes of voice per day ✔️\n", 
                                    "Custom Prompts ✖️\n", 
                                    "Memory ✖️"]

        plusFeatures.textContent = "";
        proFeatures.textContent = "";
        localStorage.setItem("userPlan",user);
        freeConfirm.textContent = "Free Plan Confirmed ✅"
        proConfirm.textContent = "";
        plusConfirm.textContent = "";
    })
}

if(plus) {
    plus.addEventListener("click", () => {
        user = plan[1];
           freeFeatures.textContent = "";
           plusFeatures.textContent = ["\n30 Messages daily with each bot ✔️\n",
                                       "\nUpload up to 5 files per day (10MB max each) ✔️", 
                                       "\nRecord up to 10 minutes of voice per day ✔️", 
                                       "\nCustom Prompts ✔️", 
                                       "\nMemory ✔️"];
            proFeatures.textContent = "";

        localStorage.setItem("userPlan", user);
        freeConfirm.textContent = "";
        plusConfirm.textContent = "Plus Plan Confirmed! ✅";
        proConfirm.textContent = "";
    });
}

if(pro) {
    pro.addEventListener("click", () => {
        user = plan[2];
        freeFeatures.textContent = "";
        plusFeatures.textContent = "";
        proFeatures.textContent = ["Unlimited Messages daily with each bot ✔️",
                                   "Unlimited upload files (25MB max each) ✔️", 
                                   "Unlimited Voice recording ✔️", 
                                   "Custom Prompts ✔️", 
                                   "Memory ✔️",
                                   "Detailed Messages ✔️"];

        localStorage.setItem("userPlan", user);
        freeConfirm.textContent = "";
        plusConfirm.textContent = "";
        proConfirm.textContent = "Pro Plan Confirmed! ✅";
    });
}