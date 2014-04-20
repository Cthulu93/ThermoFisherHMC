from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER
import decimal
import time

current_time = time.time()

data = Table('raspi')
result = data.query_2(station__eq='home',date__gte=current_time-3600)


count = 0
temp_accum = 0
light_accum = 0
humidity_accum = 0

for res in result:
    count += 1
    temp_accum += res['temperature']
    light_accum += res['light']
    humidity_accum += res['humidity']



temp_average = decimal.Decimal(str(float(temp_accum)/float(count)))
light_average = decimal.Decimal(str(float(light_accum)/float(count)))
humidity_average = decimal.Decimal(str(float(humidity_accum)/float(count)))

data.put_item(data={
                'station' : 'minute_average',
                'date' : current_time,
                'temperature' : temp_average,
                'light' : light_average,
                'humidity' : humidity_average})

