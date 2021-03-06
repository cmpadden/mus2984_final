# tutorial found at : http://stackoverflow.com/questions/16086667/using-supercollider-with-python
# additionally : http://www.caseyanderson.com/teaching/ipython-to-supercollider-via-osc/
# dependent on module : pyOSC

import OSC
import time, random

def sendMessageOSC(frequency, msgAddress="/acid"):
    try:
        client = OSC.OSCClient()
        client.connect( ( '127.0.0.1', 57120 ) )
        #client.connect( ( '192.168.1.21', 57120 ) )
        msg = OSC.OSCMessage()
        msg.setAddress(msgAddress)
        msg.append(frequency)
        client.send(msg)
    except Exception, e:
        print "Error in OSC Connection: " + str(e)
