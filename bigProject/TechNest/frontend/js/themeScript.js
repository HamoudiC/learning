// ===============================
// DETECT CURRENT PAGE LOCATION
// ===============================
const currentPath = window.location.pathname;
const isIndexPage = currentPath.includes('index.html') || currentPath.endsWith('/frontend') || currentPath.endsWith('/frontend/');
const isHtmlFolder = currentPath.includes('/html/');

let pathPrefix;
if (isIndexPage) {
    pathPrefix = './css/';
} else if (isHtmlFolder) {
    pathPrefix = '../css/';
} else {
    pathPrefix = '../css/';
}

// ===============================
// LOAD SAVED THEME
// ===============================
const themeLink = document.getElementById("theme-link");
const savedThemeName = localStorage.getItem("selectedThemeName") || "themeDark.css";

if (themeLink) {
    themeLink.href = pathPrefix + savedThemeName;
}

// ===============================
// THEME SELECTOR HANDLING 
// ===============================
const themeSelect = document.getElementById("theme-select");

if (themeSelect) {
    themeSelect.value = savedThemeName;

    themeSelect.addEventListener("change", () => {
        const themeName = themeSelect.value;
        themeLink.href = pathPrefix + themeName;
        localStorage.setItem("selectedThemeName", themeName);
    });
}

// ===============================
// SETTINGS SIDEBAR ANIMATION 
// ===============================
const settingsBtn = document.getElementById("settings-btn");
const settingsPopup = document.getElementById("settings-popup");
const closeSettings = document.getElementById("close-settings");

if (settingsBtn && settingsPopup && closeSettings) {
    settingsBtn.addEventListener("click", () => {
        settingsPopup.classList.remove("hidden");
        settingsBtn.style.opacity = "0";
        settingsBtn.style.pointerEvents = "none";
    });

    closeSettings.addEventListener("click", () => {
        settingsPopup.classList.add("hidden");

        setTimeout(() => {
            settingsBtn.style.opacity = "1";
            settingsBtn.style.pointerEvents = "auto";
        }, 300);
    });
}



  //im gonna move this code into script.js when i figure out what it means. I will have to link the js file to this one when i do.
  //i did it yay.

