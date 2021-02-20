 	#########################
# File: Alarm_Handling.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		File helps implement user side alarm tracking, as well as other helper functions
#		used by both UI designs, but are not monitor concerned
#		
#########################

from Monitor import Monitor
import math

# Define any needed LUT-like objects for the UI
# Create Monitor Class
Monitor = Monitor()


# Simple UI display Functions
UI_FUNCTIONS  = {
					1: 'SensorNumber',
					2: 'CurrentTemp',
					3: 'CurrentHumidity',
					4: 'TempAlarmCount',
					5: 'HumAlarmCount'
}



# Alarm Value dictionaries that both UI's use
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



# Set sensor alarm value
# setVal: Desired alarm value
# sensor_number: Sensor number
# function_number: index of corresponding entry in UI_FUNCTIONS
def setSensorAlarmVal(setVal, sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		SensorTAlarms[sensor_number]['val'] = setVal

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		SensorHAlarms[sensor_number]['val'] = setVal


# Increment sensor alarm count
# sensor_number: Sensor number
# function_number: index of corresponding entry in UI_FUNCTIONS
def incSensorAlarmCount(sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		SensorTAlarms[sensor_number]['count'] = SensorTAlarms[sensor_number]['count'] + 1

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		SensorHAlarms[sensor_number]['count'] = SensorHAlarms[sensor_number]['count'] + 1


# Get sensor alarm dict, {count, value}
# sensor_number: Sensor number
# function_number: index of corresponding entry in UI_FUNCTIONS
def getSensorAlarm(sensor_number, function_number):

	if(UI_FUNCTIONS[function_number] == "TempAlarmCount"):
		return SensorTAlarms[sensor_number]

	elif(UI_FUNCTIONS[function_number] == "HumAlarmCount"):
		return SensorHAlarms[sensor_number]

# Round floating point value to 2 decimal places

def roundFloat(float_val):

	num = float_val * 100
	num = math.floor(num)
	num = num / 100
	return num

# Used to convert the values in T alarm dict from F to C to allow monitoring
def convertAlarmVals(F_flag):

	for sensor_num, entry in SensorTAlarms.items():
		if(not F_flag):
			SensorTAlarms[sensor_num]['val'] = math.floor(Monitor.fahrenheit_to_celsius(SensorTAlarms[sensor_num]['val']))
		else:
			SensorTAlarms[sensor_num]['val'] = math.floor(Monitor.celsius_to_fahrenheit(SensorTAlarms[sensor_num]['val']))

	return SensorTAlarms




