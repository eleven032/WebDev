const mysql = require('mysql');

const pool = mysql.createPool({
    connectionLimit:10,
    password:'1130',
    user:'root',
    database:'test',
    port:'3306',
    host:'localhost'
})

let testdb = {};

testdb.all=()=>{
    return new Promise((resolve,reject)=>{
        pool.query('SELECT * FROM info',(err,results)=>{
            if(err){
                return reject(err);
            } 
            return resolve(results);
        })
    })
};


testdb.keyword_all=(keyword)=>{
    return new Promise((resolve,reject)=>{
        pool.query(`SELECT * FROM info WHERE keyword = ?`,[keyword],(err,results)=>{
            if(err){
                return reject(err);
            } 
            return resolve(results);
        })
    })
}

module.exports = testdb;