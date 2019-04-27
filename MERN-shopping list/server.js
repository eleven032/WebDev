const express = require("express");
const mongoose = require("mongoose");
const bodyparser = require("body-parser");


const app = express();


//middleware
app.use(bodyparser.json());

//DB config
const db = require("./config/keys").mongoURI;

//connect
mongoose.connect(db)
    .then(()=>console.log("DB connected"))
    .catch(err=>console.log(err));



const port = process.env.PORT || 5000;

app.listen(port, ()=>{
    console.log("Server start");
})

