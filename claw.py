#!/usr/bin/env python3

import logging
import signal
import sys
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor
from time import sleep

CLAW_DEGREES_OPEN = 225
CLAW_DEGREES_CLOSE = 920 
CLAW_SPEED_PCT = 50

# claw open
def claw_open(motor : MediumMotor, state : bool):
    if state:
        motor.on(speed=CLAW_SPEED_PCT * -1, block=True)
        motor.off()
        motor.reset()
        motor.on_to_position(speed=CLAW_SPEED_PCT, position=CLAW_DEGREES_OPEN, brake=False, block=True)

# claw close
def claw_close(motor : MediumMotor, state : bool):
    if state:
        motor.on_to_position(speed=CLAW_SPEED_PCT, position=CLAW_DEGREES_CLOSE)
        
medium_motor = MediumMotor(OUTPUT_A)

loop_times = 10
i = 0
while i < loop_times:
    claw_open(medium_motor, True)
    sleep(0.5)
    claw_close(medium_motor, True)
    sleep(0.5)
    i = i + 1
claw_open(medium_motor, True)