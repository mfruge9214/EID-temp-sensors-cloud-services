/*
* File: TempSensorApplication.js
* Author: Mike Fruge & Bryan Cisneros
* Description: This file is the master sensor process, which will spawn the child processes and run through each sensor process
*/

const { fork } = require('child_process');



//Obtain User Input for number of sensors
var userIn= process.argv.slice(2);
var numSensors = Number(userIn);


// Thread Forking and creation
var sensor_proc_list = [];
for(var i = 1; i < numSensors + 1 ; i++){

	var new_proc = fork('SensorProcess_MQ.js', [String(i)]);
	sensor_proc_list[i] = new_proc;

}



// console.log('Cleared Table and Created Sensors');




function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}




