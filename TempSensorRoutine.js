

const { TempSensor, randomvalue } = require('./TempSensor.js');
const { fork } = require('child_process');



//Obtain User Input for number of sensors
var userIn= process.argv.slice(2);
var numSensors = Number(userIn);

// // Sensor creation
// let s1 = new TempSensor(1);
// let s2 = new TempSensor(2);

// console.log('s1:', s1);
// console.log('s2:', s2);




// Thread Forking and creation

var sensor_proc_list = [];

for(var i = 0; i<numSensors; i++){

	var new_proc = fork('SensorProcess.js', [String(i)]);

}

console.log('Created Sensors');


// for(var i = 0; i<10; i++){
// 	console.log("Taking Temps")
// 	console.log(s1.measureTemp());
// 	console.log(s2.measureTemp());
// 	console.log(s1);
// 	console.log(s2);
// }
