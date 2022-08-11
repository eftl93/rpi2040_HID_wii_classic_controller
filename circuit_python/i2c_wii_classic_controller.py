# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Pin Map Script"""
import time
import microcontroller
import board
from digitalio import DigitalInOut, Direction, Pull
import busio

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

i2c=busio.I2C(board.GP7, board.GP6)

#Lock the I2C device before we try to scan
while not i2c.try_lock():
    pass
#Print the addresses found 
print("I2C addresses found:",[hex(device_address) for device_address in i2c.scan()])

#unlock the i2c bus when finished scanning
i2c.unlock()

while True:
    led.value = True
    time.sleep(1.00)
    led.value = False
    time.sleep(1.00)

