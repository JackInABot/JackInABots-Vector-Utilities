# JackInABots-Vector-Utilities
This is a pet project to create some easy to use, pick up and go executable code to utilise Vectors capabilities through the provided SDK.

## Contents
1. Installation Info
1. How To Use
1. Utilities
    1.1. RainbowEyes


### 1. Installation Info
All of the utilities rely on the Vector SDK being operational, ensure that the SDK is working on your device and communicating with your vector before using any of the utilities. [Here is the tutorial provided by Anki to do that](https://developer.anki.com/vector/docs/index.html).

Ultimately, it doesn't matter where you install this repo, the SDK will be initialised by the main.py file. The folder structure and filenames must remain the same for the utilities to work however.

### 2. How To Use Utilities
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

### 3. Utilities
#### i RainbowEyes
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

These methods are written exactly as presented with no optional arguments passed in.

#### `MakeEyesCustom(hue,saturation)`
If you wish to set your own static colour, there is `MakeEyesCustom()`. It functions the same as the other methods, but is overloaded with optional arguments `hue` and `saturation` which, when passed in, set the `self.hue` and the `self.sat` properties of the object and write them to the SDK for you.

#### `MakeEyesRandom(justHue,rangeVal)`
For fun there is a method which randomizes Vectors eye colour! `MakeEyesRandom()` when called with no arguments, creates a randomised value for the hue to display to vectors eyes. 

The `justHue` argument can be set to False, in which case the method will also assign a randomised value for the `self.sat` property and write both the hue and the satuation value to the SDK.

The `rangeVal` argument can be used to control the range of random numbers considered for the output.




