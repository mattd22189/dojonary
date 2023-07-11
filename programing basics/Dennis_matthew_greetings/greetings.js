
//let hour = Date().slice(16,18);

// I created a function that multiplied hour by 1 to turn from a string into a number.
function concat(hour,number){
  return hour * number
}
//I pulled the date function from the computer and stored it inside the variable hour.
// then sliced the part of the string that represent hour.
// I stored concat into present_time variable with Date function as a parameter multiplied by the number 1 to turn it into a string. 
let present_time = concat(Date().slice(16,18),1)

// I called a function named time_of_day and stored an if statement that took the present_time 
// then converted it into a string based on the hours of the day by their proposed time slots 
//night, morning, afternoon, and evening. 


function time_of_day(){ 
if (present_time >= 0 && present_time <= 5){
  time = "night"
 }else if(present_time > 5 && present_time <= 11){
  time = "morning"
 } else if (present_time > 11 && present_time <= 17){
   time = "afternoon" 
  } else if (present_time > 17 && present_time <= 23){
  time = "evening"
  }
return time
}
console.log(time_of_day())

user_name = "what is your name?"

question = prompt(user_name)

if (question == "Count Dooku"){
  answer = alert("Hello" + " " + question + " " + "good" + " " + time_of_day() + ", " + "I'm coming for you, Dooku!")
} else {
  answer = alert("Hello" + " " + question + " " + "good" + " " + time_of_day())
}