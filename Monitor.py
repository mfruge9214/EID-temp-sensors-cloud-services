 	#########################
# File: Monitor.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		This class monitors the TempSensors. It has methods to read data from
#		the temp sensors, calculate the low/high/avg, and print/log a report.
#		
#########################


from time import sleep
import os
import json
from datetime import datetime
import pyodbc


database = 'SensorData_1'
table = 'Sensor_Data_Test'


class Monitor:

	def __init__(self):
		# dictionary that will contain all the data from all the sensors
		self.all_sensor_data = {}

		self.server = 'localhost'
		self.database = database
		self.username = 'eid'
		self.password = 'eid' # super secure
		self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
		self.cursor = self.cnxn.cursor()
		self.fahrenheit = True

		# dictionary that will contain calculations on the sensor data
		self.all_sensor_calculations = {}
		self.ErrorCount = 0
		self.WriteFilePath = 'MonitorLogs.txt'

		# Delete the log file if it already exists. This check/delete was referenced
		# from: https://www.w3schools.com/python/python_file_remove.asp
		if os.path.exists(self.WriteFilePath):
  			os.remove(self.WriteFilePath)
	

	def read_sensor_data(self):
		# clear the current stored data. We will re-read all of it to get a fresh copy
		self.all_sensor_data.clear()

		tsql = "SELECT * FROM " + table + ";"
		with self.cursor.execute(tsql):
			# help getting the data into a json object from:
			# https://stackoverflow.com/questions/16519385/output-pyodbc-cursor-results-as-python-dictionary/16523148#16523148
			columns = [column[0] for column in self.cursor.description]
			for row in self.cursor.fetchall():
				entry = dict(zip(columns, row))
				# if the sensor number isn't in the dictionary yet, add an
				# empty list to the dictionary for that sensor
				if entry['SensorNumber'] not in self.all_sensor_data:
					self.all_sensor_data[entry['SensorNumber']] = []
				self.all_sensor_data[entry['SensorNumber']].append(entry)

		#print(self.all_sensor_data)
		if not self.fahrenheit:
			for sensor_id, data in self.all_sensor_data.items():
				#for measurement in data:
				for i in range(len(data)):
					if data[i]['CurrentTemp'] != 999:
						self.all_sensor_data[sensor_id][i]['CurrentTemp'] = self.fahrenheit_to_celsius(data[i]['CurrentTemp'])


	def fahrenheit_to_celsius(self, deg_f):
		deg_c = None
		try:
			deg_c = (deg_f - 32) * 5/9
		except TypeError:
			# deg_f is None (no valid entries yet). This is ok, so we'll just pass
			pass
		return deg_c

	def celsius_to_fahrenheit(self, deg_c):
		deg_f = None
		try:
			deg_f = (deg_c * 9/5) + 32
		except TypeError:
			# deg_f is None (no valid entries yet). This is ok, so we'll just pass
			pass
		return deg_f

	def get_last_sensor_data(self, sensor_number):

		if(self.all_sensor_data): return self.all_sensor_data[sensor_number][-1]

		else: return None
		



	def print_report(self):
		# generate a report, consisting of a timestamp, then the low, high, average,
		# alarm count, and error count for each sensor
		output = ''
		now = datetime.now()
		timestamp = now.strftime("%H:%M:%S, %m/%d/%Y")
		output += '-------------------------------------------------\n'
		output += 'Monitor report, generated at ' + timestamp + '\n'
		output += '-------------------------------------------------\n'
		output += f'Current monitor error count: {self.ErrorCount}\n\n'
		
		for sensor_id, calculations in self.all_sensor_calculations.items():
			output += f'Sensor {sensor_id}:\n'
			low_f = calculations["low"]
			low_c = self.fahrenheit_to_celsius(low_f)
			output += f'\tLow: {low_f} F ({low_c} C)\n'
			high_f = calculations["high"]
			high_c = self.fahrenheit_to_celsius(high_f)
			output += f'\tHigh: {high_f} F ({high_c} C)\n'
			avg_f = calculations["avg_f"]
			avg_c = self.fahrenheit_to_celsius(avg_f)
			output += f'\tAvg: {avg_f} F ({avg_c} C)\n'
			output += f'\tAlarm count: {self.all_sensor_data[sensor_id][-1]["AlarmCount"]}\n'
			output += f'\tError count: {self.all_sensor_data[sensor_id][-1]["ErrorCount"]}\n'
			output += '\n'

		# send report to stdout
		print(output)

		# also write report to the log file
		try:
			with open(self.WriteFilePath, 'a') as f:
				f.write(output)
		except:
			print('Problem opening log file')
			self.ErrorCount += 1

	def generate_report(self):
		self.read_sensor_data()
		self.run_calculations()
		self.print_report()
