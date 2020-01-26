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
            returnVar = robotEyes.GetSavedEyeColour()
            print(returnVar)
            robotEyes.SetSavedEyeColour(0.5,1)
            returnVar = robotEyes.GetSavedEyeColour()
            print(returnVar)

            # end test #
            if(forever == False):
                break

        robot.behavior.say_text("Test Complete")
        print("Test Complete. Returning Vector to his common state...")
        time.sleep(3)

if __name__ == '__main__':
    main()
