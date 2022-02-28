const mysql = require('mysql');

const con = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'rice',
	database: 'myapp'
});
const foodData = [
    { name: 'キャベツ', va: true },
    { name: 'キャベツ', va: true , ve: true },
    { name: 'キャベツ', vd: true , vk: true },
];
con.connect();
const sql = 'INSERT INTO nutrients SET ?;';

for (const food of foodData) {
    con.query(sql,[food],(err, res) => {
        if(err) throw err;
        console.log(food.name)
    });
}














