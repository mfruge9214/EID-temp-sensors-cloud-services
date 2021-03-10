/*
* File: SensorProcess.js
* Author: Mike Fruge
* Description: This file serves as the entry point for each different sensor process, forked from SensorParent 
*					This file utilizes rabbitMQ module to send data to the application gateway
*/

// const { createNewEntry, clearTable, pool } = require('./Database.js');
const { TempSensor, randomvalue, parseDateTime } = require('./TempSensor.js');
var amqp = require('amqplib/callback_api');

// Initialize sensor on first run through with passed in parameters

var sensor = 'None';
var sensor_number = Number(process.argv[2]);
sensor = new TempSensor(sensor_number);
console.log(' Created new sensor');
console.log(' Sensor Number:', sensor.number);


var serverConnectParams = {
  protocol: 'amqp',
  hostname: 'localhost'
}


var count = 0;

amqp.connect(serverConnectParams, function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var queue = 'sensor_' + sensor_number.toString() + '_DataQ';

        channel.assertQueue(queue, {
            durable: true
        });

        console.log(" Crested %s Queue", queue);


        setInterval(function () {

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
				'HumAlarm'			: sensor.HAlarmState,
				'TempAlarm'			: sensor.TAlarmState 
			}


			var msg = JSON.stringify(dataEntry);

        	channel.sendToQueue(queue, Buffer.from(msg));

			// Exit condition
			// Occurs at 33 executions of this periodic process, creating 99 measurments
			if(count === 33){			
				process.exit();
			}
			count++;

		}, 10000)
    });
});




