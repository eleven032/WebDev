console.log("Linked success")

document.getElementById("start").addEventListener("click", doWork);
console.log("");
let result = [];
function doWork(){
    result=document.getElementById("ourNewspaper").contentWindow
    console.log(result[0]);
    console.log(result[1]);
}

