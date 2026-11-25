import json
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from PogPawsPinout import PAWPADS

pawpad_names = tuple(pawpad_name for pawpad_name, _ in PAWPADS)
pins = tuple(pin for _, pin in PAWPADS)

def load_keymap(path="config.json"):
    keymap = {}
    try:
        with open(path, "r") as f:
            user_config = json.load(f)
        for pawpad, names in user_config.items():
            codes =[
                getattr(Keycode, name.upper()) for name in names if hasattr(Keycode, name.upper())
                ]
            keymap[pawpad] = codes
    except Exception as e:
        print("Config load error:", e)
    return keymap

keymap = load_keymap()
keybd = Keyboard(usb_hid.devices)
keys = keypad.Keys(pins, value_when_pressed=False, pull=True)

while True:
    event = keys.events.get()
    if event:
        pawpad_name = pawpad_names[event.key_number]
        codes = keymap.get(pawpad_name)
        if not codes:
            continue
        if event.pressed:
            keybd.press(*codes)
        elif event.released:
            keybd.release(*codes)