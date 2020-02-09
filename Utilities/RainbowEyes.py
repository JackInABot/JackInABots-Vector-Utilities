import time
import random

# Core functionality class #
class RainbowEyesCORE:
    # Constructor sets up the attributes d^-^b #
    def __init__(self, set_robot, set_hue=None, set_sat=None):
        #vars
        self.hue = 0 if set_hue == None else set_hue
        self.sat = 1 if set_sat == None else set_sat

        self.robot = set_robot

    #**  d^-^b GRADIENT EFFECT METHODS d^-^b **#
    def hue_gradient(self, delay=None, repeat=None, hold=None, to_colour=None, from_colour=None):
        if(not isinstance(to_colour, float)): #to_colour can be inputted as string, float
            to_colour = self.__figure_out_colour(to_colour) #use __figure_out_colour to handle alternative types
        if(not isinstance(from_colour, float)): #from_colour can be inputted as string, float
            from_colour = self.__figure_out_colour(from_colour) #use __figure_out_colour to handle alternative types
            
        to_colour = 1 if to_colour == None else to_colour
        from_colour = 0 if from_colour == None else from_colour
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold

        repeat_step = 0
        while True: #python do while loop
            print("Loop #"+str(repeat_step))
            #failsafe for bad inputs
            if (from_colour > to_colour):
                print("You must use ReverseHueColourGradient to go count up from "+str(from_colour)+" to "+str(to_colour))
                break
            self.__set_hue(from_colour)
            self.__set_sat(1)
            step = 0
            while(self.hue < to_colour):
                #step up float values
                self.__step_up_hue()
                #write to vector
                self.__write_to_robot()
                #ensure this loop is counted
                step += 1
                #apply delay
                time.sleep(delay)

            #This is the end of the 'do while' loop
            if(isinstance(repeat,bool)):
                if(repeat == False): 
                    break
            else:
                if(repeat_step >= repeat-1):
                    break
                else:
                    repeat_step += 1

        print("Holding "+str(self.hue)+" for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def reverse_hue_gradient(self, delay=None, repeat=None, hold=None, to_colour=None, from_colour=None):
        if(not isinstance(to_colour,float)): #to_colour can be inputted as string, float
            to_colour = self.__figure_out_colour(to_colour) #use __figure_out_colour to handle alternative types
        if(not isinstance(from_colour,float)): #from_colour can be inputted as string, float
            from_colour = self.__figure_out_colour(from_colour) #use __figure_out_colour to handle alternative types

        to_colour = 0 if to_colour == None else to_colour
        from_colour = 1 if from_colour == None else from_colour
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold

        repeat_step = 0
        while True: #python do while loop
            print("Loop #"+str(repeat_step))
            #failsafe for bad inputs
            if (from_colour < to_colour): 
                print("You must use hue_gradient to count down from "+str(from_colour)+" to "+str(to_colour))
                break
            self.__set_hue(from_colour)
            self.__set_sat(1)
            step = 0
            while(self.hue >= to_colour):
                #step up float values
                self.__step_down_hue()
                #write to vector
                self.__write_to_robot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeat_step >= repeat-1):
                    break
                else:
                    repeat_step += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def saturation_gradient(self, delay=None, repeat=None, hold=None, set_colour=None, to_percent=None, from_percent=None):
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold
        set_colour = 0 if set_colour == None else set_colour
        to_percent = 100 if to_percent == None else to_percent
        from_percent = 0 if from_percent == None else from_percent

        if(isinstance(set_colour,str)):
            set_colour = self.__figure_out_colour(set_colour)
        if(isinstance(to_percent,int)):
            to_percent =  self.__figure_out_percentage(to_percent)
        if(isinstance(from_percent,int)):
            from_percent =  self.__figure_out_percentage(from_percent)

        repeat_step = 0
        while True: #python do while loop
            print("Loop #"+str(repeat_step))
            #failsafe for bad inputs
            if (to_percent < from_percent):
                print("You must use reverse_hue_gradient to count down from "+str(from_percent)+" to "+str(to_percent))
                break
            self.__set_hue(set_colour)
            self.__set_sat(from_percent)
            step = 0
            while(self.sat <= to_percent):
                #step up float values
                self.__step_up_sat()
                #write to vector
                self.__write_to_robot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeat_step >= repeat-1):
                    break
                else:
                    repeat_step += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def reverse_saturation_gradient(self, delay=None, repeat=None, hold=None, set_colour=None, to_percent=None, from_percent=None):
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold
        set_colour = 0 if set_colour == None else set_colour
        to_percent = 0 if to_percent == None else to_percent
        from_percent = 100 if from_percent == None else from_percent

        if(isinstance(set_colour,str)):
            set_colour = self.__figure_out_colour(set_colour)
        if(isinstance(to_percent,int)):
            to_percent =  self.__figure_out_percentage(to_percent)
        if(isinstance(from_percent,int)):
            from_percent =  self.__figure_out_percentage(from_percent)

        repeat_step = 0
        while True: #python do while loop
            print("Loop #"+str(repeat_step))
            #failsafe for bad inputs
            if (to_percent > from_percent):
                print("You must use reverse_hue_gradient to count up from "+str(from_percent)+" to "+str(to_percent))
                break
            self.__set_hue(set_colour)
            self.__set_sat(from_percent)
            step = 0
            while(self.sat >= to_percent):
                #step up float values
                self.__step_down_sat()
                #write to vector
                self.__write_to_robot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeat_step >= repeat-1):
                    break
                else:
                    repeat_step += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    #Private methods for in house use only
    #Setters for colour change
    def __set_hue(self, newHue):
        self.hue = newHue
        
    def __set_sat(self, newSat):
        self.sat = newSat

    #methods to step up and down for gradient effect in loops
    def __step_up_hue(self):
        if(self.hue > 1):
            print("Cannot step hue value higher than 1")
        else:
            self.hue += 0.01
    
    def __step_up_sat(self):
        if(self.sat > 1):
            print("Cannot step saturation value higher than 1")
        else:
            self.sat += 0.01

    def __step_down_hue(self):
        if(self.hue < 0):
            print("Cannot step hue value lower than 0")
        else:
            self.hue -= 0.01
    
    def __step_down_sat(self):
        if(self.sat < 0):
            print("Cannot step saturation value lower than 0")
        else:
            self.sat -= 0.01
    
    def __figure_out_colour(self, colour, set=None):
        if(isinstance(colour,str)):
            colours={
                'orange':0.05,
                'darkyellow':0.1,
                'yellow':0.15,
                'lightyellow':0.2,
                'green':0.3,
                'lightgreen':0.4,
                'cyan':0.5,
                'lightblue':0.6,
                'blue':0.65,
                'darkblue':0.7,
                'purple':0.8,
                'pink':0.9,
                'red':1
            }

            return colours[colour.lower()]

    def __figure_out_percentage(self, percent):
        if(isinstance(percent,int)):
            #check valid percentage
            if(percent < 0 or percent > 100):
                print("Percentage must be an int between 0 and 100")
            
            return percent / 100

    #Write to robot what colours to display
    def __write_to_robot(self):
        print("Displaying | Hue: "+str(self.hue) +" | Sat: "+str(self.sat))
        self.robot.behavior.set_eye_color(hue=self.hue, saturation=self.sat)

