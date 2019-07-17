const express = require('express');
const db = require('../db');
const fs = require('fs');
const router = express.Router();


let path = 'C:/Users/Arthur/Desktop/test'



//get request 
//return all data inside the table
router.get('/', async (req, res, next) => {
    try {
        let results = await db.all();
        res.json(results);
    } catch (e) {
        console.log(e);
        res.sendStatus(500);
    }
})


//get one item 
//return special keyword with all matched data
router.get('/:keyword', async (req, res, next) => {
    try {
        let results = await db.keyword_all(req.params.keyword);
        res.json(results);
    } catch (e) {
        console.log(e);
        res.sendStatus(500);
    }
})

//todo:
//create new row and insert into database
router.post('/csv', async (req, res, next) => {
    try {

        //read all files inside dir 
        fs.readdir(path, (err, files) => {
            if (err) {
                console.log("read dir fail")
            }

            //deal with each file
            files.forEach(file => {
                let file_path = path + "/" + file;
                let keyword = file.split("_")[1].slice(0, -4);

                fs.readFile(file_path, async(err, data) => {
                    try{
                        if (err) {
                            console.log("got err at single file read");
                        }
                        data = data.toString();
                        let results = format_data(keyword, data);
                        let a = await db.import_all(results);
                        res.json(a);
                    }catch(e1){
                        console.log(e1);
                        res.sendStatus(500);
                    }
                    
                })
            })
        })
    } catch (e) {
        console.log(e);
        res.sendStatus(500);
    }
})

function format_data(keyword, data) {
    let new_rows = [];
    let rows = data.split("\r\n");
    let locations = rows[0].split(",").slice(1);
    for (let i = 1; i < rows.length; i++) {
        //[year,x,x,x,x,x,x,x,x,x,x,x...]
        let curr_year_row = rows[i].split(",");
        for (let j = 0; j < locations.length; j++) {
            let tuple = [];
            //[keyword]
            tuple.push(keyword);
            //[keyword,location]
            tuple.push(locations[j]);
            //[keyword,location,year]
            tuple.push(curr_year_row[0]);
            //[keyword,location,year,freq]
            tuple.push(curr_year_row[j + 1]);
            new_rows.push(tuple);
        }

    }

    return new_rows;
}
module.exports = router;