import numpy as np
import matplotlib.pyplot as plt

m boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
import decimal
import time

# creates plots from the last 10 minutes
current_time = time.time()

data = Table('raspi')
result = data.query_2(station__eq='home',date__gte=current_time-600)


temp_vector = []
light_vector = []
hum_vector = []
time_vector = []

for res in result:
	temp_vector.append[res['temperature']]
	light_vector.append[res['light']]
	hum_vector.append[res['humidity']]

time_vector = [i*(600/len(temp_vector)) for i in range(len(temp_vector))]	

print time_vector

plotTempHumLight(time_vector, temp_vector, hum_vector, light_vector)

def calcHeatIndex(temp, hum):
    tempinF = float(C) * 9 / 5 + 32
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783 * 10**(-3)
    c6 = -5.481717 * 10**(-2)
    c7 = 1.22874 * 10**(-3)
    c8 = 8.5282 * 10**(-4)
    c9 = -1.99 * 10**(-6)
    heatIndex = c1 + c2*temp + c3*hum + c4*temp*hum + c5*(temp**2) + \
                c6*(hum**2) + c7*(temp**2)*hum + c8*temp*(hum**2) + c9*(temp**2)*(hum**2)
    return heatIndex

def simpleDataPlot(time, data, color='b', filename='lastFig.png'):
    timeArray = np.array(time)
    datArray = np.array(data)
    plt.plot(timeArray, datArray, color)
    #plt.show()
    plt.savefig(filename, dpi=300)

def plotTempHumLight(time, temp, hum, light, filename = 'lastFig.png'):
    timeArray = np.array(time)
    tempArray = np.array(temp)
    humArray = np.array(hum)
    lightArray = np.array(light)
    plt.plot(timeArray, tempArray, 'r', timeArray, humArray, 'g',
             timeArray, lightArray, 'b')
    plt.savefig(filename, dpi=300)
