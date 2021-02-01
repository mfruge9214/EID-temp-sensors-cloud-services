

// Code referenced:
// https://github.com/microsoft/sql-server-samples/tree/master/samples/tutorials/node.js/Windows/SqlServerSample


const sql = require('mssql')

var connectionParameters = {
	server: 'localhost',
	database: 'TempSensorDB',
	};




async () => {
    try {
        // make sure that any items are correctly URL encoded in the connection string
        let conn = await sql.connect(connectionParameters);
        const result = await sql.query`select * from mytable where id = ${value}`
        console.dir(result)
    } catch (err) {
        // ... error checks
    }
}

