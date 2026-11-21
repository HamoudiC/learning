// string methods = allows you to manipulate and work with text (strings)


//example 1
let userName =  "moontle";


//charAt.()
console.log(userName.charAt(2));        // outputs letter at the specified index or number. e.g: charAt(2) return o. since the second value in "moontle" is o.


//.length()
console.log(userName.length())          // outputs the length of "moontle", so 6.


//.trim
console.log(userName.trim);             // removes any white space iin between or on the sides of the string


//.toUpperCase
console.log(userName.toUpperCase);      // makes all letters uppercase


//.toLowerCase  
console.log(userName.toLowerCase);      // makes all letters lowercase


//.repeat()
console.log(userName.repeat(1));        // repeats the string, number in brackets is how many times you wanna repeat it.


//.startsWith()
console.log(userName.startsWith('m'));  // t or f, used to check if strings starts with a specific letter or character, case matters. 
                                        // Spacing also matters, " moontle" would start with a space instead of an 'm'

userName.startsWith('m') ? console.log("starts with 'm'.") : console.log("does not start with 'm'.");  //example of how .startsWith can be used. (if else can also work, this is ternary)


//.endsWith()
console.log(userName.endsWith('e'));    // t or f, used to check if strings ends with a specific letter or character, case matters. 
                                        // Spacing also matters, "moontle " would end with a space instead of an 'e'

userName.endsWith('e') ? console.log("ends with 'e'.") : console.log("does not end with 'e'.");  //example of how .endsWith can be used. (if else can also work, this s ternary)


//.includes()
console.log(userName.includes('e'));    //checks if the string includes a specific letter or character.

userName.includes('e') ? console.log("username includes the letter 'e'.") : console.log("username does not include the letter 'e'.");   //example of how .includes() can be used. 

//example 2

let phoneNumber = "123-456-7890";

//.replaceAll()
phoneNumber = phoneNumber.replaceAll("-","A");         // replaces all of a specified character with something else. the first " " is the character that is being replaced, the second " " 
                                                       // is what you are replacing it with. (you can even replace the character with a "" to delete the character or " " for space instead)
console.log(phoneNumber)                               

//.padStart()
phoneNumber = phoneNumber.padStart(17, "A");           // number specifies how long you want the string to be, if the string isnt as long as the value you inputted, 
                                                       // it will put as many characters in front of the string until it is the specifed length. If the number you input
                                                       // is shorter than the length of the string, nothing happens.
console.log(phoneNumber) 

//.padEnd()
phoneNumber = phoneNumber.padEnd(17, "A");            // number specifies how long you want the string to be, if the string isnt as long as the value you inputted, 
                                                      // it will put as many characters at the end of the string until it is the specifed length. If the number you input
                                                      // is shorter than the length of the string, nothing happens.
console.log(phoneNumber) 











