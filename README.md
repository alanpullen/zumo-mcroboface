# Zumo McRoboFace

Zumo McRoboFace is a Zumo size robot with a face, powered by a Raspberry Pi with a McRoboFace (by 4Tronix) hence the name!

The motors and face are controlled using a 4Tronix PiCon Zero, with USB WiFi and Bluetooth dongles connected to a UUGear Zero4U hub.

The code for this is based upon the Raspberry Pi Foundation's Learning Resource for RoboButler ([https://www.raspberrypi.org/learning/robo-butler/](https://www.raspberrypi.org/learning/robo-butler/)) and has been adapted by myself under the terms of the Creative Commons [CC BY-SA](http://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA") License.

Details of McRoboFace can be found [here](http://4tronix.co.uk/mcroboface/ "here").

Code to allow multiple attempts to connect to the WiiMote was taken from here [https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/wiimote/](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/wiimote/ "https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/wiimote/") and is used under the terms of the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB "Creative Commons Attribution-ShareAlike 3.0 Unported License").

## PiCon Zero Library
The PiCon Zero library is developed and maintained by 4Tronix and is used here under the terms of the Creative Commons BY-SA License - See [CC  BY-SA](http://creativecommons.org/licenses/by-sa/3.0/"CC BY-SA"). 

See [http://4tronix.co.uk/piconzero/](http://4tronix.co.uk/piconzero/ "PiCon Zero") for more information about the PiCon Zero.

## Dependencies
**i2C**

i2c support must be enabled on your Raspberry Pi.

Use either `sudo raspi-config` to enable i2c or add the following to `/boot/config.txt`

    dtparam=i2c1=on
    dtparam=i2c_arm=on

Also ensure Python support is enabled by running the following command:

    sudo apt-get install python-smbus python3-smbus python-dev python3-dev

**CWiiD**

The CWiiD Module is required.  This can be installed using the following command:

    sudo apt-get install python-cwiid