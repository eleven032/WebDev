const express = require("express");
const mongoose = require("mongoose");
const bodyparser = require("body-parser");

const items = require('./routes/api/items');

const app = express();


//middleware
app.use(bodyparser.json());


//---------------------------------------------------
//DB config
mongoose
const db = require("./config/keys").mongoURI;

//connect
mongoose.connect(db, { useNewUrlParser: true })
    .then(() => console.log("DB connected"))
    .catch(err => console.log(err));
//---------------------------------------------------



//use routes
app.use('/api/items', items);












const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log("Server start");
})

