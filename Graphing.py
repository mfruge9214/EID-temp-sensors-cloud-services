#########################
# File: Graphing.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		Reads database table and creates plots of each sensor data
#		
#########################

import matplotlib.pyplot as plt
import numpy as np
# from Monitor import Monitor
# from time import sleep

# monitor = Monitor()


# while True:
# 	monitor.generate_report()
# 	sleep(30)


def plotSensorData(numSensors, data):

	numEntries = len(data[1])

	timevals = np.arange(0, 10*numEntries, 10);
	print(timevals)
	plt.figure()

	# Average Temps
	plt.subplot(231)

	for num in range(numSensors):
		sensorNum = num + 1
		tempList = data[sensorNum]
		plt.plot(timevals, tempList)


	# High Temps
	plt.subplot(232)
	for num in range(numSensors):
		sensorNum = num + 1
		tempList = data[sensorNum]
		plt.plot(timevals, tempList)


	# Low Temps
	plt.subplot(233)
	for num in range(numSensors):
		sensorNum = num + 1
		tempList = data[sensorNum]
		plt.plot(timevals, tempList)


	# Alarms
	plt.subplot(234)
	for num in range(numSensors):
		sensorNum = num + 1
		tempList = data[sensorNum]
		plt.bar(timevals, tempList)

	# Errors
	plt.subplot(235)
	for num in range(numSensors):
		sensorNum = num + 1
		tempList = data[sensorNum]
		plt.bar(timevals, tempList)


	plt.show()



data = {
	1 : [{'Id': 1, 'CurrentTemp': 72.3, 'AlarmCount' : 1}, {'Id': 4, 'CurrentTemp': 79.0, 'AlarmCount' : 1}],
	2 : [{'Id': 2, 'CurrentTemp': 20.0, 'AlarmCount' : 1}, {'Id': 5, 'CurrentTemp': 20.0, 'AlarmCount' : 1}],
	3 : [{'Id': 3, 'CurrentTemp': 50.0, 'AlarmCount' : 1}, {'Id': 6, 'CurrentTemp': 20.0, 'AlarmCount' : 1}],

}


avg_temps = { 1 : [],
			  2 : [],
			  3 : [] }


for sensor_number in range(3):
	for measurment in data[sensor_number + 1]:
		avg_temps[sensor_number+1].append((measurment['CurrentTemp']))


print(avg_temps)


plotSensorData(3, avg_temps)




