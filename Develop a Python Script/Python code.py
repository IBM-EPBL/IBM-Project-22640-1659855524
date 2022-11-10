Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #IBM Watson IOT Platform
... import wiotp.sdk.device
... import time
... import random
... myConfig = { 
...     "identity": {
...         "orgId": "hj5fmy",
...         "typeId": "NodeMCU",
...         "deviceId":"12345"
...     },
...     "auth": {
...         "token": "12345678"
...     }
... }
... 
... def myCommandCallback(cmd):
...     print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
...     m=cmd.data['command']
... 
... client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
... client.connect()
... 
... while True:
...     temp=random.randint(-20,125)
...     hum=random.randint(0,100)
...     myData={'temperature':temp, 'humidity':hum}
...     client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
...     print("Published data Successfully: %s", myData)
...     client.commandCallback = myCommandCallback
...     time.sleep(2)
