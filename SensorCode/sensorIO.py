#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re
import subprocess
import dhtreader
import wiringpi2 as wp2
import serial
from time import time, sleep, localtime, strftime

DHTPin = 25
DHT11 = 11

dhtreader.init()
wp2.wiringPiSetupGpio()
ser = serial.Serial('/dev/ttyUSB0', 9600)
startTime = int(time())
while True:
    currentTime = int(time())
    if ((currentTime-startTime) % 3 == 0):
        #DHTdata = dhtreader.read(DHT11, DHTPin)
        output = subprocess.check_output(["/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "11", "25"]);
        print output
        matches = re.search("Temp =\s+([0-9.]+)", output)
        if (not matches):
            sleep(3)
            continue
        temp = float(matches.group(1))
  
        # search for humidity printout
        matches = re.search("Hum =\s+([0-9.]+)", output)
        if (not matches):
            sleep(3)
            continue
        humidity = float(matches.group(1))

        print "Temperature: %.1f C" % temp
        print "Humidity:    %.1f %%" % humidity
        if (temp):
            ser.write('A')
            light = ser.readline()
            print("Temp = {0} *C, Hum = {1} %".format(t, h))
            print ("Intensity = {0}".format(light))
            print(strftime('%Y-%m-%d %H:%M:%S', localtime(currentTime)))
        else:
            print 'Read failure'
        sleep(1)
    if ((currentTime - startTime) % 30 == 0):
        # code to upload to the cloud
        print 'Butts'
        sleep(1)
