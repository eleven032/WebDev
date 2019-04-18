var express = require("express");
var app = express();
var request = require("request");

app.set("view engine", "ejs");

app.get("/",(req,res)=>{
    res.render("search");
});

app.get("/results", (req,res)=>{
    let val = req.query.val;
    // console.log(val);
    let url = "http://www.omdbapi.com/?s="+val+"&apikey=thewdb ";
    request(url, (error, response, body)=>{
        if(!error&&response.statusCode==200){
            var data = JSON.parse(body);
            res.render("results", {data: data});
        }
    })
});

app.listen(process.env.PORT||3000, process.env.IP, ()=>{
    console.log("start here!");
});