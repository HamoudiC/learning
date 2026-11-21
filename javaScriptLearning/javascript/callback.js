// callback =  allows a function to call another function
         
//              used to handle asynchronous operations.
//              e.g. fetching data from a server, reading files,   

//              "when you finish this, do this next"

sum(displayPage, 1,2)

function sum(callback, x,y){
    let result = x + y;
    callback(result)
}

function displayConsole(result){
    console.log(result)
}

function displayDOM(result){
    document.getElementById("myH1").textContent = result;
}
