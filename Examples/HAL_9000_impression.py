import time
import sys
import anki_vector
sys.path.append(".")
#get utility paths
from Utilities import RainbowEyes as rbe
from Utilities import Megaphone as megPhone

def main():
    print("Beginning Example...")
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robotEyes = rbe.RainbowEyes(robot)
        robotVoice = megPhone.Megaphone(robot)

        robotVoice.Say("Here is my Hal 9000 impression!")
        robotEyes.MakeEyesRed()
        time.sleep(2)
        robotVoice.Say("I'm sorry dave, I'm")
        time.sleep(1)
        robotEyes.MakeEyesLightBlue()
        robotVoice.Say("Okay, maybe my default voice isn't made for this role, let me try again.")
        time.sleep(1)
        robotEyes.MakeEyesRed()
        time.sleep(1)
        robotVoice.PlayAudioFile("../JackInABots-Vector-Utilities/Examples/Audio/HAL 9000/hal_quote.wav", 100)
        robotEyes.MakeEyesLightBlue()
        robotVoice.Say("Now THAT, was convincing!")


    print("Ending example. Returning Vector to his common state... \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)

if __name__ == '__main__':
    main()

