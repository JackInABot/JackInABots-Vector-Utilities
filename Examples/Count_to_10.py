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

        robotVoice.PlayAudioList("../JackInABots-Vector-Utilities/Examples/Audio/French numbers",100)

        print("Ending example. Returning Vector to his common state... \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(1)

if __name__ == '__main__':
    main()