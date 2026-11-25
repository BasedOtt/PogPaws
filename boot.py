import digitalio
import storage
from PogPawsPinout import PAWPADS
# import usb_cdc

config_mode = False

# Set up each pawpad as a digital input
# Pressing a pawpad pulls voltage low
# pullup resistor enabled to keep voltage high when not pressed
for pawpad in PAWPADS:
    # name = pawpad[0]
    pin = pawpad[1]
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

    # If a pawpad is pressed, then enter configuration mode
    if not btn.value:
        config_mode = True
    btn.deinit()

if not config_mode:
    storage.disable_usb_drive()
    # Optional: uncomment the line below to also hide the USB serial/COM port
    # usb_cdc.disable()