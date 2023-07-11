// I used const because the park limit is unchangeable 
const heightRestiction = 42;
const ageRestriction = 10;

// I used a prompt to ask age and height because they can be changed
let age = prompt("what is your age?");
let height = prompt("what is your height in inches?")

// I used an if statement to set conditions
if (height < heightRestiction || age < ageRestriction) {
    alert("You can not ride this ride!")
}else{
    alert("You may ride!")
}