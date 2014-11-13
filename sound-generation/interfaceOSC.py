# tutorial found at : http://stackoverflow.com/questions/16086667/using-supercollider-with-python
# additionally : http://www.caseyanderson.com/teaching/ipython-to-supercollider-via-osc/
# dependent on module : pyOSC


import OSC
import time, random
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = OSC.OSCMessage()
msg.setAddress("/print")
msg.append(400)
client.send(msg)
