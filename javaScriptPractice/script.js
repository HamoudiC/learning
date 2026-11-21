const input = document.getElementById("input");
const enter = document.getElementById("enter");
const message = document.getElementById("message");
const shock = document.getElementById("shock");
let val;
let sho; 


enter.addEventListener("click", function(e){

    val = input.value;
    message.textContent = `Your number is ${val}`;

    shock.textContent = "🤯🤯🤯";
    document.body.style.backgroundColor = "blue";

});
