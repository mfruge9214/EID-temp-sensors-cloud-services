/*
* File: TempSensorApplication.js
* Author: Mike Fruge & Bryan Cisneros
* Description: This file is the master sensor process, which will spawn the child processes and run through each sensor process
*/

const { fork } = require('child_process');

const { clearTable, poolConnect } = require('./Database.js')




//Obtain User Input for number of sensors
var userIn= process.argv.slice(2);
var numSensors = Number(userIn);


// Thread Forking and creation
var sensor_proc_list = [];
for(var i = 0; i<numSensors; i++){

	if(i === 0){
		var new_proc = fork('SensorProcess.js', [String(i), true]);
	}
	else{
		var new_proc = fork('SensorProcess.js', [String(i), false]);
	}
	
	sensor_proc_list[i] = new_proc;

}



// console.log('Cleared Table and Created Sensors');




function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}




