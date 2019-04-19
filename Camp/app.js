var express = require("express");
var app = express();
var bodyparser = require("body-parser");
app.use(bodyparser.urlencoded({ extended: true }))
app.set("view engine", "ejs");
app.get("/", (req, res) => {
    res.render("landing")
});
let arr = [
    { name: "whale1", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" },
    { name: "whale2", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" },
    { name: "whale3", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" }
];

app.get("/campgrounds", (req, res) => {
    
    res.render("campgrounds", { arr: arr });
})


app.post("/campgrounds", (req, res) => {
    // res.send("at post part");
    var newshit = {
        name:req.body.name,
        image:req.body.img
    }
    
    
    arr.push(newshit);
    res.redirect("/campgrounds");
})


app.get("/campgrounds/new",(req,res)=>{
    res.render("new");
})
   

app.listen(process.env.PORT || 3000, () => {
    console.log("connect");
});