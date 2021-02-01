const { TempSensor, randomvalue } = require('./TempSensor.js');



var sensor = 'None';

// const sensorInit = function()





// This is some js wizardry, but it will repetadly execute this function every 10 seconds
// Uses window.setInterval function

var count = 0;
setInterval(function () {

	// This code initializes each sensor on the first interval run
	if(sensor === 'None'){

		var sensor_number = Number(process.argv[2]);
		sensor = new TempSensor(sensor_number + 1);
		console.log(' Created new sensor');
		console.log(' Sensor Number:', sensor.number);

	}

	// This code is executed on every subsequent run post initialization
	else{
		count++;

		sensor.measureTemp();
		console.log(sensor.number, ' taking temp');

		
		// Write database with sensor data
		// TODO




		// Exit condition
		// Occurs at 30 executions of this periodic process
		if(count === 30){			
			process.exit();
		}

	}
}, 10000)



// Same js wizardry here, but this one is a timeout