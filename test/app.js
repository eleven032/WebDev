const express = require('express');
const app = express();
const request = require('request');
var bodyparser = require("body-parser");
app.use(bodyparser.urlencoded({ extended: true }));




let url = "https://www.newspapers.com/search/#query=hurricane"

// const superagent = require('superagent');
// superagent.gest(url).end((err, res)=>{
//     if(err){
//         console.log(`connection fail-${err}`);
//     } else {
//         console.log(res.text);
//     }
// })

request(url,{json:true},(err,res,body)=>{
   if(err){
    console.log(`connection fail-${err}`);
   } else {
     console.log(body);
   }
})
















app.get('/', function (req, res) {
    res.send('Hello World!');
});

let server = app.listen(3000, function () {
    let host = server.address().address;
    let port = server.address().port;
    console.log('Your App is running at http://%s:%s', host, port);
});



