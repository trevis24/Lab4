import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
import version as ver

import socket
import time
from time import sleep


def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1

    return ret

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
    init()
    led.init
    lcd = LCD.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    lcd.lcd_clear()
    lcd.lcd_display_string("Trevis Tan", 1)  # write on line 1
    lcd.lcd_display_string("DevOps", 2)  # write on line 2
    # starting on 3rd column

    t=0
    while True:
        switch_position =read_slide_switch()

        if switch_position ==1:
            t=0
            blink_led(0.1)
        else:
            if t==0:
                t=time.time()

            if time.time()-t<5:
                blink_led(0.05)
            else:
                led.set_output(0,0)
    


if __name__ == "__main__":
    main()