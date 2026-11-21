// .checked = property that determines the chekced state of an HTML
// checkbox or radio button element

const myCheckbox = document.getElementById("myCheckbox")
const visaBtn = document.getElementById("visaBtn");
const masterCardBtn = document.getElementById("masterCardBtn");
const paypalBtn = document.getElementById("paypalBtn");
const mySubmit = document.getElementById("mySubmit")
const subResult = document.getElementById("subResult")
const paymentResult = document.getElementById("paymentResult")


mySubmit.onclick = function(){

    if(myCheckbox.checked){
        subResult.textContent = 'You are subscribed!';
    }
    else{
        subResult.textContent = 'You are NOT subscribed!';
    }
}

if(visaBtn.checked){
    paymentResult.textContent = 'You are paying with VISA.';
}

else if(masterCardBtn.checked){
    paymentResult.textContent = 'You are paying with MASTERCARD.';
}

else if(paypalBtn.checked){
    paymentResult.textContent = 'You are paying with PAYPAL.';
}

else{
    paymentResult.textContent = 'You must select a payment type.'
}


