import sys

from PyQt5.QtWidgets import QMainWindow, QApplication 
from Simple_UI import Ui_MainWindow


# cmd to convert from .ui file to .py file
# python -m PyQt5.uic.pyuic -x Simple_UI.ui -o Simple_UI.py


# For now, just putting these defines here

NUM_SENSORS = 6

class AppWindow(QMainWindow): 
	def __init__(self):
		super().__init__() 
		self.ui=  Ui_MainWindow()
		self.ui.setupUi(self)
		self.sensorAppInit() 
		self.show()



	def sensorAppInit(self):

		# Initialize variables we need
		self.currentSensor = 1
		self.functions  = {
							1: 'Sensor',
							2: 'Temperature',
							3: 'Humidity',
							4: 'Temp Alarm',
							5: 'Hum Alarm'
		}

		self.function_indicator = {
									1: self.ui.led_sensor,
									2: self.ui.led_temp,
									3: self.ui.led_hum,
									4: self.ui.led_t_alarm,
									5: self.ui.led_h_alarm
		}

		self.functionNumber = 1;

		# Initialize the state of the UI
		self.ui.screen_output.setText(str(self.currentSensor))

		# Register functions to corresponding event
		self.ui.pb_select.released.connect(self.select_button)
		self.ui.pb_up.released.connect(self.up_button)
		self.ui.pb_down.released.connect(self.down_button)


	def select_button(self):

		# Uncheck current button
		self.function_indicator[self.functionNumber].setChecked(False)

		# Wrap around or not
		if(self.functionNumber < 5):
			self.functionNumber += 1
		else:
			self.functionNumber = 1

		# Check next box
		self.function_indicator[self.functionNumber].setChecked(True)

		
		
	# Up button released event
	def up_button(self):
		if self.currentSensor < NUM_SENSORS:
			self.currentSensor += 1

		self.ui.screen_output.setText(str(self.currentSensor))

	# Down Button released event
	def down_button(self):
		if self.currentSensor > 1:
			self.currentSensor -= 1

		self.ui.screen_output.setText(str(self.currentSensor))

app = QApplication(sys.argv)
w = AppWindow()
w.show() 
sys.exit(app.exec_())