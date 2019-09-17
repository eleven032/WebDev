//hardcode for PA, need change to passed in function, like what we did at last program, get a list of location and pass in
let pla = "PA";
//same as last project, change to variable
let year = "1900";

//get totall papaer number
let target = document.getElementById("paper_count");
let number = target.innerText.split(" ")[0];

//create filename 
//file context is like 'year,location,number'
//such as "1900,PA,165"
let filename = year + "_" + pla + ".txt";
let context = year + "," + pla + "," + number

//download the file
function down(a) {
    let tmp = document.createElement("a");
    tmp.href = "data:text/plain;charset=utf-8," + encodeURI(a);
    tmp.download = filename;
    tmp.click();
};
down(context);