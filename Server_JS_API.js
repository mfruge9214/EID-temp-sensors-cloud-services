
function roundFloat(float_val) {
	// Rounding help from:
	// https://stackoverflow.com/questions/11832914/round-to-at-most-2-decimal-places-only-if-necessary
	return Math.round(float_val * 100) / 100
}

function convertTemp(temp, celsius_flag){
	if(celsius_flag && temp != 999){
		temp = (temp - 32) * 5/9
	}
	return temp
}

function formatOutput(sensor_data, celsius_flag) {

	var output = ""
	var unit_string = " F, "
	if (celsius_flag) {
		unit_string = " C, "
	}

	output = "Timestamp: " + sensor_data['Hour'] + ":" + sensor_data['Minute'] + ":" + sensor_data['Second']
	var temp_str = " " + roundFloat(convertTemp(sensor_data['CurrentTemp'], celsius_flag)) + unit_string + roundFloat(sensor_data['CurrentHumidity']) + "% RH"
	output += temp_str

	return output
}

function get_last_10(all_data) {
	var last_10 = {}
	all_data.forEach(function (item, index) {
		if (!(item['SensorNumber'] in last_10)) {
			last_10[item['SensorNumber']] = []
		}
		last_10[item['SensorNumber']].push(item)
	});
	for (var key in last_10) {
		// getting last 10 elements came from
		// https://stackoverflow.com/questions/6473858/in-a-javascript-array-how-do-i-get-the-last-5-elements-excluding-the-first-ele     
		last_10[key] = last_10[key].slice(Math.max(last_10[key].length - 10, 0))
	}
	return last_10;
}

function get_last_measurement(data, sensor_number) {
	var sensor_data = null
	data.forEach(function (item, index) {
	  if (item['SensorNumber'] === sensor_number){
		sensor_data = item
	  }
	  });
	return sensor_data
  }

module.exports = {
	'get_last_10': get_last_10,
	'formatOutput': formatOutput,
	'get_last_measurement': get_last_measurement,
}
