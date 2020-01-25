# JackInABots-Vector-Utilities
This is a pet project to create some easy to use, pick up and go executable code to utilise Vectors capabilities through the provided SDK.

## Contents
1. Installation Info
1. How To Use
1. Utilities
    1. RainbowEyes


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
#### 3.1. RainbowEyes
