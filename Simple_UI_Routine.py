import sys

from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.QtCore import QTimer
from Simple_UI import Ui_MainWindow
from Monitor import Monitor

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
					1: 'SensorNumber',
					2: 'CurrentTemp',
					3: 'CurrentHumidity',
					4: 'TempAlarmCount',
					5: 'HumAlarmCount'
		}


		self.function_indicator = {
									1: self.ui.led_sensor,
									2: self.ui.led_temp,
									3: self.ui.led_hum,
									4: self.ui.led_t_alarm,
									5: self.ui.led_h_alarm
		}

		self.functionNumber = 1;

		self.displayCelcius = False

		# Initialize the state of the UI
		self.ui.screen_output.setText(str("0000000"))

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
		self.timer.start(1000)


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
		if self.currentSensor < NUM_SENSORS:
			self.currentSensor += 1

		self.updateOutput()

	# Down Button released event
	def down_button(self):
		if self.currentSensor > 1:
			self.currentSensor -= 1

		self.updateOutput()


	def convertTemp_button(self):
		self.displayCelcius = ~(self.displayCelcius)
		self.updateOutput()


	def read_data(self):
		self.monitor.read_sensor_data()
		self.updateOutput()

	def updateOutput(self):
		lastMeasurement = self.monitor.get_last_sensor_data(self.currentSensor)

		neededData = lastMeasurement[self.functions[self.functionNumber]]

		displayString = "S0" + str(self.currentSensor) + "  " + str(neededData)

		self.ui.screen_output.setText(displayString)

app = QApplication(sys.argv)
w = AppWindow()
w.show() 
sys.exit(app.exec_())