//   = assignment operator
//  == comaprison operator (comapre if values are equal)
// === strict equality operator (compare if values & datatypes are equal)
//  != inequality operator
// !== strict inequality operator

const pi = 3.14;

//equality
if(pi == 3.14){                             // i could make 3.14 here a string and it would still return true since its not as strict as ===
    console.log("That is PI")
}
else{
    console.log("That is not PI")
}

if(pi === "3.14"){                          // === means that it checks if the value is equal AND matches the data type like string, number etc.. usually == dosent care but === does.
    console.log("That is PI")
}
else{
    console.log("That is not PI")
}

//inqeaulity
if(pi != 3.12){                             // i could make 3.12 here a string and it would still return false since its not as strict as ===
    console.log("That is NOT PI")
}
else{
    console.log("That is nt PI")
}

if(pi !== "3.14"){                          // === means that it checks if the value is NOT equal AND does NOT match the data type like string, number etc.. usually == dosent care but === does.
    console.log("That is NOT PI")
}
else{
    console.log("That is PI")
}
