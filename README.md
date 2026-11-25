# About

PogPaws is a 10 button keyboard in the shape of pawpads. It connects to a PC through a micro USB cable. The buttons can be configured to any key combo you so desire.

I made this as a personal project some 4 years ago ( --.-- ) and I'm finally getting around to posting it on the internet. I've made a few of these and given them as trophies at gaming tournaments. If you won a PogPaws, congrats! If you'd like to see any additional features, requests and PRs are welcome.

# Configuration

To enter "Configuration Mode", simply plug in PogPaws while pressing any button. Check your File Explorer to view the PogPaws as a mounted drive. Inside the folder, there will be a file named ```config.json```. This is the file you edit with your desired keyboard inputs. Inputs can be values such as:

```
A
B
C
ONE
TWO
THREE
DELETE
DOWN_ARROW
SHIFT
```

The keys are US Keyboard layout, so if you want and exclamation mark (!), use
```
SHIFT,ONE
```

[!NOTE]
JSON files are picky! If you mis-format the JSON, PogPaws may silently fail (it doesn't send any keystrokes and there's no LED or notification saying it is broken). Make sure every line follows the pattern of the original ```config.json```

## Keyboard layout

There are 10 keys, 5 on the left pawpad, 5 on the right. They are numbered on each paw left to right, with the big pawpad being last. 

![PogPaws Layout](assets/layout.png)

# Dependencies

adafruit circuitpython raspberry pi pico en US 10.3.2 

adafruit circuitpython bundle 10.x-mpy-20261121 -> adafruit HID