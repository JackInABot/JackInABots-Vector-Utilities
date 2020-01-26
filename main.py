import time
import sys
import anki_vector
#get utility paths
from Utilities import RainbowEyes as rbe

def main():
    # d^-^b vars for the test d^-^b #
    hue = 0
    sat = 1
    steps = 100
    delay = 0
    forever = False

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # d^-^b Any initial setup before test d^-^b #
        robotEyes = rbe.RainbowEyes(robot)

        # end init #
        print("Beginning Test...")
        while True:
            # d^-^b Test Contents d^-^b #
            robotEyes.MakeEyesBlue()
            time.sleep(1)
            robotEyes.MakeEyesDarkBlue()
            time.sleep(1)
            robotEyes.MakeEyesDarkYellow()
            time.sleep(1)
            robotEyes.MakeEyesGreen()
            time.sleep(1)
            robotEyes.MakeEyesLightBlue()
            time.sleep(1)
            robotEyes.MakeEyesLightGreen()
            time.sleep(1)
            robotEyes.MakeEyesLightYellow()
            time.sleep(1)
            robotEyes.MakeEyesOrange()
            time.sleep(1)
            robotEyes.MakeEyesPink()
            time.sleep(1)
            robotEyes.MakeEyesPurple()
            time.sleep(1)
            robotEyes.MakeEyesRed()
            time.sleep(1)
            robotEyes.MakeEyesWhite()
            time.sleep(1)
            robotEyes.MakeEyesYellow()
            time.sleep(1)
            robotEyes.MakeEyesCustom()
            time.sleep(3)
            robotEyes.MakeEyesRandom()
            time.sleep(3)
            robotEyes.MakeEyesRainbow()
            time.sleep(3)
            robotEyes.MakeEyesPulse()
            time.sleep(3)

            returnVar = robotEyes.GetSavedEyeColour()
            print(returnVar)
            time.sleep(1)
            robotEyes.SetSavedEyeColour(0.5,1)
            returnVar = robotEyes.GetSavedEyeColour()
            print(returnVar)
            time.sleep(1)

            # end test #
            if(forever == False):
                break

        robot.behavior.say_text("Test Complete")
        print("Test Complete. Returning Vector to his common state...")
        time.sleep(3)

if __name__ == '__main__':
    main()
