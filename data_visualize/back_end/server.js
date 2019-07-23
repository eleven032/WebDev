const express = require('express');
const apiRouter = require('./routes/index');
const cors = require("cors");
const app = express();

app.use(cors());
app.use(express.json());
app.use('/api', apiRouter);


app.listen(process.env.PORT||'4000', ()=>{
    console.log(`runing at port ${process.env.PORT||4000}`)
})