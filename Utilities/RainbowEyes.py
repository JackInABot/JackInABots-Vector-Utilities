import time
import random

# Core functionality class #
class RainbowEyesCORE:
    # Constructor sets up the attributes d^-^b #
    def __init__(self, setRobot, setHue=None, setSat=None):
        #vars
        self.hue = 0 if setHue == None else setHue
        self.sat = 1 if setSat == None else setSat

        self.robot = setRobot

    #**  d^-^b GRADIENT EFFECT METHODS d^-^b **#
    def HueGradient(self, delay=None, repeat=None, hold=None, toColour=None, fromColour=None):
        if(not isinstance(toColour, float)): #toColour can be inputted as string, float
            toColour = self.__figureOutColour(toColour) #use __figureOutColour to handle alternative types
        if(not isinstance(fromColour, float)): #fromColour can be inputted as string, float
            fromColour = self.__figureOutColour(fromColour) #use __figureOutColour to handle alternative types
            
        toColour = 1 if toColour == None else toColour
        fromColour = 0 if fromColour == None else fromColour
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold

        repeatStep = 0
        while True: #python do while loop
            print("Loop #"+str(repeatStep))
            #failsafe for bad inputs
            if (fromColour > toColour):
                print("You must use ReverseHueColourGradient to go count up from "+str(fromColour)+" to "+str(toColour))
                break
            self.__SetHue(fromColour)
            self.__SetSat(1)
            step = 0
            while(self.hue < toColour):
                #step up float values
                self.__StepUpHue()
                #write to vector
                self.__WriteToRobot()
                #ensure this loop is counted
                step += 1
                #apply delay
                time.sleep(delay)

            #This is the end of the 'do while' loop
            if(isinstance(repeat,bool)):
                if(repeat == False): 
                    break
            else:
                if(repeatStep >= repeat-1):
                    break
                else:
                    repeatStep += 1

        print("Holding "+str(self.hue)+" for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def ReverseHueGradient(self, delay=None, repeat=None, hold=None, toColour=None, fromColour=None):
        if(not isinstance(toColour,float)): #toColour can be inputted as string, float
            toColour = self.__figureOutColour(toColour) #use __figureOutColour to handle alternative types
        if(not isinstance(fromColour,float)): #fromColour can be inputted as string, float
            fromColour = self.__figureOutColour(fromColour) #use __figureOutColour to handle alternative types

        toColour = 0 if toColour == None else toColour
        fromColour = 1 if fromColour == None else fromColour
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold

        repeatStep = 0
        while True: #python do while loop
            print("Loop #"+str(repeatStep))
            #failsafe for bad inputs
            if (fromColour < toColour): 
                print("You must use HueGradient to count down from "+str(fromColour)+" to "+str(toColour))
                break
            self.__SetHue(fromColour)
            self.__SetSat(1)
            step = 0
            while(self.hue >= toColour):
                #step up float values
                self.__StepDownHue()
                #write to vector
                self.__WriteToRobot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeatStep >= repeat-1):
                    break
                else:
                    repeatStep += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def SaturationGradient(self, delay=None, repeat=None, hold=None, setColour=None, toPercent=None, fromPercent=None):
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold
        setColour = 0 if setColour == None else setColour
        toPercent = 100 if toPercent == None else toPercent
        fromPercent = 0 if fromPercent == None else fromPercent

        if(isinstance(setColour,str)):
            setColour = self.__figureOutColour(setColour)
        if(isinstance(toPercent,int)):
            toPercent =  self.__figureOutPercentage(toPercent)
        if(isinstance(fromPercent,int)):
            fromPercent =  self.__figureOutPercentage(fromPercent)

        repeatStep = 0
        while True: #python do while loop
            print("Loop #"+str(repeatStep))
            #failsafe for bad inputs
            if (toPercent < fromPercent):
                print("You must use ReverseHueGradient to count down from "+str(fromPercent)+" to "+str(toPercent))
                break
            self.__SetHue(setColour)
            self.__SetSat(fromPercent)
            step = 0
            while(self.sat <= toPercent):
                #step up float values
                self.__StepUpSat()
                #write to vector
                self.__WriteToRobot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeatStep >= repeat-1):
                    break
                else:
                    repeatStep += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    def ReverseSaturationGradient(self, delay=None, repeat=None, hold=None, setColour=None, toPercent=None, fromPercent=None):
        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat
        hold = 0 if hold == None else hold
        setColour = 0 if setColour == None else setColour
        toPercent = 0 if toPercent == None else toPercent
        fromPercent = 100 if fromPercent == None else fromPercent

        if(isinstance(setColour,str)):
            setColour = self.__figureOutColour(setColour)
        if(isinstance(toPercent,int)):
            toPercent =  self.__figureOutPercentage(toPercent)
        if(isinstance(fromPercent,int)):
            fromPercent =  self.__figureOutPercentage(fromPercent)

        repeatStep = 0
        while True: #python do while loop
            print("Loop #"+str(repeatStep))
            #failsafe for bad inputs
            if (toPercent > fromPercent):
                print("You must use ReverseHueGradient to count up from "+str(fromPercent)+" to "+str(toPercent))
                break
            self.__SetHue(setColour)
            self.__SetSat(fromPercent)
            step = 0
            while(self.sat >= toPercent):
                #step up float values
                self.__StepDownSat()
                #write to vector
                self.__WriteToRobot()
                #ensure this loop is counted
                step += 1
                #check if delay and apply
                time.sleep(delay)

            #break the do while loop if conditions are met
            if(isinstance(repeat,bool)):
                if(repeat == False):
                    break
            else:
                if(repeatStep >= repeat-1):
                    break
                else:
                    repeatStep += 1

        print("Holding for:"+str(hold)+" seconds")
        time.sleep(hold) #keep the last colour for an amount in seconds

    #Private methods for in house use only
    #Setters for colour change
    def __SetHue(self, newHue):
        self.hue = newHue
        
    def __SetSat(self, newSat):
        self.sat = newSat

    #methods to step up and down for gradient effect in loops
    def __StepUpHue(self):
        if(self.hue > 1):
            print("Cannot step hue value higher than 1")
        else:
            self.hue += 0.01
    
    def __StepUpSat(self):
        if(self.sat > 1):
            print("Cannot step saturation value higher than 1")
        else:
            self.sat += 0.01

    def __StepDownHue(self):
        if(self.hue < 0):
            print("Cannot step hue value lower than 0")
        else:
            self.hue -= 0.01
    
    def __StepDownSat(self):
        if(self.sat < 0):
            print("Cannot step saturation value lower than 0")
        else:
            self.sat -= 0.01
    
    def __figureOutColour(self, colour, set=None):
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

    def __figureOutPercentage(self, percent):
        if(isinstance(percent,int)):
            #check valid percentage
            if(percent < 0 or percent > 100):
                print("Percentage must be an int between 0 and 100")
            
            return percent / 100

    #Write to robot what colours to display
    def __WriteToRobot(self):
        print("Displaying | Hue: "+str(self.hue) +" | Sat: "+str(self.sat))
        self.robot.behavior.set_eye_color(hue=self.hue, saturation=self.sat)

