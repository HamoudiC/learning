// while loop  = repeat some code WHILE some codition is true

//example 1: do while loop.                          username dosent need to be defined since the code will
//                                                  run at least once before checking the while statement
//let username;

//do{
//    username = window.prompt('enter your name')
//}while(username === "" || username === null);

//console.log("hello "+username);



//example 2: while loop.                            username needs to be defined for the while loop to run 
//                                                 otherwise it will just skip over the loop completely
//let username = "";

//while(username === "" || username === null){
//    username = window.prompt('enter your name')
//}

//console.log("hello "+username);




//example 3: log in using while loop. 

//let loggedIn = false;
//let username;
//let password;

//while(!loggedIn){
//    username = window.prompt("Enter your username.");
//    password = window.prompt("Enter your password.");

//    if(username === "bob" && password === "joe"){
//        loggedIn = true;
//        console.log("you are now logged in.");
//    }
//    else{
//        console.log("invalid credentials. Try again.");
//    }
//}




//example 4:   same example but with loggedIn set as: true.

//let loggedIn = true;                                            
//let username;
//let password;

//while(!loggedIn){                                               //while loop gets skipped because the condition is not met.
//   username = window.prompt("Enter your username.");
//    password = window.prompt("Enter your password.");

//    if(username === "bob" && password === "joe"){
//        loggedIn = true;
//        console.log("you are now logged in.");
//    }
//    else{
//       console.log("invalid credentials. Try again.");
//    }
//}

//example 4:   do-while example but with loggedIn set as: true.
let loggedIn = true;                                            
let username;
let password;

do{                                               //a do while loop still works because there is no conditions for the do part. Even if loggedIn is set to true, it sill runs at 
                                                  //least one time. when it gets to the while part, it checks the condition, if its not met it will keep running until its met, in 
                                                  // this case loggedIn is already true so all it needs to do is run the code until something checks it.
   username = window.prompt("Enter your username.");
    password = window.prompt("Enter your password.");

    if(username === "bob" && password === "joe"){
        loggedIn = true;
        console.log("you are now logged in.");
    }
    else{
        console.log("invalid credentials. Try again.");
    }
}while(!loggedIn);