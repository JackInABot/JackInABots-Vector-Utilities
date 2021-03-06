# JackInABots Vector Utilities
This is a pet project to create some easy to use, pick up and go executable code to utilise Vectors capabilities through the provided SDK.

### Contents
1. Installation Info
1. Quick Start Implementation
1. What's included
1. Feedback of any kind
1. Documentation
1. Copyright and legal stuffs


## 1. Installation Info
All of the utilities rely on the Vector SDK being operational, ensure that the SDK is working on your device and communicating with your vector before using any of the utilities. [Here is the tutorial provided by Anki to do that](https://developer.anki.com/vector/docs/index.html).

Right now this repo is under development, and therefore is not available from pip3 or anything like that. Right now the best way to gain access to the utilities is to implement `from Utilities import <Utility Filename> as <classRef>` into any file using the Utilities. So to import the RainbowEyes utility: `from Utilities import RainbowEyes as rbe`.

**Also, ensure the _Utilities_ folder is inside the same directory as your project folder and / or the file(s) which will be using them**.

I promise I plan to have this available to download via pip3 in the future so stay tuned while I figure that out -_-

## 2. Quick Start Implementation
The ease of use is the biggest factor of this project, and so the utilities are organised into classes which only require you to pass the reference of the SDK into the object initialisation. Here's an example of how to initialise a utility object, in this example we're initiating the RainbowEyes utility:
```python
from Utilities import RainbowEyes as rbe #from Utilities import <Utility-File> as <class-ref>

args = anki_vector.util.parse_command_args() #SDK setup
with anki_vector.Robot(args.serial) as robot: #SDK setup
    robotEyes = rbe.RainbowEyes(robot) #init object of RainbowEyes
```
The two lines below the import were extracted directly from the vector tutorial scripts provided by the SDK (which I hope you've seen already) and so instead of writing directly to that robot object, we simply pass it into the Utility we are planning to use.

The next step is easy, just use the initiated objects methods, (in our example, that’s 'robotEyes') like so:
```python
robotEyes.make_eyes_blue()
```
The utility classes have private methods which handle communication to the SDK and the functionality of the public methods which you are able to access, for more information of all the current supported utilities and their helpful methods, check the [wiki](https://github.com/JackInABot/JackInABots-Vector-Utilities/wiki)!

## 3. What's included
This repo currently contains the following:
#### Utilities
* RainbowEyes - Control Vectors eye colour
* Megaphone - Control Vectors audio output

#### Dev tools
* Animation - Check if local animations are out of date
* Testing - Run through the utilities methods to check if they work as expected.

#### Examples
* HAL_9000_impression.py - Have Vector do a HAL 9000 impression.
* Count_to_10.py - Have Vector count from 1 to 10... in french!

Any of the contents of the `Examples`folder or the `Dev tools` folder do not affect the Utilities in any way and can be deleted if you don't want them. Everything inside the `Utilities` folder does coincidentally rely on the functionality of a Utility.

Also just an important note. `main.py` is setup to act as a manual testing environment for the utilities included in the repo. `main.py` is **not essential** to the functionality of the Utilities and **can be deleted** if you would prefer it not exist. For more information on what the utilities do, check the [wiki](https://github.com/JackInABot/JackInABots-Vector-Utilities/wiki)!

## 4. Feedback of any kind
This project is open to any feedback you have, suggestions or bug highlighting. You can hopefully reach me on here if you go to the issues tab and speak your mind there. If it isn't set up yet I’m sorry, this is my first git repo, I will figure it out soon :)

## 5. Documentation
All documentation, including an overview of the utilities and their purpose, to the intricate details of how all the methods work and what their arguments do, can be found in the [wiki](https://github.com/JackInABot/JackInABots-Vector-Utilities/wiki).

## 6. Copyright and legal stuffs
All copyright goes to Anki. As the SDK is freely available I am under the assumption it is allowed to develop software that relies on it. This is a pet project and will not be commercialised or monetised in any way. I am doing this because it is fun! :) 

This project is open for feedback and contribution from others. I encourage people to take it, use it, change / upgrade it to suit your needs for your projects.
