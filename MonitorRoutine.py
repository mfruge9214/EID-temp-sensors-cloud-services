#########################
# File: MonitorRoutine.py
# Author: Mike Fruge & Bryan Cisneros
# Description:
# 		Implements the routine to run the temp sensor Monitor. It simply has the
#		monitor generate a report every 30 seconds
#		
#########################


from Monitor import Monitor
from time import sleep

monitor = Monitor()

while True:
	monitor.generate_report()
	sleep(30)
