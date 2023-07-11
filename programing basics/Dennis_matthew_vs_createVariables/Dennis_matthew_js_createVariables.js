// I used const because the park limit is unchangeable 
const heightRestiction = 42;
const ageRestriction = 10;

// I used a prompt to ask age and height because they can be changed
// prompt("what is your age?");
//im taking the number that is in the form feild and I'm storing the value of age into variable
let age = ageInput;
let height = heightInput;

document.getElementsByClassName(ageInput) = age;

let getElementsByClassName(heightInput) = height;


age.addEventListener("btn", parkRestriction());

height.addEventListener("btn", parkRestriction());

getElementById(btn).addEventListener("input", function { (alert("button pressed") } ));

        //    prompt("what is your height in inches?")

        // I used an if statement to set conditions
        function parkRestriction("btn") {
            if (height < heightRestiction || age < ageRestriction) {
                alert("You can not ride this ride!")
            } else {
                alert("You may ride!")
            }
        }

console.log(age)
//    , function (parkRestriction) { }