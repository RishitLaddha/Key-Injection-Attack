import digitalio
from digitalio import DigitalInOut, Pull
from board import *
from adafruit_debouncer import Debouncer

# init button (payload trigger)
button1_pin = DigitalInOut(GP22)  # defaults to input
button1_pin.pull = Pull.UP        # internal pull-up
button1 = Debouncer(button1_pin)

# payload selection switches
# payload1 = GPIO4 to GND
# payload2 = GPIO5 to GND
# payload3 = GPIO10 to GND
# payload4 = GPIO11 to GND
payload1Pin = digitalio.DigitalInOut(GP4)
payload1Pin.switch_to_input(pull=digitalio.Pull.UP)
payload2Pin = digitalio.DigitalInOut(GP5)
payload2Pin.switch_to_input(pull=digitalio.Pull.UP)
payload3Pin = digitalio.DigitalInOut(GP10)
payload3Pin.switch_to_input(pull=digitalio.Pull.UP)
payload4Pin = digitalio.DigitalInOut(GP11)
payload4Pin.switch_to_input(pull=digitalio.Pull.UP)

# setup mode pin (GP0 to GND)
progStatusPin = digitalio.DigitalInOut(GP0)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)

# onboard LED for Raspberry Pi Pico W
led = DigitalInOut(LED)
led.switch_to_output(value=False)

