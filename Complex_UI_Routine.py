import sys


from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.QtCore import QTimer
from Complex_UI import Ui_MainWindow
from Monitor import Monitor
import Alarm_Handling as UI_Helper
import numpy as np


# cmd to convert from .ui file to .py file
# python -m PyQt5.uic.pyuic -x Complex_UI.ui -o Complex_UI.py

NUM_SENSORS = 6

class AppWindow(QMainWindow): 
	def __init__(self):
		super().__init__() 
		self.ui=  Ui_MainWindow()
		self.ui.setupUi(self)
		self.sensorAppInit() 
		self.periodic_update()
		self.show()

	def sensorAppInit(self):

		# Initialize variables we need
		self.currentSensor = 1


		# dictionary of QT measurement output objects
		self.measurement_output_displays = {
												1: self.ui.s1_measurement_output,
												2: self.ui.s2_measurement_output,
												3: self.ui.s3_measurement_output,
												4: self.ui.s4_measurement_output,
												5: self.ui.s5_measurement_output,
												6: self.ui.s6_measurement_output
										}

		# dictionary of QT alarm input objects
		self.alarm_inputs = {
								1: {
									'Temp': self.ui.s1_T_alarm,
									'Hum' : self.ui.s1_H_alarm
								},
								2: {
									'Temp': self.ui.s2_T_alarm,
									'Hum' : self.ui.s2_H_alarm
								},
								3: {
									'Temp': self.ui.s3_T_alarm,
									'Hum' : self.ui.s3_H_alarm
								},
								4: {
									'Temp': self.ui.s4_T_alarm,
									'Hum' : self.ui.s4_H_alarm
								},
								5: {
									'Temp': self.ui.s5_T_alarm,
									'Hum' : self.ui.s5_H_alarm
								},
								6: {
									'Temp': self.ui.s6_T_alarm,
									'Hum' : self.ui.s6_H_alarm
								}
						}

		# dictionary of QT alarm output objects
		self.alarm_count_outputs = {
								1: {
									'Temp': self.ui.s1_Talarm_cnt_out,
									'Hum' : self.ui.s1_Halarm_cnt_out
								},
								2: {
									'Temp': self.ui.s2_Talarm_cnt_out,
									'Hum' : self.ui.s2_Halarm_cnt_out
								},
								3: {
									'Temp': self.ui.s3_Talarm_cnt_out,
									'Hum' : self.ui.s3_Halarm_cnt_out
								},
								4: {
									'Temp': self.ui.s4_Talarm_cnt_out,
									'Hum' : self.ui.s4_Halarm_cnt_out
								},
								5: {
									'Temp': self.ui.s5_Talarm_cnt_out,
									'Hum' : self.ui.s5_Halarm_cnt_out
								},
								6: {
									'Temp': self.ui.s6_Talarm_cnt_out,
									'Hum' : self.ui.s6_Halarm_cnt_out
								}
						}

		# dictionary of QT error output objects
		self.error_outputs = {

								1: self.ui.s1_error_output,
								2: self.ui.s2_error_output,
								3: self.ui.s3_error_output,
								4: self.ui.s4_error_output,
								5: self.ui.s5_error_output,
								6: self.ui.s6_error_output

		}

		# connect the F/C slider to the event handler function
		self.ui.slider_F_C.sliderReleased.connect(self.disp_format_slider_moved)

		# Connect alarm input boxes to event handler
		for sensor_num in self.alarm_inputs.keys():

			for input_field, sb_obj in self.alarm_inputs[sensor_num].items():
				sb_obj.valueChanged.connect(self.alarm_input_handler)

		# Boolean to prevent the UI from updating the alarms when we are updating them here
		self.editing_alarms = False

		self.ui.tabWidget.setCurrentIndex(0)

		# Initialize UI timer for updates
		self.timer = QTimer()

		# Create instance of monitor class
		self.monitor = Monitor()

		# Register functions to corresponding event
		self.timer.timeout.connect(self.periodic_update)
		self.timer.start(10000)
		self.updateOutput()

	def alarm_input_handler(self):

		if( not self.editing_alarms): # check that we're not manually editing the alarms
			# for all the alarms, update the local copy of the alarms with
			# the new values in the UI
			for num in self.alarm_inputs.keys():

				for input_field, sb_obj in self.alarm_inputs[num].items():
					new_alarm_val = sb_obj.value()

					if(input_field == 'Temp'):
						UI_Helper.setSensorAlarmVal(new_alarm_val, num, 4)
					else:
						UI_Helper.setSensorAlarmVal(new_alarm_val, num, 5)


	# event handler for when the F/C slider is moved
	def disp_format_slider_moved(self):

		lastState = self.monitor.fahrenheit

		if(self.ui.slider_F_C.value() == 0): # if we want Fahrenheit

			self.monitor.fahrenheit = True
			if(lastState != self.monitor.fahrenheit):
				UI_Helper.convertAlarmVals(self.monitor.fahrenheit)

		else: # if we want Celcius
			self.monitor.fahrenheit = False
			if(lastState != self.monitor.fahrenheit):
				UI_Helper.convertAlarmVals(self.monitor.fahrenheit)

		# Update all of the data to use the new units and update the display
		self.monitor.read_sensor_data()
		self.updateOutput()


	# this function gets called every 10 seconds to read new data and update the UI
	def periodic_update(self):
		self.monitor.read_sensor_data()

		for sensor in self.measurement_output_displays.keys(): # for all sensors

			# Get the last measurement and set alarms as needed
			lastMeasurement = self.monitor.get_last_sensor_data(sensor)
			if(lastMeasurement == None):
				return

			TAlarm = UI_Helper.getSensorAlarm(sensor, 4)['val']
			HAlarm = UI_Helper.getSensorAlarm(sensor, 5)['val']

			if(lastMeasurement['CurrentTemp'] > TAlarm and lastMeasurement['CurrentTemp'] != 999):
				UI_Helper.incSensorAlarmCount(sensor, 4)

			if(lastMeasurement['CurrentHumidity'] > HAlarm and lastMeasurement['CurrentHumidity'] != 999):
				UI_Helper.incSensorAlarmCount(sensor, 5)

		# update the output
		self.updateOutput()

	def updateOutput(self):
		self.update_measurements()
		self.update_alarm_displays()
		self.update_errors()
		self.update_graphs()

	def update_graphs(self):
		temps = {}
		hums = {}

		if(self.monitor.all_sensor_data == {}):
			# if there isn't any sensor data yet, just return
			return

		# for all sensors
		for sensor_id, sensor_data in self.monitor.all_sensor_data.items():
			# add the sensor to temps and hums if it's not there already
			if sensor_id not in temps:
				temps[sensor_id] = []
				hums[sensor_id] = []

			# Go through all the data and add the temps and humidities to an
			# list that will be used for graphing, ignoring measurements that
			# are 999.0
			for entry in sensor_data:
				temp = entry['CurrentTemp']
				humidity = entry['CurrentHumidity']
				if temp == 999.0:
					temp = np.nan
				if humidity == 999.0:
					humidity = np.nan
				temps[sensor_id].append(temp)
				hums[sensor_id].append(humidity)

		numEntries = len(temps[1])

		timevals = np.arange(0, 10*numEntries, 10)

		self.ui.plotWidget.canvas.fig.clear()
		self.ui.plotWidget.canvas.ax = self.ui.plotWidget.canvas.fig.subplots(3, 2)

		# Plot all the sensor data!
		for sensor_id in self.monitor.all_sensor_data.keys():
			tempList = temps[sensor_id]
			humList = hums[sensor_id]
			title = 'Sensor ' + str(sensor_id)
			row = int((sensor_id-1) / 2)
			col = (sensor_id-1) % 2

			# plotting help from:
			# https://matplotlib.org/3.2.1/gallery/subplots_axes_and_figures/two_scales.html
			temp_color = 'tab:blue'
			hum_color = 'tab:orange'
			self.ui.plotWidget.canvas.ax[row][col].set_title(title)
			self.ui.plotWidget.canvas.ax[row][col].set_xlabel('time (s)')
			units = '(F)'
			if not self.monitor.fahrenheit:
				units = '(C)'
			self.ui.plotWidget.canvas.ax[row][col].set_ylabel('Temperature ' + units, color=temp_color)
			self.ui.plotWidget.canvas.ax[row][col].plot(timevals, tempList, color=temp_color)
			self.ui.plotWidget.canvas.ax[row][col].tick_params(axis='y', labelcolor=temp_color)

			# get a copy of the axis so we can plot both temperature and humidity
			# on the same graph
			ax_hum = self.ui.plotWidget.canvas.ax[row][col].twinx()
			ax_hum.plot(timevals, humList, color=hum_color)
			ax_hum.set_ylabel('Humidity (%)', color=hum_color)
			ax_hum.tick_params(axis='y', labelcolor=hum_color)
		
		# Finally, draw everything
		self.ui.plotWidget.canvas.draw()


	def update_measurements(self):
		# For each sensor, get the last measurement.
		# Try to round it and display it, but if there was an exception,
		# that means there isn't any valid data yet
		for sensor_num, display in self.measurement_output_displays.items():

			try:
				lastMeasurement = self.monitor.get_last_sensor_data(sensor_num)
				temp = UI_Helper.roundFloat(lastMeasurement['CurrentTemp'])
				hum = UI_Helper.roundFloat(lastMeasurement['CurrentHumidity'])

				if self.monitor.fahrenheit:
					display_string = str(temp) + " F\n" + str(hum) + "% RH\n"
				else:
					display_string = str(temp) + " C\n" + str(hum) + "% RH\n"

			except:
				display_string = '888'
				print("No Valid Data Yet")

			
			display.setText(display_string)



	def update_errors(self):
		# For each sensor, get the last error count, then display it. If there
		# isn't a last measurement, that means there isn't any valid data yet
		for sensor_num, display in self.error_outputs.items():
			try:
				lastMeasurement = self.monitor.get_last_sensor_data(sensor_num)
				num_errors = lastMeasurement['ErrorCount']
				if(num_errors == 1):
					display_string = str(num_errors) + " Error"
				else:
					display_string = str(num_errors) + " Errors"

			except:
				display_string = '888'
				print("No Valid Dat Yet")


			display.setText(display_string)


	def update_alarm_displays(self):

		self.editing_alarms = True # set to true to prevent the UI from updating anything

		# For each sensor, get the latest alarm counts (for both temp and humidity)
		# and display them
		for sensor_num in self.alarm_count_outputs.keys():

			for alarm_field, display in self.alarm_count_outputs[sensor_num].items():

				if(alarm_field == "Temp"):
					alarm = UI_Helper.getSensorAlarm(sensor_num, 4)['count']
					display.setText(str(alarm))
				else:
					alarm = UI_Helper.getSensorAlarm(sensor_num, 5)['count']
					display.setText(str(alarm))

		# For each sensor, get the latest alarm thresholds (for both temp and humidity)
		# and display them
		for sensor_num in self.alarm_inputs.keys():

			for alarm_field, display in self.alarm_inputs[sensor_num].items():

				if(alarm_field == "Temp"):
					alarm = UI_Helper.getSensorAlarm(sensor_num, 4)['val']
					display.setValue(int(alarm))
				else:
					alarm = UI_Helper.getSensorAlarm(sensor_num, 5)['val']
					display.setValue(int(alarm))

		self.editing_alarms = False # allow the UI to update things again

# run the UI
def UI_Run():
	app = QApplication(sys.argv)
	w = AppWindow()
	w.show() 
	sys.exit(app.exec_())
