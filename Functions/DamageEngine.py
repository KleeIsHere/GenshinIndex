import pandas as pd

class DamageEngine:

    teamDict = {}

    # action list can be an attack sequence or series of attack sequences
    def __init__(self, actionList, team):
        self.characterList = actionList[0]
        self.skillMultipliers = actionList[1]
        self.skillDetails = actionList[2]

        # set team into a dictionary so that we can access each obj with the name of the character
        for member in team:
            self.teamDict[member.name] = member

        self.frame = 0
        self.finalFrame = 60

    def runEngine(self, endConditions, team):
        conditions = True

        print(self.skillMultipliers)
        print(self.characterList)
        print(self.skillDetails)

        # use team in order to initialize character objects
        # from character objects pull out values needed for the conditions / damage calculation / etc...

        #currentAction = self.actionList[0]

        # while loop checks that all conditions are true. If any are false then it exits the loop
        while conditions:

            # for each frame we need to check a number of things
            #   - were any elements applied or reacted?
            #   - determined inputs for damage calculation
            #   - tracking the status of the applied element
            # we will use the GaugeTracking class to check the states of the applied element
            # gauge needs to decay as a function of its Unit

            index = 0

            for name in self.characterList:

                
                # access the object of the character 
                character = self.teamDict[name]



                # calculate damage for the attack
                # pass damage stats into damage function
                

                # check for character buffs
                # check for team buffs (bennet / resonance)
                # check for weapon buffs
                # character.runChecks()
                damage = CalculateDamage(character.getStats(), self.skillMultipliers[index])

                print(damage.calculate_DMG())
                #print(self.frame)

                index =  index + 1

            for member in team:
                pass
                # check the conditionals and buffs and status of each skill on each frame
                # the length of each skill and the duration need to be saved inside of the character object


            # check which skills / buffs are active

            # for now we can just do damage calculation
            #damage_formula_output = 

        

            # We need to call an update function to update the values of everything that changes by each frame
            '''
            if (CharacterObject.getCurrentActionDuration(currentAction) = 0):
                currentAction = self.nextAction(currentAction)
            
            '''
            

            # Also update the frame number by 1
            self.frame = self.frame+1

            # Final step is to check that no termination conditions are met
            #conditions = self.checkConditions(endConditions)
            
            if self.frame >= self.finalFrame:
                conditions = False

    def nextAction(self, currentAction):
        currentIndex = self.actionList.index(currentAction)
        newIndex = currentIndex + 1
        return self.actionList[newIndex]


    def checkConditions(*conditions):
       # create a switch statement with dictionary mapping containing all of the conditions that we'd want to consider for termination
       # put the conditions inside of each character's object
       # pass some string to call a condition check
       # ex: HuTao Eskill active? -> checks Hu Tao's Eskill duration and returns TRUE / FALSE
       # Inside of the main class
       pass

class CalculateDamage:

    def __init__(self, stats, skillMultipier):

        self.stats = stats
        self.skillMultiplier = skillMultipier
    
    def calculate_DMG(self):
        
        print("SM: " + str(self.skillMultiplier))
        DMG =  self.stats["baseATK"] * self.skillMultiplier

        return DMG

# the conditionals class will have a bunch of methods that initialize each of the conditionals
# the conditionals will be defined in terms of a bunch of local variables within an instance of the class
# other methods will be used to check the conditionals

class Conditionals:

    
    # time conditionals defined by frame data

    startFrame = 0
    currentFrame = startFrame # will be updated by methods after creation of the object
    endFrame  = 60*60*3 # end frame is default set to a 3min simulation, time from Spiral Abyss 36 stars

    def __init__(self):
        pass

    # energy recharge conditionals: defined by the ER status of each character
    characterMaxEnergy = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    characterCurrentEnergy = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    # Basically the energy will change based on the input of whatever skills are used
    # we will write functions here to check conditionally for the state of the ER
    # we will not include stat analysis




    # enemy status conditionals: 

    # reaction conditionals:



    # time conditional functions

    def updateFrame(self, increment):
        self.currentFrame = self.currentFrame + increment

    def setEndFrame(self, newEndFrame):
        self.endFrame = newEndFrame

    def checkEndSim(self):
        
        reachedEnd = False
        
        if self.currentFrame > self.endFrame:
            reachedEnd = True
        
        return reachedEnd

    # energy Conditional Functions

    def characterBurstReady (self, charIndex):

        burstReady = False
        
        if self.characterCurrentEnergy >= self.characterMaxEnergy:
            burstReady = True

        return burstReady

    # skill cooldown conditionals 
    # will look at a the value of whether a skill is on or off cooldown

