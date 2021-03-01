import numpy as np
import matplotlib.pyplot as plt

def generate_graph(data):
    temps = {}
    hums = {}

    if(data == {}):
        # if there isn't any sensor data yet, just return
        return
            
    for sensor_id, sensor_data in data.items():
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

    fig, ax = plt.subplots(3, 2)
    fig.subplots_adjust(hspace=0.8, wspace=0.75, top=0.92, bottom=0.12)
    # Plot all the sensor data!
    for sensor_id in data.keys():
        tempList = temps[sensor_id]
        humList = hums[sensor_id]
        title = 'Sensor ' + str(sensor_id)
        row = int((sensor_id-1) / 2)
        col = (sensor_id-1) % 2

        # plotting help from:
        # https://matplotlib.org/3.2.1/gallery/subplots_axes_and_figures/two_scales.html
        temp_color = 'tab:blue'
        hum_color = 'tab:orange'
        ax[row][col].set_title(title)
        ax[row][col].set_xlabel('time (s)')
        units = '(F)'
        # if not self.monitor.fahrenheit:
        #     units = '(C)'
        ax[row][col].set_ylabel('Temperature ' + units, color=temp_color)
        ax[row][col].plot(timevals, tempList, color=temp_color)
        ax[row][col].tick_params(axis='y', labelcolor=temp_color)

        # get a copy of the axis so we can plot both temperature and humidity
        # on the same graph
        ax_hum = ax[row][col].twinx()
        ax_hum.plot(timevals, humList, color=hum_color)
        ax_hum.set_ylabel('Humidity (%)', color=hum_color)
        ax_hum.tick_params(axis='y', labelcolor=hum_color)
    
    # Finally, draw everything
    plt.savefig('eid_graph.png')