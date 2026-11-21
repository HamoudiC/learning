// array = a variable like structure that can hold more than one value

let fruits = ["apple","orange","banana"];

//for loop to go through all the items in the array
for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}

//reverse for loop to go through all the items in the array
for(let  i = fruits.length -1; i>= 0; i--){
    console.log(fruits[i]);
}

//sort alpahbetically a-z

fruits.sort();


//sort alpahbetically z-a

fruits.sort().reverse;