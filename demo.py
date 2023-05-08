#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import os

os.system('setfont Lat15-TerminusBold14')
print("Hello, my name is EV3")
sound = Sound()
sound.speak('Hello, my name is EV3!')
sound.speak('Welcome chen ke yu!')

motor_a = LargeMotor(OUTPUT_A)
motor_b = LargeMotor(OUTPUT_B)
motor_a.on_for_rotations(SpeedPercent(100), 5)
motor_b.on_for_rotations(SpeedPercent(100), 5)

sound.beep(20)