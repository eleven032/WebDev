var express = require("express");
var app = express();
var bodyparser = require("body-parser");
app.use(bodyparser.urlencoded({extended:true}));

var campgrounds = [
    {name:"camp1", image:"https://d2ciprw05cjhos.cloudfront.net/files/v3/styles/gs_large/public/images/18/06/gettyimages-649155058.jpg?itok=Lhx5ciAR"},
    {name:"camp2", image:"https://s3.amazonaws.com/imagescloud/images/medias/camping/camping-tente.jpg"},
    {name:"camp3", image:"https://cdn.vox-cdn.com/thumbor/-JoPdcgAuLTUsWiDZ62CX4wb33k=/0x0:5225x3479/1200x800/filters:focal(2195x1322:3031x2158)/cdn.vox-cdn.com/uploads/chorus_image/image/54137643/camping_tents.0.jpg"}
]
app.set("view engine","ejs");



app.get("/",(req,res)=>{
    res.render("landing");
});

app.get("/campgrounds",(req,res)=>{
    res.render("campgrounds",{campgrounds:campgrounds});
});



app.post("/campgrounds", (req,res)=>{
    var name = req.body.name;
    var image = req.body.image;
    var newCampground = {name:name, image:image};
    campgrounds.push(newCampground);
    res.redirect("/campgrounds");

});


app.get("/campgrounds/new",(req,res)=>{
    res.render("new");
})

app.listen(process.env.PORT||3000, ()=>{
    console.log("Connect successful");
});