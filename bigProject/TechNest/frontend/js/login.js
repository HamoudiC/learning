import { userId } from "./birdieScript.js";

const enterBtn = document.getElementById("enter");
const usernameInput = document.getElementById("username-input");

enterBtn.addEventListener("click", () => {
    const name = usernameInput.value.trim();

    if (name === "") return;

    localStorage.setItem("userId", name);
    enterBtn.disabled = true;

    const conf = document.createElement("p");
    conf.style.marginTop = "10px";
    enterBtn.insertAdjacentElement("afterend", conf);

    setTimeout(() => {
        location.href = "../index.html";
    }, 1500);
});