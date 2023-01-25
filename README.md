# HID Keyboard Device with Raspberry Pi Pico

This project is to convert an old Wii Classic Controller into an emulator of an HID keyboard. Each button or action can be mapped into a key press. This is done by using a Raspberry Pi Pico with CircuitPython's HID library. It can easily be modified to do key sequences extremely fast (faster than any human can with their hands), it can be adjusted for games where button smashing is required (don't use it on online competition games).

# Approach
The way this classic controller used to communicate with the Wii-Remote is through the I2C protocol, the "wii-mote" would initialize communication with the classic controller. The wii-mote would receive data encrypted packages from the classic controller.

I request the data packages with the Raspberry Pi Pico in such a way that the classic controller will release the data unencrypted. This is done to not waste CPU cycles decrypting the packages. 

# Pre-Requsites
In order to do this project, CircuitPython and its libraries need to be installed on the Raspberry Pi Pico. The steps are as follows:

Download CircuitPython for Rasberry Pi Pico from the circuitpython page: https://circuitpython.org/board/raspberry_pi_pico/. In my project, I installed version 7.x The extension of the file will be.uf2

Go to this link and Download the libraries that match the version of CircuitPython that was installed: https://circuitpython.org/libraries

Open the zip file that was downloaded. Then find the lib folder. Inside the lib folder find the adafruit_hid folder. Copy it.

Inside the CIRCUITPY drive, open the lib folder and paste the adafruit_hid library.

# Process Flowchart
<img src="https://user-images.githubusercontent.com/86902176/214703327-a042d8aa-b180-40a3-a3a5-f75c8deda077.png" width="400">
