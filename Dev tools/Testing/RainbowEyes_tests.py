import time
import sys
import random
import anki_vector
sys.path.insert(0,".")
#get utility paths
from Utilities import RainbowEyes as rbe
from Utilities import Megaphone as mph

def main():
    print("Welcome to the RainbowEyes Test script!")
    print("In order to test properly, make sure your Vector is:")
    print("1) Operational and fully charged")
    print("2) Set up properly to the SDK")
    print("3) Within your eyesight. \n")
    print("You'll need to observe Vectors behaviour throughout this procedure, if he doesn't behave as expected. Please report it to the projects Github Page: https://github.com/JackInABot/JackInABots-Vector-Utilities/issues \n")
    go_next = input("Press [Enter] to coninue ")

    with anki_vector.Robot() as robot:
        # d^-^b Setup utility object for test d^-^b #
        robotEyes = rbe.RainbowEyes(robot)
        # end init #
        # d^-^b Test Contents d^-^b #
        test_make_eyes_white(robotEyes)
        test_make_eyes_orange(robotEyes)
        test_make_eyes_dark_yellow(robotEyes)
        test_make_eyes_yellow(robotEyes)
        test_make_eyes_light_yellow(robotEyes)
        test_make_eyes_green(robotEyes)
        test_make_eyes_light_green(robotEyes)
        test_make_eyes_cyan(robotEyes)
        test_make_eyes_light_blue(robotEyes)
        test_make_eyes_blue(robotEyes)
        test_make_eyes_dark_blue(robotEyes)
        test_make_eyes_purple(robotEyes)
        test_make_eyes_pink(robotEyes)
        test_make_eyes_red(robotEyes)
        test_make_eyes_custom(robotEyes)
        test_make_eyes_random(robotEyes)
        test_make_eyes_rainbow(robotEyes)
        test_make_eyes_pulse(robotEyes)

        #robot.behavior.say_text("Test Complete")
        print("Tests Complete. Returning Vector to his common state... \n\n\n\n\n")
        time.sleep(3)

#Tests#
def test_make_eyes_white(robotEyes):
    print("Testing method make_eyes_white()...")
    robotEyes.make_eyes_white()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_orange(robotEyes):
    print("Testing method make_eyes_orange()...")
    robotEyes.make_eyes_orange()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_dark_yellow(robotEyes):
    print("Testing method make_eyes_dark_yellow()...")
    robotEyes.make_eyes_dark_yellow()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_yellow(robotEyes):
    print("Testing method make_eyes_yellow()...")
    robotEyes.make_eyes_yellow()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_light_yellow(robotEyes):
    print("Testing method make_eyes_light_yellow()...")
    robotEyes.make_eyes_light_yellow()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_green(robotEyes):
    print("Testing method make_eyes_green()...")
    robotEyes.make_eyes_green()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_light_green(robotEyes):
    print("Testing method make_eyes_light_green()...")
    robotEyes.make_eyes_light_green()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_cyan(robotEyes):
    print("Testing method make_eyes_cyan()...")
    robotEyes.make_eyes_cyan()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_light_blue(robotEyes):
    print("Testing method make_eyes_light_blue()...")
    robotEyes.make_eyes_light_blue()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_blue(robotEyes):
    print("Testing method make_eyes_light_blue()...")
    robotEyes.make_eyes_light_blue()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_dark_blue(robotEyes):
    print("Testing method make_eyes_dark_blue()...")
    robotEyes.make_eyes_dark_blue()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_purple(robotEyes):
    print("Testing method make_eyes_purple()...")
    robotEyes.make_eyes_purple()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_pink(robotEyes):
    print("Testing method make_eyes_pink()...")
    robotEyes.make_eyes_pink()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_red(robotEyes):
    print("Testing method make_eyes_red()...")
    robotEyes.make_eyes_red()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_custom(robotEyes):
    #gen values to go in
    hue = random.uniform(0.01, 0.99)
    sat = random.uniform(0.01, 0.99)
    #report the numbers to see if they come back out
    print("hue value generated for test:"+str(hue))
    print("sat value generated for test:"+str(sat))

    print("Testing method make_eyes_custom()...")
    robotEyes.make_eyes_custom(False, hue, sat)
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_random(robotEyes):
    print("Testing method make_eyes_random()...")
    robotEyes.make_eyes_random()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_rainbow(robotEyes):
    print("Testing method make_eyes_rainbow()...")
    robotEyes.make_eyes_rainbow()
    print("Test completed with no errors... \n")
    time.sleep(1)

def test_make_eyes_pulse(robotEyes):
    print("Testing method make_eyes_pulse()...")
    robotEyes.make_eyes_pulse()
    print("Test completed with no errors... \n")
    time.sleep(1)



if __name__ == '__main__':
    main()