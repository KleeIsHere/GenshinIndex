import pandas as pd


class GaugeUnitEngine:

    def __init__(self, actionList, team):
        self.actionList = actionList
        self.team = team

    def runEngine(self, endConditions):
        frame = 0
        conditions = True

        # use team in order to initialize character objects
        # from character objects pull out values needed for the conditions / damage calculation / etc...

        currentAction = self.actionList[0]

        # while loop checks that all conditions are true. If any are false then it exits the loop
        while conditions:

            # for each frame we need to check a number of things
            #   - were any elements applied or reacted?
            #   - determined inputs for damage calculation
            #   - tracking the status of the applied element
            # we will use the GaugeTracking class to check the states of the applied element
            # gauge needs to decay as a function of its Unit

            

        

            # We need to call an update function to update the values of everything that changes by each frame
            '''
            if (CharacterObject.getCurrentActionDuration(currentAction) = 0):
                currentAction = self.nextAction(currentAction)
            
            '''
            

            # Also update the frame number by 1
            self.frame = self.frame+1

            # Final step is to check that no termination conditions are met
            conditions = self.checkConditions(endConditions)

    def nextAction(self, currentAction):
        currentIndex = self.actionList.index(currentAction)
        newIndex = currentIndex  + 1
        return self.actionList[newIndex]


    def checkConditions(*conditions):
       # create a switch statement with dictionary mapping containing all of the conditions that we'd want to consider for termination
       # put the conditions inside of each character's object
       # pass some string to call a condition check
       # ex: HuTao Eskill active? -> checks Hu Tao's Eskill duration and returns TRUE / FALSE
       # Inside of the main class 
       pass




