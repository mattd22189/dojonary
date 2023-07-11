function hide(btn){
    btn.remove();
}
let count1=0;
function add1(){
    document.querySelector(".add1").innerText= count1 + "petting(s)";
    count1++ 
}
let count2=0;
function add2(btn){
    document.querySelector(".add2").innerText= count2 + "petting(s)";
    count2++ 
}
let count3=0;
function add3(btn){
    document.querySelector(".add3").innerText= count3 + "petting(s)";
    count3++ 
}
    let pet = document.getElementById("pet").value 
    let cat = document.getElementById("cat").value
    let dog = document.getElementById("dog").value

    function select(cat,dog){
    if (pet == cat){
        alert("this is a cat");
    } else if (pet == dog){
        alert("this is a dog");
    } 
    return pet
}
select(pet,pet);
