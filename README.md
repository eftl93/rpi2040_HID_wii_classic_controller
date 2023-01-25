# HID Keyboard Device with Raspberry Pi Pico
<img src="https://user-images.githubusercontent.com/86902176/214705628-3525323f-78dc-455e-bf0d-cb8b7c128663.png" width="400">


This project is to convert an old Wii Classic Controller into an emulator of an HID keyboard. Each button or action can be mapped into a key press. This is done by using a Raspberry Pi Pico with CircuitPython's HID library. It can easily be modified to do key sequences extremely fast (faster than any human can with their hands), it can be adjusted for games where button smashing is required (don't use it on online competition games).

I have uploaded the complete project to hackster.io: https://www.hackster.io/ederfernandotorres3/hid-keyboard-device-with-raspberry-pi-pico-aa650f

## Approach
The way this classic controller used to communicate with the Wii-Remote is through the I2C protocol, the "wii-mote" would initialize communication with the classic controller. The wii-mote would receive data encrypted packages from the classic controller.

I request the data packages with the Raspberry Pi Pico in such a way that the classic controller will release the data unencrypted. This is done to not waste CPU cycles decrypting the packages. 

## Pre-Requsites (Software)
In order to do this project, CircuitPython and its libraries need to be installed on the Raspberry Pi Pico. The steps are as follows:

Download CircuitPython for Rasberry Pi Pico from the circuitpython page: https://circuitpython.org/board/raspberry_pi_pico/. In my project, I installed version 7.x The extension of the file will be.uf2

Go to this link and Download the libraries that match the version of CircuitPython that was installed: https://circuitpython.org/libraries

Open the zip file that was downloaded. Then find the lib folder. Inside the lib folder find the adafruit_hid folder. Copy it.

Inside the CIRCUITPY drive, open the lib folder and paste the adafruit_hid library.



## Pre-Requisites (Hardware)
First, the wii classic controller needs to be dissasembled and the original cable desoldered. 
<img src="https://user-images.githubusercontent.com/86902176/214707128-b6a34148-67a4-4f37-aeb6-d0cee6a991ac.png" width="400">

Then we need to solder the I2C pins of the Raspberry Pi to the corresponding pins on the controller PCB
<img src="https://user-images.githubusercontent.com/86902176/214706562-c611e855-0c72-4684-b68a-688290529561.png" width="400">

# Process Flowchart
<img src="https://user-images.githubusercontent.com/86902176/214703327-a042d8aa-b180-40a3-a3a5-f75c8deda077.png" width="400">


## How to use it
After downloading the code into the board, select the window that will be expecting the keyboard strokes. To activate the keyboard "mode" on the controller, press the "Home" button. Press it again to deactivate it.
