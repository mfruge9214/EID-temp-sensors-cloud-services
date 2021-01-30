

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

function getCurrentDateTime() {

	return new Date().toLocaleString();

}

class TempSensor
{
	constructor(number){
		this.number = number;
		this.target = genRandomFromRange(5, 40, true);
		this.timestamp = getCurrentDateTime();
		this.alarmCnt = 0;
		this.errorCnt = 0;
		this.lastTemp = 0;
		this.measureTemp();
	}


	measureTemp() {

		// Normal sensor variation around target
		var normalVariation = genRandomFromRange(2, 0, false);

		// Check random range of numbers for spike
		var spikeChance = Math.random();
		var spike = 0;
		if(spikeChance >.1 && spikeChance < .2){

			// Generate spike
			spike = genRandomFromRange(4.5, 3.5, false)

		}
		var thisTemp = this.target + normalVariation + spike;

		// Random range for error
		var errorChance = Math.random();
		if(errorChance > .4 && errorChance < .5){
			thisTemp = 999;
			this.errorCnt++;
		}


		// Increment alarm counter if there is valid temp and outside range
		if(thisTemp > this.target + 5 || thisTemp < this.target - 5){
			if(thisTemp != 999){
				this.alarmCnt++;
			}
		}


		this.lastTemp = thisTemp;
		
		return thisTemp;
	}

}

// This allows us to initialize the sensor outside of the file
module.exports = { TempSensor, genRandomFromRange}
