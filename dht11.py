#!/usr/bin/python
# used sensor link https://www.amazon.fr/gp/product/B01MQIOTGB
################  connection description  ####################
# +   -> 3v3 for BCD or pin 1 for BOARD
# out -> #4  for BCD or pin 7 for BOARD
# -   -> Any ground on pi
import sys
import Adafruit_DHT
import requests
import datetime


DEVICE_ID = 'ABCDEF'
url = 'http://server.technosofteam.com/pi/api/dht11/'


try:
    while True:
	 i = datetime.datetime.now()
	 current_time_string = "%s-%s-%s %s:%s:%s" % (i.year, i.month, i.day, i.hour, i.minute, i.second)
         humidity, temperature = Adafruit_DHT.read_retry(11, 4)
         data = '{{"id":"{0:s}", "temp": "{1:0.1f}", "humidity": "{2:0.1f}", "instant" : "{3:s}"}} '.format(DEVICE_ID, temperature, humidity, current_time_string)
         response = requests.post(url, data=data)
         print "sending : " + data
         print response.text
except KeyboardInterrupt:
    print "\Stopping capture"

finally:
    print "\exit"

