import time
import random
import glob
import os
from anki_vector import audio

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

        #setup words if none
        words = defaultWords if words == None else words

        if(isinstance(words,list)):
            for word in words:
                self.__WriteToRobotWords(word)
        else:
            self.__WriteToRobotWords(words)

    def PlayAudioFile(self, filePath, volume=None):
        volume = 80 if volume == None else volume

        #warn of bad inputs
        filePath = self.__checkValidfPath(filePath)
        if(filePath == "bad input"):
            return

        #change string if necessary
        filePath = self.__figureOutFilePath(filePath)
        if(filePath == "bad input"):
            return

        self.__WriteToRobotStreamAudio(filePath, volume)

    def PlayAudioList(self, folderPath, volume=None, limit=None, randomizeList=None, delay=None):
        volume = 80 if volume == None else volume
        limit = 0 if limit == None else limit
        delay = 0 if delay == None else delay
        randomizeList = False if randomizeList == None else randomizeList

        #warn of bad inputs
        folderPath = self.__checkValidfPath(folderPath)
        if(folderPath == "bad input"):
            return
        #change string if necessary
        folderPath = self.__figureOutFolderPath(folderPath)
        #get full folder list
        audioList = glob.glob(folderPath)
        #randomize handler
        if(randomizeList == True):
            random.shuffle(audioList)
        #limit handler
        if(limit != 0):
            audioList = self.__limitHandler(audioList, limit)

        for audio in audioList:
            self.__WriteToRobotStreamAudio(audio, volume)
            time.sleep(delay)

    def SetGlobalVolume(self, volume):
        volume = self.__FigureOutSetVolume(volume)
        #check for bad inputs
        if(volume == "bad input"):
            print("Insert a number 1 - 5 to set volume. 1 being LOW and 5 being HIGH.")
            print("Or insert string: LOW, MEDIUM LOW, MEDIUM, MEDIUM HIGH, HIGH to set volume")
            return
        
        self.__WriteToRobotMasterVolume(volume)

    def __WriteToRobotWords(self, words):
        if(words == None):
            print("Var 'words' cannot be none before writing to robot")
            return

        self.robot.behavior.say_text(words)

    def __WriteToRobotStreamAudio(self, audoName, volume):
        #checks
        if(audoName == None or volume == None):
            print("audio file name and/or voume var cannot be None before writing to robot")
            return
        if(not isinstance(volume,int) or volume < 0 or volume > 100):
            print("Volume must be between 0 - 100")
            return
        #write to robot
        self.robot.audio.stream_wav_file(audoName, volume)

    def __WriteToRobotMasterVolume(self, volume):
        #standerd checks
        if(volume == None):
            print("volume var cannot be None before writing to robot")
            return
        
        self.robot.audio.set_master_volume(volume)

    def __limitHandler(self, audioList, limit):
        i = 0
        limitList = []
        for audio in audioList:
            if(i >= limit): break
            limitList.append(audio)
            i += 1

        return limitList

    def __checkValidfPath(self, pathVar):
        #checks
        if(pathVar == None or not isinstance(pathVar,str)):
            print("Argument must be a string of the path which leads to the audio file you wish to write to Vector")
            return "bad input"
        if('/' not in pathVar):
            if('\\' not in pathVar):
                print("Argument doesn't look like a path. Expecting: '/Folder/Subfolder/Audio.wav' for example.")
                return "bad input"
        #if we get here, all systems go!
        return pathVar


    def __FigureOutSetVolume(self, volume):
        #1 = LOW, 2 = MEDIUM LOW, 3 = MEDIUM, 4 = MEDIUM HIGH, 5 = HIGH
        
        #figure out bad inputs
        if(isinstance(volume,int)):
            if(volume < 0 or volume > 5):
                return "bad input"

        if(isinstance(volume,str)):
            #bit of string handling for fair comparison
            volume.lower()
            volume.replace(" ", "")
            #do checks
            if(volume == "low"): volume = 1
            elif(volume == "mediumlow"): volume = 2
            elif(volume == "medium"): volume = 3
            elif(volume == "mediumhigh"): volume = 4
            elif(volume == "high"): volume = 5
            else: return "bad input"
        
        #if we made it here, figure it out
        if(volume == 1):
            return audio.RobotVolumeLevel.LOW
        elif(volume == 2):
            return audio.RobotVolumeLevel.MEDIUM_LOW
        elif(volume == 3):
            return audio.RobotVolumeLevel.MEDIUM
        elif(volume == 4):
            return audio.RobotVolumeLevel.MEDIUM_HIGH
        elif(volume == 5):
            return audio.RobotVolumeLevel.HIGH
        else:
            #input must not be an int or a string
            return "bad input"



    # format string to get single
    def __figureOutFilePath(self, filePath):
        #if file doesn't appear to present, try to get it.
        if filePath.endswith('/') or filePath.endswith('\\'):
            print("File doesn't seem to be included in the path. Attempting to grab it from whats specified.")
            file = os.listdir(filePath)[0]
            if(file == None):
                print("Couldn't find a file in the path specified")
                return "bad input"
            else:
                filePath = filePath+file

        #catch if extension not present and add if needed
        if(".wav" in filePath):
            return filePath
        else:
            return filePath + ".wav"

    # format string to get multiple
    def __figureOutFolderPath(self, folderPath):
        #*.wav lets glob know what file type to look for, it needs to be in the string
        if("*.wav" in folderPath):
            return folderPath
        else:
            if folderPath.endswith('/') or folderPath.endswith('\\'):
                return folderPath + "*.wav"
            else:
                return folderPath + "/*.wav"

