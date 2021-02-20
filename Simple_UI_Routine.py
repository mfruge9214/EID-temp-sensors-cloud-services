 	#########################
# File: Simple_UI_Routine.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		Main window and functionality for Simple UI
#		Main Simple UI Design file
#				Utilizes montor API to retrieve data, Alarm Handling to process incoming data, and PyQT for interface and widgets
#		
#########################



import sys


from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.QtCore import QTimer
from Simple_UI import Ui_MainWindow
from Monitor import Monitor
import Alarm_Handling as UI_Helper


# cmd to convert from .ui file to .py file
# python -m PyQt5.uic.pyuic -x Simple_UI.ui -o Simple_UI.py


NUM_SENSORS = 6

class AppWindow(QMainWindow): 
	def __init__(self):
		super().__init__() 
		self.ui=  Ui_MainWindow()
		self.ui.setupUi(self)
		self.sensorAppInit() 
		self.read_data()
		self.show()

	def sensorAppInit(self):

		# Initialize variables we need
		self.currentSensor = 1



		self.function_indicator = {
									1: self.ui.led_sensor,
									2: self.ui.led_temp,
									3: self.ui.led_hum,
									4: self.ui.led_t_alarm,
									5: self.ui.led_h_alarm
		}

		self.functionNumber = 1

		self.displayCelcius = False

		# Initialize the state of the UI
		self.ui.screen_output.setText("INITIALIZING")

		# Initialize UI timer for updates
		self.timer = QTimer()

		# Create instance of monitor class
		self.monitor = Monitor()

		# Register functions to corresponding event
		self.ui.pb_select.released.connect(self.select_button)
		self.ui.pb_up.released.connect(self.up_button)
		self.ui.pb_down.released.connect(self.down_button)
		self.ui.pb_convertTemp.released.connect(self.convertTemp_button)
		self.timer.timeout.connect(self.read_data)
		self.timer.start(10000)


	def select_button(self):

		# Uncheck current button
		for num in range(1, 6):
			self.function_indicator[self.functionNumber].setChecked(False)

		# Wrap around or not
		if(self.functionNumber < 5):
			self.functionNumber += 1
		else:
			self.functionNumber = 1

		# Check next box
		self.function_indicator[self.functionNumber].setChecked(True)

		self.updateOutput()

		
		
	# Up button released event
	def up_button(self):

		function = UI_Helper.UI_FUNCTIONS[self.functionNumber]

		if(function == 'SensorNumber'):
			if self.currentSensor < NUM_SENSORS:
				self.currentSensor += 1

		elif(function == 'TempAlarmCount' or function == 'HumAlarmCount'):

			alarm = UI_Helper.getSensorAlarm(self.currentSensor, self.functionNumber)['val']
			alarm += 1
			UI_Helper.setSensorAlarmVal(alarm, self.currentSensor, self.functionNumber)

		self.updateOutput()

	# Down Button released event
	def down_button(self):

		function = UI_Helper.UI_FUNCTIONS[self.functionNumber]

		if(function == 'SensorNumber'):
			if self.currentSensor > 1:
				self.currentSensor -= 1

		elif(function == 'TempAlarmCount' or function == 'HumAlarmCount'):

			alarm = UI_Helper.getSensorAlarm(self.currentSensor, self.functionNumber)['val']
			alarm -= 1
			UI_Helper.setSensorAlarmVal(alarm, self.currentSensor, self.functionNumber)

		self.updateOutput()


	def convertTemp_button(self):
		self.displayCelcius = ~(self.displayCelcius)
		self.updateOutput()


	def read_data(self):
		self.monitor.read_sensor_data()

		# for each sensor, get the last measurement and update the alarm count as needed
		for sensor in range(1, NUM_SENSORS+1):
			lastMeasurement = self.monitor.get_last_sensor_data(sensor)
			if(lastMeasurement == None):
				return

			TAlarm = UI_Helper.getSensorAlarm(sensor, 4)['val']
			HAlarm = UI_Helper.getSensorAlarm(sensor, 5)['val']

			if(lastMeasurement['CurrentTemp'] > TAlarm and lastMeasurement['CurrentTemp'] != 999):
				UI_Helper.incSensorAlarmCount(sensor, 4)

			if(lastMeasurement['CurrentHumidity'] > HAlarm and lastMeasurement['CurrentHumidity'] != 999):
				UI_Helper.incSensorAlarmCount(sensor, 5)

		self.updateOutput()

	def updateOutput(self):
		# get the last measurement
		lastMeasurement = self.monitor.get_last_sensor_data(self.currentSensor)

		## Ensure there is valid data to display
		if(lastMeasurement == None):
			self.ui.screen_output.setText(" INITIALIZING ")
			return

		neededData = lastMeasurement[UI_Helper.UI_FUNCTIONS[self.functionNumber]]

		errorCount = lastMeasurement['ErrorCount']

		# Construct standard part of display
		displayString = "S0" + str(self.currentSensor) + ":"

		# Format the data correctly
		dataString = " "

		function = UI_Helper.UI_FUNCTIONS[self.functionNumber]
		## Display Temperature
		if(function == 'CurrentTemp'):

			if(self.displayCelcius):
				dataString = str(self.monitor.fahrenheit_to_celsius(neededData)) + " Deg C "
			else:
				dataString = str(UI_Helper.roundFloat(neededData)) + " Deg F "

		elif(function == 'CurrentHumidity'):

			dataString = str(UI_Helper.roundFloat(neededData)) + " % RH  "

		elif(function == 'TempAlarmCount'):

			alarm = UI_Helper.getSensorAlarm(self.currentSensor, self.functionNumber)

			if(self.displayCelcius):
				dataString = "Thresh:" + str(UI_Helper.roundFloat(self.monitor.fahrenheit_to_celsius(alarm['val']))) + " Deg C, Count:" + str(alarm['count'])
			else:
				dataString = "Thresh:" + str(UI_Helper.roundFloat(alarm['val'])) + " Deg F, Count:" + str(alarm['count'])

		elif(function == 'HumAlarmCount'):

			alarm = UI_Helper.getSensorAlarm(self.currentSensor, self.functionNumber)

			dataString = "Thresh:" + str(UI_Helper.roundFloat(alarm['val'])) + "% RH, Count:" + str(alarm['count'])


		displayString += dataString

		displayString += " Errors: " + str(errorCount)

		self.ui.screen_output.setText(displayString)

# run the UI
def UI_Run():
	app = QApplication(sys.argv)
	w = AppWindow()
	w.show() 
	sys.exit(app.exec_())
