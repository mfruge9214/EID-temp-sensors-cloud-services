import atexit
import Complex_UI_Routine
import Simple_UI_Routine
import subprocess

# start the temp sensors in a subprocess
command = 'node TempSensorApplication.js 6'
sensor_process = subprocess.Popen(
    command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# start the Node JS server in a subprocess
command = 'node NodeWebServer.js'
node_server_process = subprocess.Popen(
    command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# start the Tornado webserver in a subprocess
command = 'python TornadoWebServer.py'
tornado_server_process = subprocess.Popen(
    command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# atexit help from:
# https://stackoverflow.com/questions/320232/ensuring-subprocesses-are-dead-on-exiting-python-program
def cleanup():
    print('Cleaning up')
    sensor_process.terminate()
    node_server_process.terminate()
    tornado_server_process.terminate()
    print('Done! Exiting')

atexit.register(cleanup)

print('Welcome to the Temperature Sensor Simulation!')
print('Which UI do you want to run?')
val = input('Enter "T" for touchscreen or "H" for hardware: ')
if val in ['T', 't']:
    print('Touchscreen UI selected')
    Complex_UI_Routine.UI_Run()
elif val in ['H', 'h']:
    print('Hardware UI selected')
    Simple_UI_Routine.UI_Run()
else:
    print('Invalid Selection!')
