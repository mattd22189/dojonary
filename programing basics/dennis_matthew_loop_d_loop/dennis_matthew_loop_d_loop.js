//How do we know we need a loop here?
// we know we need a loop because the runner has to receive a reward for every mile so the condition must run a minimum of 6 times. 

//What's the starting point of the loop? 
// the loop starts at zero because the runner starts at 0 miles ran. 

//When should the loop stop?
//the loop should stop at the 6th mile

//How will the loop know when to stop?
// the loop will stop when the condition is met, when the condition is met it is true. 

//What's incrementing for each iteration of the loop?
//the miles increment on each iteration or lap

//What variables do we need?
//the variables are "let" because it will change with every lap it increments 
for (let mile = 0; mile < 20; mile++ ){
if ( mile != 6 ) {
console.log("mile " + mile + " here is a piece of candy");
} else {
    console.log("sorry no candy this lap")
}

}

