var express = require("express");
var app = express();

app.set("view engine", "ejs");
app.get("/", (req, res) => {
    res.render("landing")
});


app.get("/campgrounds", (req, res) => {
    let arr = [
        { name: "whale1", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" },
        { name: "whale2", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" },
        { name: "whale3", image: "https://en.pimg.jp/047/206/497/1/47206497.jpg" }
    ];
    res.render("campgrounds", {arr:arr});
})
app.listen(process.env.PORT || 3000, () => {
    console.log("connect");
});