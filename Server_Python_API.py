from Monitor import Monitor
import math



monitor = Monitor()


def roundFloat(float_val):

	num = float_val * 100
	num = math.floor(num)
	num = num / 100
	return num

def formatOutput(sensor_data):

	output = ""

	if(monitor.fahrenheit):
		unit_string = " F , "
	else:
		unit_string = " C , "

	try:
		output = "Timestamp: " + str(sensor_data['Hour']) + ":" + str(sensor_data['Minute']) + ":" + str(sensor_data['Second'])

		temp_str = " " + str(roundFloat(sensor_data['CurrentTemp'])) + unit_string + str(roundFloat(sensor_data['CurrentHumidity'])) + "% RH"

		output += temp_str

	except:
		print("--")

	return output


def ParseMessage(msg_obj):

	command = msg_obj['command']


	output = ""
	# Deal with changes in settings before everything else in case they effect monitor
	if(command == 'S'):

		setting = msg_obj['trigger_id'][2:]

		if(setting == "convertTemp"):
			monitor.fahrenheit = not monitor.fahrenheit

			if(monitor.fahrenheit):
				output = "Fahrenheit"
			else:
				output = "Celsius"

	


	
	monitor.read_sensor_data()

	if(command == 'I'):

		try:
			sensor_number = msg_obj['trigger_id'][-3]
			sensor_data = monitor.get_last_sensor_data(int(sensor_number))

			output = formatOutput(sensor_data)

		except:
			
			print("Nothing")

	elif(command == 'C'):

		# This is where we will get the last 10 measurments for each sensor

		data_list = {}
		
		for sensor_number in monitor.all_sensor_data.keys():
			data_list[sensor_number] = []
			j = -1
			for i in range(10):
				data_list[sensor_number].append( formatOutput(monitor.get_specific_sensor_data_records(sensor_number, j)) )
				j -= 1


			
		output = data_list


	elif(command == 'G'):
		
		print("Nothing Yet")


	return output





