// ternary operator =  a shortcut to if{} and else{} statements
//                     helps assign a variable based on a condition
//synatx:              condition ? codeIfTrue : codeIfFalse



//example 1
//let age = 21;
//age >=18 ? "You are an adult" : "You are a minor"

//instead of:
//if(age >=  18){
//    "You are an adult"
//    }
//else{
//    "You are a minor"
//    }


// example 2
//let isStudent = true;
//let message  = isStudent ? "You are a student." : "You are not a student."
//console.log(message);


//example 3
let purchaseAmount  =  125;
let discount  = purchaseAmount >= 100 ? "You get a 10% discount."  : "You do not get a discount."
console.log(discount)