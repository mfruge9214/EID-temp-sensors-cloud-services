import Complex_UI_Routine
import Simple_UI_Routine
import subprocess

# start the temp sensors in a subprocess
command = 'node TempSensorApplication.js 6'
subprocess.Popen(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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
