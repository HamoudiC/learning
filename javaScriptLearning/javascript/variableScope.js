// variable scope = where a variable is recognized and accessible (local vs global)

let x=9;    //global
console.log(x);
one();
two();

function one(){
    let c =1;       //local
    console.log(c)
}

function two(){
    console.log(x);        //this will output 9 because its global
    console.log(c);        //this wont work because we funtions cant see inside other funtions.
}