function change(element){
    if (element.innerText !="Login"){
    element.innerText ="Login"
    } else if(element.innerText != "Logout"){
    element.innerText = "Logout"
    }
    
}

//var counter = document.querySelector("#btn");

let counterOne=0;
function like1(button){
   button.innerText = (counterOne + " Likes");
   counterOne++;
    }

    let counterTwo=0;
    function like2(button){
       button.innerText = (counterTwo + " Likes");
       counterTwo++;
        }
    
    


function hide(btn){
    btn.remove();
} 

