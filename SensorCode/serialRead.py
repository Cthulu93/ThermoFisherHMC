import time
import serial
import re
import boto
from boto.s3.key import Key
import boto.dynamodb2
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
import decimal
import os



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

def checkForTimelapse(bucket, prevFileList):
        directory = '/tmp/motion/'
        allFiles = sorted(os.listdir(directory),
                          key=lambda p: os.path.getctime(os.path.join('/tmp/motion', p)))
        # Check for new file
        if ((not (prevFileList == allFiles)) and len(allFiles) > 1):
                # Upload complete file
                print "New file detected, uploading."
                prevTimelapse = allFiles[-2]
                k = Key(bucket)
                k.key = prevTimelapse
                k.set_contents_from_filename(directory + prevTimelapse)
                return allFiles
        return prevFileList
                
                
                

if __name__=="__main__":
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    homeTable = createTableIfNotExists()
    conn = boto.connect_s3()
    bucket = conn.get_bucket('thermofisher-testvideos')
    startTime = time.time()
    timelapseList = sorted(os.listdir('/tmp/motion'),
                           key=lambda p: os.path.getctime(os.path.join('/tmp/motion', p)))
    while True:
        timelapseList = checkForTimelapse(bucket, timelapseList)
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



    
    
