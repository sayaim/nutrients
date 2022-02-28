const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'rice',
    database: 'myapp'
});


const sql = 'create table test(id auto-increment, name text);';

connection.connect(function(err){  
    if(err)throw err;  
    connection.query(sql,function(err,result){  
        if(err)throw err;  
        console.log( "テーブルが作成されました"); 
    }); 
});