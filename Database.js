/*
	File: Database.js
	Author: Mike Fruge & Bryan Cisneros
	Description: This file contains all resources needed to interface with a SQL database and conduct Truncate and Insert SQL transactions
					Connection parameters must be changed to reflect desired DB connection parameters
*/

// Code referenced:
// https://github.com/microsoft/sql-server-samples/tree/master/samples/tutorials/node.js/Windows/SqlServerSample
// https://www.npmjs.com/package/mssql#connection-pools

const sql = require('mssql')

// Table name used when Transacting with DB
const TableName = 'dbo.Sensor_Data_Test'


// Defines SQL server and database, as well as other connection parameters
const connectionParameters = {
	server: 'localhost',
	database: 'SensorData_1',
	user : 'eid',
	password : 'eid',
	pool: {
		max: 10,
		min: 0,
		idleTimeoutMillis: 20000,
		}
	};


// Connection pool object
const pool = new sql.ConnectionPool(connectionParameters);

// DB connection with callback 
// Clear DB table on connection opened, else report error
//		(The DB will be cleared by each thread, not a problem for this implementation but not desireable)
const poolConnect = pool.connect( err => {
	if(err){
		console.log('Error Creating Connection');
	}
	else{
		console.log(' Connection to DB Successful ');

		// Run TRUNCATE SQL command on TableName
		clearTable();
	}
});


// function: makeQuery
// args: sql_cmd
//			string of text used as argument to SQL
// note: asyncronus function with try/catch and await statements, allows event loop to continue until Promise is fulfilled

async function makeQuery(sql_cmd) {
    await poolConnect; // ensures that the pool has been created
    try {
        const request = pool.request(); // or: new sql.Request(pool1)
        const result = await request.query(sql_cmd);
        console.dir(result);
        return result;

    } catch (err) {
        console.error('SQL error', err);
        return null;
    }
}



// function: createNewEntry
// desc: this function is used by each sensor to add the last measurment into the database
// args: data
//		Object with key value pairs corresponding to database columns and values to insert
var createNewEntry = function (data) {

	var update_cols = '';
	var update_vals = '';

	for (const [key, value] of Object.entries(data)){
		if(key === 'ErrorCount'){
			update_cols += key;
			update_vals += String(value);
		}
		else {
			update_cols += key + ', ';
			update_vals += String(value) + ', ';
		}
	}

	insert_q = "INSERT INTO " + TableName + ' (' + update_cols + ')' + 'VALUES (' + update_vals + ')';
	console.log(insert_q);

	var res = makeQuery(insert_q);

	if(res === null){
		console.log('Query failed' + '\n' + insert_q);
	}
	else{
		console.log(res);
	}

}

// function: clearTable
// desc: this function is used to clear the database before the first temp measurment is inserted

var clearTable = function(){

	var delete_q = 'TRUNCATE TABLE ' + TableName;

	console.log(delete_q);

	var res = makeQuery(delete_q);

	if(res === null){
		console.log('Could not clear table of values');
	}
	else{
		console.log('Table Cleared');
	}
}


module.exports = { 'createNewEntry' : createNewEntry,
					'clearTable'	: clearTable }