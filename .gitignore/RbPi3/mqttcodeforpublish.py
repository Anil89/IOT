'''
objective: to publish some data on a particular topic to an mqtt boker

step1 define your mqtt client
step2 connect to the broker
step3 publish data

step4 close the connection

'''

import paho.mqtt.client as mqtt
c=mqtt.Client()
c.connect("iot.eclipse.org",1883)
c.publish("collabera/iot","temp: "+str(x),qos=1)
c.disconnect()




