import sys


from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.QtCore import QTimer
from Complex_UI import Ui_MainWindow
from Monitor import Monitor
import UI_Event_Handling as UI_Helper
import numpy as np


# cmd to convert from .ui file to .py file
# python -m PyQt5.uic.pyuic -x Complex_UI.ui -o Complex_UI.py


# For now, just putting these defines here

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


		self.measurement_output_displays = {
												1: self.ui.s1_measurement_output,
												2: self.ui.s2_measurement_output,
												3: self.ui.s3_measurement_output,
												4: self.ui.s4_measurement_output,
												5: self.ui.s5_measurement_output,
												6: self.ui.s6_measurement_output
										}


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

		self.error_outputs = {

								1: self.ui.s1_error_output,
								2: self.ui.s2_error_output,
								3: self.ui.s3_error_output,
								4: self.ui.s4_error_output,
								5: self.ui.s5_error_output,
								6: self.ui.s6_error_output

		}


		for sensor_num in self.alarm_inputs.keys():

			for input_field, sb_obj in self.alarm_inputs[sensor_num].items():
				sb_obj.valueChanged.connect(self.alarm_input_handler)




		## Connect the alarm inputs to their respective functions
		# for sensor_num, input_box in self.alarm_inputs.items():
		# 	input_box.valueChanged.connect()

		## First screen output boxes
		# self.ui.s1_measurement_output
		# self.ui.s2_measurement_output
		# self.ui.s3_measurement_output
		# self.ui.s4_measurement_output
		# self.ui.s5_measurement_output
		# self.ui.s6_measurement_output

		## Alarm settings
		# self.ui.s1_T_alarm.valueChanged.connect()
		# self.ui.s1_H_alarm.valueChanged.connect()
		
		# self.ui.s2_T_alarm.valueChanged.connect()
		# self.ui.s2_H_alarm.valueChanged.connect()
		
		# self.ui.s3_T_alarm.valueChanged.connect()
		# self.ui.s3_H_alarm.valueChanged.connect()
		
		# self.ui.s4_T_alarm.valueChanged.connect()
		# self.ui.s4_H_alarm.valueChanged.connect()
		
		# self.ui.s5_T_alarm.valueChanged.connect()
		# self.ui.s5_H_alarm.valueChanged.connect()
		
		# self.ui.s6_T_alarm.valueChanged.connect()
		# self.ui.s6_H_alarm.valueChanged.connect()

		self.functionNumber = 1

		self.displayCelcius = False

		# Initialize the state of the UI
		#self.ui.screen_output.setText("INITIALIZING")

		# Initialize UI timer for updates
		self.timer = QTimer()

		# Create instance of monitor class
		self.monitor = Monitor()

		# Register functions to corresponding event
		# self.ui.pb_select.released.connect(self.select_button)
		# self.ui.pb_up.released.connect(self.up_button)
		# self.ui.pb_down.released.connect(self.down_button)
		# self.ui.pb_convertTemp.released.connect(self.convertTemp_button)
		self.timer.timeout.connect(self.periodic_update)
		self.timer.start(10000)
		x=range(0, 10)
		y=range(0, 20, 2)
		#self.ui.plotWidget.canvas.subplot(232)
		#self.ui.plotWidget.canvas.fig.add
		self.ui.plotWidget.canvas.ax[1][1].plot(x, y)
		self.ui.plotWidget.canvas.ax[0][0].set_title('Sensor 1')
		self.ui.plotWidget.canvas.ax[0][1].set_title('Sensor 2')
		self.ui.plotWidget.canvas.ax[1][0].set_title('Sensor 3')
		self.ui.plotWidget.canvas.ax[1][1].set_title('Sensor 4')
		self.ui.plotWidget.canvas.ax[2][0].set_title('Sensor 5')
		self.ui.plotWidget.canvas.ax[2][1].set_title('Sensor 6')
		self.ui.plotWidget.canvas.draw()

	def alarm_input_handler(self):

		for num in self.alarm_inputs.keys():

			for input_field, sb_obj in self.alarm_inputs[num].items():
				new_alarm_val = sb_obj.value()

				if(input_field == 'Temp'):
					UI_Helper.setSensorAlarmVal(new_alarm_val, num, 4)
				else:
					UI_Helper.setSensorAlarmVal(new_alarm_val, num, 5)



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


	def periodic_update(self):
		self.monitor.read_sensor_data()

		for sensor in self.measurement_output_displays.keys():

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

		self.update_measurements()
		#self.update_errors()
		self.update_graphs()

	def update_graphs(self):
		temps = {}
		hums = {}
		for sensor_id, sensor_data in self.monitor.all_sensor_data.items():
			if sensor_id not in temps:
				temps[sensor_id] = []
				hums[sensor_id] = []
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
			self.ui.plotWidget.canvas.ax[row][col].set_ylabel('Temperature (F)', color=temp_color)
			self.ui.plotWidget.canvas.ax[row][col].plot(timevals, tempList, color=temp_color)
			self.ui.plotWidget.canvas.ax[row][col].tick_params(axis='y', labelcolor=temp_color)
			ax_hum = self.ui.plotWidget.canvas.ax[row][col].twinx()
			ax_hum.plot(timevals, humList, color=hum_color)
			ax_hum.set_ylabel('Humidity (%)', color=hum_color)
			ax_hum.tick_params(axis='y', labelcolor=hum_color)
		self.ui.plotWidget.canvas.draw()


	def update_measurements(self):

		## Construct string

		for sensor_num, display in self.measurement_output_displays.items():
			lastMeasurement = self.monitor.get_last_sensor_data(sensor_num)

			if(lastMeasurement == None):
				display.setText(" 888 ")
				break

			temp = UI_Helper.roundFloat(lastMeasurement['CurrentTemp'])
			hum = UI_Helper.roundFloat(lastMeasurement['CurrentHumidity'])
			# Add T and H alarms in here too?

			t_alarm = UI_Helper.getSensorAlarm(sensor_num, 4)['count']
			h_alarm = UI_Helper.getSensorAlarm(sensor_num, 5)['count']


			display_string = str(temp) + " F\n" + str(hum) + "% RH\n" + "Alarms:\n" + "T: " + str(t_alarm) + " H: " + str(h_alarm)
			display.setText(display_string)



app = QApplication(sys.argv)
w = AppWindow()
w.show() 
sys.exit(app.exec_())