# Main utility #
class RainbowEyes(RainbowEyesCORE):
    SavedHue = 0
    SavedSat = 0

    #**  d^-^b SET EYE COLOURS d^-^b **#
    def MakeEyesWhite(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0)
        self._RainbowEyesCORE__SetSat(0)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesOrange(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.05)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesDarkYellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.1)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesYellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.15)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesLightYellow(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.2)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesGreen(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.3)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesLightGreen(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.4)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesCyan(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.5)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesLightBlue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.6)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesBlue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.65)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesDarkBlue(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.7)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesPurple(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.8)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesPink(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(0.9)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesRed(self):
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(1)
        self._RainbowEyesCORE__SetSat(1)
        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesCustom(self, writeSaved, hue=None, saturation=None):
        writeSaved = False if writeSaved == None else writeSaved
        hue = self.hue if hue == None else hue
        saturation = self.sat if saturation == None else saturation

        if(writeSaved):
            self.hue = self.SavedHue
            self.sat = self.SavedSat
        else:
            self.hue = hue
            self.sat = saturation

        self._RainbowEyesCORE__WriteToRobot()

    def MakeEyesRandom(self, justHue=None, rangeVal=None):
        justHue = True if justHue == None else justHue #set justHue to default or specified
        rangeVal = 100 if rangeVal == None else rangeVal #set rangeVal to default or specified
        #Make eyes change colour
        self._RainbowEyesCORE__SetHue(random.randrange(rangeVal)/100)
        if(justHue == False): self._RainbowEyesCORE__SetSat(random.randrange(rangeVal)/100)
        self._RainbowEyesCORE__WriteToRobot()
    
    def MakeEyesRainbow(self, delay=None, repeat=None):
        self._RainbowEyesCORE__SetSat(1)

        delay = 0 if delay == None else delay
        repeat = 0 if repeat == None else repeat

        self.HueGradient(delay,repeat)

    def MakeEyesPulse(self, delay=None, repeat=None, setColour=None, toPercent=None, fromPercent=None):
        repeat = 0 if repeat == None else repeat
        
        repeatStep = 0
        while True: #python do while loop
            print("Loop #"+str(repeatStep))
            #Make eyes pulse down
            self.ReverseSaturationGradient(delay,0,0,setColour,fromPercent,toPercent)
            #Make eyes pulse up
            self.SaturationGradient(delay,0,0,setColour,toPercent,fromPercent)

            #This is the end of the 'do while' loop
            if(isinstance(repeat, bool)):
                if(repeat == False):
                    break
            else:
                if(repeatStep >= repeat-1):
                    break
                else:
                    repeatStep += 1

    def SetSavedEyeColour(self, hue=None, sat=None):
        #if none specified, we set the current attributes into the saved
        hue = self.hue if hue == None else hue #set hue to default or specified
        sat = self.sat if sat == None else sat #set sat to default or specified

        self.SavedHue = hue
        self.SavedSat = sat
    
    def GetSavedEyeColour(self, whichReturn=None):
        whichReturn = "" if whichReturn == None else whichReturn #empty string means neither

        if(whichReturn.lower() == "hue"):
            return self.SavedHue
        elif(whichReturn.lower() == "saturation" or whichReturn.lower() == "sat"):
            return self.SavedSat
        else:
            #if we made it this far, well assume user wants both in array
            return [self.SavedHue, self.SavedSat]


