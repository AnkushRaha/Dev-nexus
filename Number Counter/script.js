let count=0
const counter = document.getElementById("count");

//update color function
function updateDisplay(){
    counter.textContent = count;
    if(count > 0){
        counter.style.color = "#00ffae";
    }
    else if(count < 0){
        counter.style.color = "#ff4d4d";
    }
    else{
        counter.style.color = "#ffffff";
    }
}

//increase function
document.getElementById("increase").onclick = function(){
    count++;
    updateDisplay(); 
}
//decrease function
document.getElementById("decrease").onclick = function(){
    count--;
    updateDisplay();
}
//reset function
document.getElementById("reset").onclick = function(){
    count = 0;
    updateDisplay();  
}