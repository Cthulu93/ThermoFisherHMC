from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
import decimal
import time


current_time = time.time()

data = Table('raspi')
result = data.query_2(station__eq='home',date__gte=current_time-6000)


temp_low = 100
temp_high = 0
humidity_low = 100
humidity_high = 0
light_low = 100
light_high = 0

for res in result:
        temp = res['temperature']
        if temp > temp_high:
                temp_high = temp
        if temp < temp_low:
                temp_low = temp

        humidity = res['humidity']
        if humidity > humidity_high:
                humidity_high = humidity
        if humidity < humidity_low:
                humidity_low = humidity

        light = res['light']
        if light > light_high:
                light_high = light
        if light < light_low:
                light_low = light


data.put_item(data={
                'station' : 'high_low',
                'date' : current_time,
                'type' : 'temperature',
                'temp_high' : temp_high,
                'temp_low' : temp_low,
                'humidity_high' : humidity_high,
                'humidity_low' : humidity_low,
                'light_high' : light_high,
                'light_low' : light_low})