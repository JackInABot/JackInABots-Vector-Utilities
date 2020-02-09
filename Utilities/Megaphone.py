import time
import random
import glob
import os
from anki_vector import audio

class Megaphone:
    # Constructor sets up the attributes d^-^b #
    def __init__(self, set_robot):
        #setup sdk ref
        self.robot = set_robot

    def say(self, words=None):
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
                self.__write_to_robot_words(word)
        else:
            self.__write_to_robot_words(words)

    def play_audio_file(self, file_path, volume=None):
        volume = 80 if volume == None else volume

        #warn of bad inputs
        file_path = self.__check_valid_path(file_path)
        if(file_path == "bad input"):
            return

        #change string if necessary
        file_path = self.__figure_out_file_path(file_path)
        if(file_path == "bad input"):
            return

        self.__write_to_robot_stream_audio(file_path, volume)

    def play_audio_list(self, folder_path, volume=None, limit=None, randomize_list=None, delay=None):
        volume = 80 if volume == None else volume
        limit = 0 if limit == None else limit
        delay = 0 if delay == None else delay
        randomize_list = False if randomize_list == None else randomize_list

        #warn of bad inputs
        folder_path = self.__check_valid_path(folder_path)
        if(folder_path == "bad input"):
            return
        #change string if necessary
        folder_path = self.__figure_out_folder_path(folder_path)
        #get full folder list
        audio_list = glob.glob(folder_path)
        #randomize handler
        if(randomize_list == True):
            random.shuffle(audio_list)
        #limit handler
        if(limit != 0):
            audio_list = self.__limit_handler(audio_list, limit)

        for audio in audio_list:
            self.__write_to_robot_stream_audio(audio, volume)
            time.sleep(delay)

    def set_global_volume(self, volume):
        volume = self.__figure_out_set_volume(volume)
        #check for bad inputs
        if(volume == "bad input"):
            print("Insert a number 1 - 5 to set volume. 1 being LOW and 5 being HIGH.")
            print("Or insert string: LOW, MEDIUM LOW, MEDIUM, MEDIUM HIGH, HIGH to set volume")
            return
        
        self.__write_to_robot_master_volume(volume)

    def __write_to_robot_words(self, words):
        if(words == None):
            print("Var 'words' cannot be none before writing to robot")
            return

        self.robot.behavior.say_text(words)

    def __write_to_robot_stream_audio(self, audo_name, volume):
        #checks
        if(audo_name == None or volume == None):
            print("audio file name and/or voume var cannot be None before writing to robot")
            return
        if(not isinstance(volume,int) or volume < 0 or volume > 100):
            print("Volume must be between 0 - 100")
            return
        #write to robot
        self.robot.audio.stream_wav_file(audo_name, volume)

    def __write_to_robot_master_volume(self, volume):
        #standerd checks
        if(volume == None):
            print("volume var cannot be None before writing to robot")
            return
        
        self.robot.audio.set_master_volume(volume)

    def __limit_handler(self, audio_list, limit):
        i = 0
        limitList = []
        for audio in audio_list:
            if(i >= limit): break
            limitList.append(audio)
            i += 1

        return limitList

    def __check_valid_path(self, path_var):
        #checks
        if(path_var == None or not isinstance(path_var,str)):
            print("Argument must be a string of the path which leads to the audio file you wish to write to Vector")
            return "bad input"
        if('/' not in path_var):
            if('\\' not in path_var):
                print("Argument doesn't look like a path. Expecting: '/Folder/Subfolder/Audio.wav' for example.")
                return "bad input"
        #if we get here, all systems go!
        return path_var


    def __figure_out_set_volume(self, volume):
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
    def __figure_out_file_path(self, file_path):
        #if file doesn't appear to present, try to get it.
        if file_path.endswith('/') or file_path.endswith('\\'):
            print("File doesn't seem to be included in the path. Attempting to grab it from whats specified.")
            file = os.listdir(file_path)[0]
            if(file == None):
                print("Couldn't find a file in the path specified")
                return "bad input"
            else:
                file_path = file_path+file

        #catch if extension not present and add if needed
        if(".wav" in file_path):
            return file_path
        else:
            return file_path + ".wav"

    # format string to get multiple
    def __figure_out_folder_path(self, folder_path):
        #*.wav lets glob know what file type to look for, it needs to be in the string
        if("*.wav" in folder_path):
            return folder_path
        else:
            if folder_path.endswith('/') or folder_path.endswith('\\'):
                return folder_path + "*.wav"
            else:
                return folder_path + "/*.wav"

