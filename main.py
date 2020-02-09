import time
import sys
import anki_vector
#get utility paths
from Utilities import RainbowEyes as rbe
from Utilities import Megaphone as mph

def main():
    # d^-^b vars for the test d^-^b #
    forever = False

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # d^-^b Any initial setup before test d^-^b #
        robotEyes = rbe.RainbowEyes(robot)
        robotVoice = mph.Megaphone(robot)

        # end init #
        print("Beginning Test...")
        while True:
            # d^-^b Test Contents d^-^b #
            robotEyes.make_eyes_rainbow(0,3)
            time.sleep(1)
            # end test # 
            if(forever == False):
                break
        
        #robot.behavior.say_text("Test Complete")
        print("Test Complete. Returning Vector to his common state... \n\n\n\n\n")
        time.sleep(3)


if __name__ == '__main__':
    main()





"""
Setup type one (with args):
---------------------------------------------------------------------------
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:

Setup type two (behaviour None)
Works only with - SetGlobalVolume()
---------------------------------------------------------------------------
    with anki_vector.Robot(behavior_control_level=None) as robot:


"""