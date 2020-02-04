import time
import random
import glob

class Megaphone:
    # Constructor sets up the attributes d^-^b #
    def __init__(self, setRobot):
        #setup sdk ref
        self.robot = setRobot

    def Say(self, words=None):
        #setup default words
        defaultWords = "try inserting a string into the method"
        #detect EasterEgg
        if(isinstance(words,str)):
            if(words.lower() == "try inserting a string into the method"):
                words = "very funny"
        #setup words
        words = defaultWords if words == None or not isinstance(words,str) else words

        self.__WriteToRobotWords(words)

    def PlayAudioFile(self, filePath, volume=None):
        volume = 80 if volume == None else volume

        #checks
        if(filePath == None or not isinstance(words,str)):
            print("Argument 'filePath' must be a string of the path which leads to the audio file you wish to write to Vector")
            return

        self.__StreamAudio(filePath, volume)

    def PlayAudioList(self, folderPath, volume=None, limit=None, randomizeList=None, delay=None):
        volume = 80 if volume == None else volume
        limit = 0 if limit == None else limit
        delay = 0 if delay == None else delay
        randomizeList = False if randomizeList == None else randomizeList

        #change string if necessary
        folderPath = self.__figureOutPath(folderPath)
        #get full folder list
        audioList = glob.glob(folderPath)
        #randomize handler
        if(randomizeList == True):
            random.shuffle(audioList)
        #limit handler
        if(limit != 0):
            audioList = self.__limitHandler(audioList, limit)

        for audio in audioList:
            self.__StreamAudio(audio, volume)
            time.sleep(delay)

    def __WriteToRobotWords(self, words):
        if(words == None):
            print("Var 'words' cannot be none before writing to robot")
            return

        self.robot.behavior.say_text(words)

    def __StreamAudio(self, audoName, volume):
        #checks
        if(audoName == None or volume == None):
            print("audio file name and/or voume var cannot be None before writing to robot")
            return
        if(not isinstance(volume,int) or volume < 0 or volume > 100):
            print("Volume must be between 0 - 100")
            return
        #write to robot
        self.robot.audio.stream_wav_file(audoName, volume)

    def __limitHandler(self, audioList, limit):
        i = 0
        limitList = []
        for audio in audioList:
            if(i >= limit): break
            limitList.append(audio)
            i += 1

        return limitList

    def __figureOutPath(self, folderPath):
        #*.wav lets glob know what file type to look for, it needs to be in the string
        if("*.wav" in folderPath):
            return folderPath
        else:
            return folderPath + "*.wav"

