// SWITCH =  can be an effecient replacement to many else if statements.


//no switch statement
//let day = 2;

//if(day = 1){
//    console.log("It is Monday")
//}

//else if(day = 2){
//    console.log("It is Tuesday")
//}

//else if(day = 3){
//    console.log("It is Wednesday")
//}

//else if(day = 4){
//    console.log("It is Thursday")
//}

//else if(day = 5){
//    console.log("It is Friday")
//}

//else if(day = 6){
//    console.log("It is Saturday")
//}

//else if(day = 7){
//    console.log("It is Sunday")
//}

//else{
//    console.log("This day does not exist")
//}

//switch statement example 1
//let day = 1;

//switch(day){
//    case 1: console.log("It is Monday"); break;
//    case 2: console.log("It is Tuesday"); break;
//    case 3: console.log("It is Wednesday"); break;
//    case 4: console.log("It is Thursday"); break;
//    case 5: console.log("It is Friday"); break;
//    case 6: console.log("It is Saturday"); break;
//    case 7: console.log("It is Sunday"); break;

//    default: console.log(`${day} is not a day`);      //You dont need a break for the last case since there is nothing afetr it.
//}


//switch example 2

let testGrade = 90;
let letterGrade;

switch(true){
    case testGrade >= 90: letterGrade = "A"; break;
    case testGrade >= 70: letterGrade = "B"; break;
    case testGrade >= 51: letterGrade = "C"; break;

    default: letterGrade = "F";                         //You dont need a break for the last case since there is nothing after it.
}
console.log(letterGrade);
