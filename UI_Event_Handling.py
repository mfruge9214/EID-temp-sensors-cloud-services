
from Monitor import Monitor
import math

# Define any needed LUT-like objects for the UI
# Create Monitor Class
Monitor = Monitor()

UI_FUNCTIONS  = {
					1: 'SensorNumber',
					2: 'CurrentTemp',
					3: 'CurrentHumidity',
					4: 'TempAlarmCount',
					5: 'HumAlarmCount'
}




SensorTAlarms = {
					1: {'val': 50, 'count': 0},
					2: {'val': 50, 'count': 0},
					3: {'val': 50, 'count': 0},
					4: {'val': 50, 'count': 0},
					5: {'val': 50, 'count': 0},
					6: {'val': 50, 'count': 0}
}

SensorHAlarms = {
					1: {'val': 50, 'count': 0},
					2: {'val': 50, 'count': 0},
					3: {'val': 50, 'count': 0},
					4: {'val': 50, 'count': 0},
					5: {'val': 50, 'count': 0},
					6: {'val': 50, 'count': 0}
}




def setSensorAlarmVal(setVal, sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		SensorTAlarms[sensor_number]['val'] = setVal

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		SensorHAlarms[sensor_number]['val'] = setVal



def incSensorAlarmCount(sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		SensorTAlarms[sensor_number]['count'] = SensorTAlarms[sensor_number]['count'] + 1

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		SensorHAlarms[sensor_number]['count'] = SensorHAlarms[sensor_number]['count'] + 1



def getSensorAlarm(sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		return SensorTAlarms[sensor_number]

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		return SensorHAlarms[sensor_number]




def fetchRequestedField(function_number):

	fields = UI_FUNCTIONS

	return fields[function_number]


def roundFloat(float_val):

	num = float_val * 100
	num = math.floor(num)
	num = num / 100
	return num


def convertAlarmVals(F_flag):

	for sensor_num, entry in SensorTAlarms.items():
		if(not F_flag):
			SensorTAlarms[sensor_num]['val'] = math.floor(Monitor.fahrenheit_to_celsius(SensorTAlarms[sensor_num]['val']))
		else:
			SensorTAlarms[sensor_num]['val'] = math.floor(Monitor.celsius_to_fahrenheit(SensorTAlarms[sensor_num]['val']))

	return SensorTAlarms




