"""CircuitPython Essentials Pin Map Script"""
import time
import microcontroller
import board
from digitalio import DigitalInOut, Direction, Pull
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

#setup a keyboard as a device
kbd = Keyboard(usb_hid.devices)
keyboard = KeyboardLayoutUS(kbd)

#define that i2c will be used and the pins to be used are gp7 and gp6 at a frequency of 400KHz
i2c=busio.I2C(board.GP7, board.GP6, frequency=400000)


#Lock the I2C device before we try to scan
while not i2c.try_lock():
    pass

#With a try block, it will ensure that i2.unlock is run
try:
    #Print the addresses found 
    print("I2C addresses found:",[hex(device_address) for device_address in i2c.scan()])
    #initialize the wii peripheral
    i2c.writeto(0x52,bytes([0xF0,0x55]))
    i2c.writeto(0x52,bytes([0xFB,0x00]))
    #Read the device ident from the extension register
    i2c.writeto(0x52,bytes([0xFA]))
    ident = bytearray(6)
    i2c.readfrom_into(0x52,ident)
    print("Device ID for device 0x52:", hex(ident[0]), hex(ident[1]), hex(ident[2]), hex(ident[3]), hex(ident[4]), hex(ident[5]))
finally:
    #unlock the i2c bus when finished scanning
    i2c.unlock()
#setup variables before infinite loop
#default value for keyboard_on is 0
keyboard_on = 0;
while True:
    led.value = True
    time.sleep(.1)
    led.value = False
    time.sleep(.1)
    while not i2c.try_lock():
        pass
    try:
        #Read data frame which is 6 bytes and it starts at address 0x00
        i2c.writeto(0x52,bytes([0x00]))
        wii_controller_frame = bytearray(6)
        i2c.readfrom_into(0x52,wii_controller_frame)
        #Extract Right X-Axis bits
        rx = (wii_controller_frame[2] & 0x80) >> 7
        rx = rx | ((wii_controller_frame[1] & 0xC0) >> 5)
        rx = rx | ((wii_controller_frame[0] & 0xC0) >> 3)
        print("Right Joystick, X-axis:", bin(rx))
        #Extract Right Y-Axis bits
        ry = (wii_controller_frame[2] & 0x1F)
        print("Right Joystick, Y-axis:", bin(ry))
        #Extract Left X-Axis bits and normalize to 5 bits like right stick
        lx = ((wii_controller_frame[0] & 0x3F) >> 1)
        print("Left Joystick, X-axis: ", bin(lx))
        #Extract Left Y-Axis bits and normalize to 5 bits like right stick
        ly = ((wii_controller_frame[1] & 0x3F) >> 1)
        print("Left Joystick, Y-axis: ", bin(ly))
        #Extract digital directional pad
        du = (wii_controller_frame[5] & 0x01)
        dd = ((wii_controller_frame[4] & 0x40) >> 6)
        dr = ((wii_controller_frame[4] & 0x80) >> 7)
        dl = ((wii_controller_frame[5] & 0x02) >> 1)
        print("up:",bin(du),"down:",bin(dd),"right:",bin(dr),"left:",bin(dl))
        #Extract digital action buttons
        da = ((wii_controller_frame[5] & 0x10) >> 4)
        db = ((wii_controller_frame[5] & 0x40) >> 6)
        dx = ((wii_controller_frame[5] & 0x08) >> 3)
        dy = ((wii_controller_frame[5] & 0x20) >> 5)
        print("a: ",bin(da),"   b:",bin(db),"    x:",bin(dx),"   y:",bin(dy))
        #Extract digital menu buttons
        minus = ((wii_controller_frame[4] & 0x10) >> 4)
        home = ((wii_controller_frame[4] & 0x08) >> 3)
        plus = ((wii_controller_frame[4] & 0x04) >> 2)
        print(" -:",bin(minus),"home:",bin(home),"    +:",bin(plus))
        #Extract Shoulder buttons
        zl = ((wii_controller_frame[5] & 0x80) >> 7)
        zr = ((wii_controller_frame[5] & 0x04) >> 2)
        lt = ((wii_controller_frame[4] & 0x20) >> 5)
        rt = ((wii_controller_frame[4] & 0x02) >> 1)
        print("zl:",bin(zl),"  zr:",bin(zr),"   lt:",bin(lt),"  rt:",bin(rt))
        print("------------------------------------------------")
        print("------------------------------------------------")
    finally:
        #unlock the i2c bus when finished scanning
        i2c.unlock()
    #use home button to turn on or off keyboard function. 
    keyboard_on = bool(keyboard_on) ^ bool(not home)
    print("State of keyboard_on flag: ", bool(keyboard_on))
    
    if keyboard_on:
        keyboard.write(str(lx))
        keyboard.write('\n')
        keyboard.write(str(ly))
        keyboard.write('\n')16
    