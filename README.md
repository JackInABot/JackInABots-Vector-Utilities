# JackInABots Vector Utilities
This is a pet project to create some easy to use, pick up and go executable code to utilise Vectors capabilities through the provided SDK.

### Contents
1. Installation Info
1. How To Use
1. Utilities
    1. RainbowEyes
        1. `MakeEyes<Colour>`
        1. `MakeEyesCustom(hue,saturation)`
        1. `MakeEyesRandom(justHue,rangeVal)`
        1. `MakeEyesRainbow(delay,repeat)`
        1. `MakeEyesPulse(delay,repeat,setColour,toPercent,fromPercent)`

## 1. Installation Info
All of the utilities rely on the Vector SDK being operational, ensure that the SDK is working on your device and communicating with your vector before using any of the utilities. [Here is the tutorial provided by Anki to do that](https://developer.anki.com/vector/docs/index.html).

Right now this repo is under development, and therefore is not available from pip3 or anything like that. Right now the best way is to gain access to the utilities is to implement `sys.path.insert(0, '../JackInABots-Vector-Utilities/Utilities')` into any file using the Utilities **Then, make sure the _Utilities_ folder is inside the same directory as your project folder** to have access to the Utilities (I suppose you could change the directory string if you don't want the Utilities folder outside your project folder for any reason). Then all you need to do is import what you want to use from the Utilities folder, like so `import RainbowEyes as rbe`.

I promise I plan to have this available to download via pip3 in the future so stay tuned while I figure that out -_-

## Structure & Quirks
TBD if this is necessary to explain

## 2. How To Use Utilities
The ease of use is the buggest factor of this project, and so the utilities are organisaed into classes which only require you to pass in the reference to the SDK. Heres an example in the case of the RainbowEyes Utility:
```python
import RainbowEyes as rbe

args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
    robotEyes = rbe.RainbowEyes(robot)
```
The two lines below the import were extracted directly from the vector tutorial scripts provided by the SDK (which I hope you've seen already) and so instead of writing directly to that robot object, we simply pass it into the Utility we are planning to use.

The next step is easy, just use the initiated objects methods, (in our example, thats 'robotEyes') like so:
```python
robotEyes.MakeEyesBlue()
```
The objects have private methods which handle communication to the SDK, and often provide a suite of functionality which can be switched on and off using the method arguments.

## 3. Utilities
### i. RainbowEyes
RainbowEyes is a utility to give simple control over vectors eye colour, it can be used to set and hold his eyes a static colour, or to create a gradient of colours which display fluently. 
#### `MakeEyes<Colour>`
Firstly it's important to know the range of colours that can be written to Vector. These methods simply set the `self.hue` and the `self.sat` properties of the object and write them to the SDK for you. These include:
* White via `MakeEyesWhite()`
* Orange via `MakeEyesOrange()`
* Dark yellow via `MakeEyesDarkYellow()`
* Yellow via `MakeEyesYellow()`
* LightYellow via `MakeEyesLightYellow()`
* Green via `MakeEyesGreen()`
* LightGreen via `MakeEyesLightGreen()`
* Cyan via `MakeEyesCyan()`
* Light blue via `MakeEyesLightBlue()`
* Blue via `MakeEyesBlue()`
* Dark blue via `MakeEyesDarkBlue()`
* Purple via `MakeEyesPurple()`
* Pink via `MakeEyesPink()`
* Red via `MakeEyesRed()`

These methods are written exactly as presented with no optional arguments available to be passed in.

#### `MakeEyesCustom(hue,saturation)`
If you wish to set your own static colour, there is `MakeEyesCustom()`. It functions the same as the other methods, but is overloaded with optional arguments `hue` and `saturation` which, when passed in, set the `self.hue` and the `self.sat` properties of the object and write them to the SDK for you.

#### `MakeEyesRandom(justHue,rangeVal)`
For fun there is a method which randomizes Vectors eye colour! `MakeEyesRandom()` when called with no arguments, creates a randomised value for the hue to display to vectors eyes.

The `justHue` argument can be set to False, in which case the method will also assign a randomised value for the `self.sat` property and write both the hue and the satuation value to the SDK. `justHue` is set to True by default and is an optional argument.

The `rangeVal` argument can be used to control the range of random numbers considered for the output. `rangeVal` is set to 100 by default and is an optional argument.

#### `MakeEyesRainbow(delay,repeat)`
RainbowEyes has a capability to gradient Vectors hue and satuation properties. This esestually means that that these properties can climb from 0 to 1 by a value of 0.01 for each loop, and write these values for every step that float value changes. This action cycles through all of the possible colours. This is exactly what `MakeEyesRainbow()` does. It utilises a CORE method `HueGradient()` to create a rainbow effect to his eyes, which cycles through all of the possible colours that Vector can display.

The `delay` argument allows you to control the speed of the colours cycling through the colour gradient. `delay` can be passed as an int or a float, int values = seconds whereas float values = milliseconds. `delay`is set to 0 by default and is an optional argument.

The `repeat` argument allows you to either set a nummber of times you want the loop to repeat represented by an integer value, or `repeat` can be set as a boolean value. When set to False the loop will not repeat, when set to True the method will repeat infinitly. **WARNING Currently the only way to break an infinite loop is with a Ctrl + C Interrupt command in the terminal. This will be changed at a later update I plan to add another Utility which handles security and logging for Vector, stay tuned :)**. `repeat` is set to 0 by default and is an optional argument.

#### `MakeEyesPulse(delay,repeat,setColour,toPercent,fromPercent)`
`MakeEyesPulse` utilises CORE methods `SaturationGradient()` and `ReverseSaturationGradient()` to 'pulse' the saturation value `self.sat` up and then back down by a value of 0.01 each loop. This affect makes vectors eyes go from full colour to no colour (or a lighter shade of the colour depending on the arguments passed in).

The `delay` argument allows you to control the speed of the saturation cycling through the colour gradient. `delay` can be passed as an int or a float, int values = seconds whereas float values = milliseconds. `delay`is set to 0 by default and is an optional argument.

The `repeat` argument allows you to either set a nummber of times you want the loop to repeat represented by an integer value, or `repeat` can be set as a boolean value. When set to False the loop will not repeat, when set to True the method will repeat infinitly. **WARNING Currently the only way to break an infinite loop is with a Ctrl + C Interrupt command in the terminal. This will be changed at a later update I plan to add another Utility which handles security and logging for Vector, stay tuned :)**. `repeat` is set to 0 by default and is an optional argument.

The `setColour`argument allows you to set the colour which will be statically assigned to vector before the 'pulsing' loop begins. `setColour` can be a float, int or a string. As a float value `setColour` must be between 0 and 1 (e.g 0.3). As an int value `setColour` must be either 0 or 1. As a string value `setColour` must be a correctly spelt colour out of the selection; "orange","darkyellow","yellow","lightyellow","green","lightgreen","cyan","lightblue","blue","darkblue","purple","pink" or "red".

The `toPercent`argument sets the percentage that the saturation is allowed to reach and return from. `toPercent` is set to 0 by default in the CORE method `ReverseSaturationGradient()` & is set to 100 by `SaturationGradient()`. This means by default the `self.sat` value travels from 0 to 100 and back to 0. `toPercent` can be passed as an int or a float value. As an int, `toPercent` must be between 0 & 100 (as its a percentage). As a float value `toPercent` must be between 0 and 1. `toPercent` is an optional argument.

The `fromPercent` argument allows you to define a percentage you want the pulse to start from. Maybe you don't want to start from 0 and have the full colour displayed, and so you could set `fromPercent` to 20 and have the pulse start with self.sat set to 0.2. Then it would loop up by 0.01 per loop all the way up to whatever is set to `toPercent` and then back down. `fromPercent` can be passed as an int or a float value. As an int, `toPercent` must be between 0 & 100 (as its a percentage). As a float value `fromPercent` must be between 0 and 1. `fromPercent` is an optional argument.
