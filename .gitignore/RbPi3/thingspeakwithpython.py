from http.client import HTTPConnection

import numpy
import time

while True:
   x=100*numpy.random.random()
   x=round(x)
   print(x)
   conn=HTTPConnection('api.thingspeak.com',80)
   conn.request("GET","/update?api_key=XI9UK53865AFWE72&field3="+str(x))
   conn.close()
   time.sleep(2)
