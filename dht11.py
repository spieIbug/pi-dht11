#!/usr/bin/python
# used sensor link https://www.amazon.fr/gp/product/B01MQIOTGB
################  connection description  ####################
# +   -> 3v3 for BCD or pin 1 for BOARD
# out -> #4  for BCD or pin 7 for BOARD
# -   -> Any ground on pi
import sys
import Adafruit_DHT
import requests

url = 'http://server.technosofteam.com/pi/'

try:
    while True:
         humidity, temperature = Adafruit_DHT.read_retry(11, 4)
         data = '{{"temp": "{0:0.1f}", "humidity": "{1:0.1f}"}} '.format(temperature, humidity)
         response = requests.post(url, data=data)
         print "sending : " + data
         # print response.text
except KeyboardInterrupt:
    print "\Stopping capture"

finally:
    print "\exit"

