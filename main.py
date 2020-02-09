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
            with anki_vector.Robot() as robot:
                print("List all animation trigger names:")
                anim_trigger_names = robot.anim.anim_trigger_list
                for anim_trigger_name in anim_trigger_names:
                    print(anim_trigger_name)

            # end test # 
            if(forever == False):
                break
        
        #robot.behavior.say_text("Test Complete")
        print("Test Complete. Returning Vector to his common state... \n\n\n\n\n")
        time.sleep(3)

def setupType1(funcRef):
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        funcRef()


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