const express = require('express');
const apiRouter = require('./routes/index');

const app = express();

app.use(express.json());
app.use('/api', apiRouter);


app.listen(process.env.PORT||'3000', ()=>{
    console.log(`runing at port ${process.env.PORT||3000}`)
})