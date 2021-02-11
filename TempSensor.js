
/*
* File: TempSensors.js
* Author: Mike Fruge & Bryan Cisneros
* Description: This File Implements the TempSensor object (class) and associated helper functions
*				Used for generating data in EID Project 2
*/


// Declare Max and min target temps
 var minTarget = 35;
 var maxTarget = 45;

// Utilized code from here: 
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random

// function: genRandomFromRange
// args: range
//			Specifies the range of number generation centered on nominal
//		 nominal
//		 	central value of output range
//		 discrete
// 			true:
// 				output = nominal + range or nominal - range
// 			false:
// 				output is any float to 2 decimals in the range

function genRandomFromRange(range, nominal, discrete) {

	let sign = Math.random();
	// Do this to round off 0's
	var difference = Math.floor((Math.random() * range) * 100);
	difference = difference/100;

	if(sign <.5){

		if(discrete){
			return nominal - range;
		}

		else {
			return nominal - difference;
		}
	}

	else{
		if(discrete){
			return nominal + range;
		}
		
		else {
			return nominal + difference;
		}
	}

}


// function: getCurrentDateTime
// returns date object expressing current date and time

function getCurrentDateTime() {

	return new Date();

}


// function: parseDateTime
// returns object with hours, munite, seconds field split up

function parseDateTime(date) {
	var parsed_date = {
		'Hour' : date.getHours(),
		'Minute' : date.getMinutes(),
		'Seconds' : date.getSeconds()
	}
	return parsed_date
}


// class: Temp Sensor
// Implements object used to generate temprature data based on Assignment description

class TempSensor
{
	constructor(number){
		this.number = number;
		this.targetT = genRandomFromRange(5, 40, true);
		this.targetH = genRandomFromRange(5, 40, true);
		this.timestamp = getCurrentDateTime();
		this.TalarmCnt = 0;
		this.HalarmCnt = 0;
		this.errorCnt = 0;
		this.lastMeasurement =  {   'Temp': 0,
									'Humidity': 0
								};
		this.measureCnt = 0;
		this.measureEnvironment();
		console.log(this.lastMeasurement);
	}


	measureEnvironment() {
		////////////////////////////////////////
		// Temp calculations
		////////////////////////////////////////

		// Normal sensor variation around target
		var normalVariation = genRandomFromRange(2, 0, false);

		// Check random range of numbers for spike
		var spikeChance = Math.random();
		var spike = 0;
		if(spikeChance >.1 && spikeChance < .2){

			// Generate spike
			spike = genRandomFromRange(4.5, 3.5, false)

		}
		var thisTemp = this.targetT + normalVariation + spike;

		////////////////////////////////////////////////
		// Humidity calculations
		////////////////////////////////////////////////
		normalVariation = genRandomFromRange(2, 0, false);

		// Check random range of numbers for spike
		spikeChance = Math.random();
		spike = 0;
		if(spikeChance >.1 && spikeChance < .2){
			// Generate spike
			spike = genRandomFromRange(10, 0, false)

		}

		var thisH = this.targetH + normalVariation + spike;

		////////////////////////////////////////////
		// Sensor availability and error calculation
		////////////////////////////////////////////
		var errorChance = Math.random();

		if(errorChance > .4 && errorChance < .5){
			thisTemp = 999;
			thisH = 999;
			this.errorCnt++;
		}

		////////////////////////////////////////////
		// Alarm incrementing check
		////////////////////////////////////////////

		var h_threshold = 5;
		var t_threshold = 5;

		if((thisH > this.targetH + h_threshold)){

			// Check either value to ensure valid reading
			if(thisH != 999){
				this.HalarmCnt++;
			}
		}

		if((thisTemp > this.targetT + t_threshold)){

			// Check either value to ensure valid reading
			if(thisTemp != 999){
				this.TalarmCnt++;
			}
		}

		this.measureCnt++;

		// Compute this timestamp
		this.timestamp = getCurrentDateTime();
		
		this.lastMeasurement['Temp'] = thisTemp;
		this.lastMeasurement['Humidity'] = thisH;
	}

}

// This allows us to initialize the sensor outside of the file
module.exports = { TempSensor, genRandomFromRange, parseDateTime }
