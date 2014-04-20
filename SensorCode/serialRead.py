import time
import serial
import re
import boto.dynamodb2
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
import decimal



def createTableIfNotExists():
        homeTable = Table('raspi')
##        if homeTable is None:
##                print("Hello")
##                homeTable = Table.create('raspi', 
##                        schema=[HashKey('station'), RangeKey('date', data_type=NUMBER)])
        return homeTable

def writeToDB(table, temp, hum, light):
    table.put_item(data={
		'station': 'home',
		'date': decimal.Decimal(1)*decimal.Decimal(time.time()),
		'temperature': decimal.Decimal(1)*decimal.Decimal(temp),
                'humidity': decimal.Decimal(1)*decimal.Decimal(hum),
                'light': decimal.Decimal(1)*decimal.Decimal(light)})

if __name__=="__main__":
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    homeTable = createTableIfNotExists()
    startTime = time.time()
    while True:
        line = ser.readline()
        print line
        currentTime = time.time()
        if ((int(currentTime) - int(startTime)) % 10 == 0):
                temp = re.search("Temperature:\s+([0-9.]+)", line)
                if (temp):
                    temp = float(temp.group(1))
                    #print temp
                hum = re.search("Humidity:\s+([0-9.]+)", line)
                if (hum):
                    hum = float(hum.group(1))
                    #print hum
                light = re.search("Light intensity:\s+([0-9.]+)", line)
                if (light):
                    light = float(light.group(1))
                    #print light
                if (temp and hum and light and not justWrote):
                        print "Writing to database"
                        writeToDB(homeTable, temp, hum, light)
                        justWrote = True
                else:
                        justWrote = False
        else:
                justWrote = False



    
    
