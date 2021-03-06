#!/usr/bin/python
# based on Matt Hawkins' code http://www.raspberrypi-spy.co.uk/?p=1101
# Re written by Ryan Walmsley & Further edited by Alan Pullen
# Based on code from: https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/wiimote/

import cwiid
import piconzero as pz
import hcsr04 as sonar
import time

numPixels = 17
# Define various facial expressions
smileData   = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
frownData   = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
grimaceData = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
oooohData   = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
pairData    = [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1]

# Initialise the Picon Zero
pz.init()
pz.setOutputConfig(5, 3)  # set output 5 to WS2812

# Initialise the HC-SR04
sonar.init()

def clearFace():
    pz.setAllPixels(0, 0, 0)


def showFace(data, Red, Green, Blue):
    for i in range(numPixels):
        if (data[i] > 0):
            pz.setPixel(i, Red, Green, Blue, False)
        else:
            pz.setPixel(i, 0, 0, 0, False)
    pz.updatePixels()

button_delay = 0.1

showFace(pairData, 0, 0, 255)
time.sleep(1)
print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

wii = None
i = 2
# Try to connect to the Wiimote & quit if not found after several attempts
while not wii:
    try:
        wii = cwiid.Wiimote()
    except RuntimeError:
        if i > 10:
            print "Error: Could Not Connect to WiiMote"
            showFace(pairData, 255, 0, 0)  #
            time.sleep(1)
            sonar.cleanup()
            quit()
            break
        print "Trouble connecting to connect to Wiimote"
        print "attempt " + str(i)
        i += 1
        showFace(pairData, 255, 0, 255)#
        time.sleep(1)

print 'Wiimote connected'
wii.led = 1
showFace(pairData, 0, 255, 0)
wii.rpt_mode = cwiid.RPT_BTN
time.sleep(1)

while True:
    buttons = wii.state['buttons']
    if (buttons & cwiid.BTN_UP):
        # Forwards
        # stop all motors if too close to an object to prevent face plant
        if sonar.getDistance() < 10:
            pz.stop()
            showFace(oooohData, 0, 255, 0)
        else:
            time.sleep(button_delay)
            pz.forward(50)
            showFace(smileData, 255, 0, 0)
    elif (buttons & cwiid.BTN_DOWN):
        time.sleep(button_delay)
        pz.reverse(50)
        showFace(grimaceData, 255, 0, 255)
    elif (buttons & cwiid.BTN_LEFT):
        time.sleep(button_delay)
        pz.spinLeft(50)
        showFace(oooohData, 0, 255, 0)
    elif (buttons & cwiid.BTN_RIGHT):
        time.sleep(button_delay)
        pz.spinRight(50)
        showFace(oooohData, 0, 255, 0)
    else:
        pz.stop()
        showFace(frownData, 0, 0, 255)
    # press button A to stop all motors
    if (buttons & cwiid.BTN_A):
        time.sleep(button_delay)
        pz.stop()
        showFace(frownData, 0, 0, 255)


