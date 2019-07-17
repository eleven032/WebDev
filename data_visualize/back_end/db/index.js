const mysql = require('mysql');

const pool = mysql.createPool({
    connectionLimit: 10,
    password: '1130',
    user: 'root',
    database: 'test',
    port: '3306',
    host: 'localhost'
})

let testdb = {};

testdb.all = () => {
    return new Promise((resolve, reject) => {
        pool.query('SELECT * FROM infos', (err, results) => {
            if (err) {
                return reject(err);
            }
            return resolve(results);
        })
    })
};


testdb.keyword_all = (keyword) => {
    return new Promise((resolve, reject) => {
        pool.query(`SELECT * FROM infos WHERE keyword = ?`, [keyword], (err, results) => {
            if (err) {
                return reject(err);
            }
            return resolve(results);
        })
    })
}


testdb.import_all = (data) => {
    return new Promise((resolve, reject) => {
        console.log(data)
        data.forEach(row => {
            let keyword = row[0];
            let location = row[1];
            let year = Number(row[2]);
            let freq = Number(row[3]);
            // console.log([keyword, location, year, freq])
            pool.query('INSERT INTO infos (keyword, location, year, freq) VALUES (?,?,?,?)', [keyword, location, year, freq], (err, results) => {
                if (err) {
                    // console.log("fail at insert data");
                    return reject(err);
                }
                console.log("good at insert data");
                
            })
        });
        return resolve(results);
    })
}
module.exports = testdb;