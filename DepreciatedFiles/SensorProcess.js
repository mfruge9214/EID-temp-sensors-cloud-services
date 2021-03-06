/*
* File: SensorProcess.js
* Author: Mike Fruge
* Description: This file serves as the entry point for each different sensor process, forked from SensorParent 
*				As describe in Project 2 outline, sensor takes random measurment every 10 seconds for 5 minutes,
*					and writes result to the database
*/

const { createNewEntry, clearTable, pool } = require('./Database.js');
const { TempSensor, randomvalue, parseDateTime } = require('./TempSensor.js');


// Initialize sensor on first run through with passed in parameters

var sensor_master = process.argv[3];
var sensor = 'None';
var sensor_number = Number(process.argv[2]);
sensor = new TempSensor(sensor_number + 1);
console.log(' Created new sensor');
console.log(' Sensor Number:', sensor.number);

// Uses window.setInterval function, will repetadly execute this function every 10 seconds



var count = -1;

setInterval(function () {

	if (count === -1){
		clearTable();
		count++;
		return
	}



	sensor.measureEnvironment();
	console.log(sensor.number, ' taking measurment');

	var parsedDate = parseDateTime(sensor.timestamp);

	console.log(parsedDate);



	// Create structure for sending data to DB
	// Keys must match with database columns
	var dataEntry = {
		'SensorNumber' 		: sensor.number,
		'CurrentTemp'		: sensor.lastMeasurement['Temp'],
		'CurrentHumidity'	: sensor.lastMeasurement['Humidity'],
		'Hour'				: parsedDate['Hour'],
		'Minute'			: parsedDate['Minute'],
		'Second'			: parsedDate['Seconds'],
		'ErrorCount'		: sensor.errorCnt,
	}

	createNewEntry(dataEntry);

	// Exit condition
	// Occurs at 31 executions of this periodic process
	if(count === 30){			
		process.exit();
	}

	// This code is executed in intervals set by the second argument in ms
	count++;

}, 10000)