// string slicing  = creating a substring from a protion of another string
//
// formula:          string.slice(start,end);


//const fullName = "Mohamad Ali Cheaito"

//example 1
//first name and last name splitting
//let firstName = fullName.slice(0,11);    //always add +1 number to the end of name because the last digit is not included.
//let lastName = fullName.slice(12);       //you dont need a end number for the last name because the string ends, so we dont need to specify the ending.
                                        // if you try to string slice somehting in the middle of a string, you need to specify the start and end.

//character slicing
//let firstCharacter = fullName.slice(0,1);
//let lastCharacter = fullName.slice(-1);     //-1 just means last character in a string, the more negative you go, the more strings from the begining to end show up.
                                            //you can also just count the characetrs and output the number of the last character, -1 is just faster if you dont wanna count.

//console.log(firstName);
//console.log(lastName);
//console.log(firstCharacter);
//console.log(lastCharacter);

//example 2
//const fullName = "Mohamad Cheaito"
//let firstName = fullName.slice(0, fullName.indexOf(" "))        //first name ends when a space is found
//let lastName = fullName.slice(fullName.indexOf(" "))            //last name starts when a space is found 

//example 3
const email = "habood0176@gmail.com";

let username  =  email.slice(0, email.indexOf("@"));              //lets only the characters before the @ sign to be outputted
console.log(username);           

let extension  =  email.slice(email.indexOf("@")+1);              //outputs all the characters after the @ sign (remove the +1 if you want to output the @ as well)
console.log(extension);   









