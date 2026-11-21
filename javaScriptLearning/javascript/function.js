// function = A section  of reusable code.
//            Declare code once, use it whenevr you want.
//            Call the funtion to execute that code.

//example 1: normal funcion

//function happyBirthday(username, age){

//    console.log("Happy birthday to you.")
//    console.log("Happy birthday to you.")
//    console.log("Happy birthday dear "+username)
//    console.log("Happy birthday to you.")
//    console.log("You are now "+age+"!")

//}

//happyBirthday("hamoudi", 18);               //name then age just like the parameters in the funtion. Its order specific



//example 2: return funtions

function subtract(x,y){
    return x-y;
}

function divide(x,y){
     return x/y;
}

function multiply(x,y){
    return x*y
}

function isEven(number){
    return number%2 === 0? true : false;
}

function isValidEmail(email){
    if(email.includes("@")){
        return true;
    }
    else{
        return false;
    }
}

console.log(isValidEmail("hamoudi0716@gmail.com"))


function add(x,y){
    let result = x+y;
    return result;                              //dosent print, you need another variable to let this one print.
}

let answer = add(1,2);                          //answer is the new variable so that result can be outputted.
console.log(answer);

//faster way

console.log(add(1,2));                          //same procces except you dont need another variable, you just output the function itself.
console.log(subtract(3,4));
console.log(multiply(2,3))
console.log(divide(1,1));
console.log(isValidEmail("hamoudi0716@gmail.com"));
console.log(isValidEmail("hamoudi0716gmail.com"));
console.log(isEven(4));
console.log(isEven(5));