# Main utility #
class RainbowEyes(RainbowEyesCORE):
    SavedHue = 0
    SavedSat = 0

    #**  d^-^b SET EYE COLOURS d^-^b **#
    def make_eyes_white(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0)
        self._RainbowEyesCORE__set_sat(0)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_orange(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.05)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_dark_yellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.1)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_yellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.15)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_light_yellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.2)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_green(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.3)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_light_green(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.4)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_cyan(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.5)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_light_blue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.6)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_blue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.65)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_dark_blue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.7)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_purple(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.8)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_pink(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(0.9)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_red(self):
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(1)
        self._RainbowEyesCORE__set_sat(1)
        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_custom(self, write_saved, hue=None, saturation=None):
        write_saved = False if write_saved == None else write_saved
        hue = self.hue if hue == None else hue
        saturation = self.sat if saturation == None else saturation

        if(write_saved):
            self.hue = self.SavedHue
            self.sat = self.SavedSat
        else:
            self.hue = hue
            self.sat = saturation

        self._RainbowEyesCORE__write_to_robot()

    def make_eyes_random(self, just_hue=None, range_val=None):
        just_hue = True if just_hue == None else just_hue #set just_hue to default or specified
        range_val = 100 if range_val == None else range_val #set range_val to default or specified
        #Make eyes change colour
        self._RainbowEyesCORE__set_hue(random.randrange(range_val)/100)
        if(just_hue == False): self._RainbowEyesCORE__set_sat(random.randrange(range_val)/100)
        self._RainbowEyesCORE__write_to_robot()
    
    def make_eyes_rainbow(self, delay=None, repeat=None):
        self._RainbowEyesCORE__set_sat(1)

        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat

        self.hue_gradient(delay,repeat)

    def make_eyes_pulse(self, delay=None, repeat=None, set_colour=None, to_percent=None, from_percent=None):
        repeat = 0 if repeat == None else repeat
        
        repeat_step = 0
        while True: #python do while loop
            print("Loop #"+str(repeat_step))
            #Make eyes pulse down
            self.reverse_saturation_gradient(delay,0,0,set_colour,from_percent,to_percent)
            #Make eyes pulse up
            self.saturation_gradient(delay,0,0,set_colour,to_percent,from_percent)

            #This is the end of the 'do while' loop
            if(isinstance(repeat, bool)):
                if(repeat == False):
                    break
            else:
                if(repeat_step >= repeat-1):
                    break
                else:
                    repeat_step += 1

    def set_saved_eye_colour(self, hue=None, sat=None):
        #if none specified, we set the current attributes into the saved
        hue = self.hue if hue == None else hue #set hue to default or specified
        sat = self.sat if sat == None else sat #set sat to default or specified

        self.SavedHue = hue
        self.SavedSat = sat
    
    def get_saved_eye_colour(self, which_return=None):
        which_return = "" if which_return == None else which_return #empty string means neither

        if(which_return.lower() == "hue"):
            return self.SavedHue
        elif(which_return.lower() == "saturation" or which_return.lower() == "sat"):
            return self.SavedSat
        else:
            #if we made it this far, well assume user wants both in array
            return [self.SavedHue, self.SavedSat]


