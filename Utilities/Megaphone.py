import time
import random
import glob

class Megaphone:
    # Constructor sets up the attributes d^-^b #
    def __init__(self, setRobot):
        #setup sdk ref
        self.robot = setRobot

    def SaySomthing(self, words=None):
        #setup default words
        defaultWords = "try inserting a string into the method"
        #detect EasterEgg
        if(isinstance(words,str)):
            if(words.lower() == "try inserting a string into the method"):
                words = "very funny"
        #setup words
        words = defaultWords if words == None else words

        self.__WriteToRobotWords(words)

    def PlayAudioFile(self, fileName, filePath=None, volume=None):
        volume = 80 if volume == None else volume
        filePath = "" if filePath == None or filePath == 0 else filePath
        #checks
        if(fileName == None):
            print("Var 'fileName' cannot be none before writing to robot")
            return
        #if filepath not None we add it to fileName
        if(filePath != ""): fileName = filePath + fileName
        self.__StreamAudio(fileName, volume)

    def PlayAudioList(self, folderPath, volume):
        folderPath = folderPath + "*.wav" #*.wav makes glob know what files to look for        audioList = glob.glob(folderPath)
        print(audioList)
        for audio in audioList:
            self.__StreamAudio(audio, volume)

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

