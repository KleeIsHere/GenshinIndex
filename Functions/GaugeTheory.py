import pandas as pd
import matplotlib.pyplot as plt

class GaugeUnitTheory:

    def __init__(self, elementType, gaugeUnit, decayRate):
        self.elementType = elementType
        self.gaugeUnit = gaugeUnit
        self.decayRate = decayRate


    def applyElement(self, newElement, gaugeUnitValue):
        
        # check what happens to the element (reaction / extention)
        reactionCheck = self.checkRxn(self.elementType, newElement)

        # implement a switch function to switch through a dictionary to find which case we want to apply
        # with each of the functions update the corresponding variables in the object to reflect the elemental application


        pass

    def checkRxn(oldElement, newElement):

        if oldElement == 'None':
            'apply new element'

        elif oldElement == newElement:
            return 'extension'
        
        else:
            # switch through every reaction case
            E1 = oldElement
            E2 = newElement

            # if else construct to find the right combination

            # Multiplicative Reactions
            if (E1 == 'Pyro') and (E2 == 'Hydro'):
                return ('Multiplicative', ('Vaporize', 'Strong'))

            elif (E1 == 'Hydro') and (E2 == 'Pyro'):
                return ('Multiplicative', ('Vaporize', 'Weak'))

            elif (E1 == 'Cryo') and (E2 == 'Pyro'):
                return ('Multiplicative', ('Melt', 'Strong'))

            elif (E1 == 'Pyro') and (E2 == 'Cryo'):
                return ('Multiplicative', ('Melt', 'Weak'))

            # Transformative Reactions
            elif (E1 == 'Pyro') and (E2 == 'Electro'):
                return ('Transformative', 'Overload')

            elif (E1 == 'Electro') and (E2 == 'Pyro'):
                return ('Transformative', 'Overload')

            elif (E1 == 'Hydro') and (E2 == 'Electro'):
                return ('Transformative', 'Electrocharged')

            elif (E1 == 'Electro') and (E2 == 'Hydro'):
                return ('Transformative', 'Electrocharged')

            elif (E1 == 'Cryo') and (E2 == 'Electro'):
                return ('Transformative', 'Superconduct')

            elif (E1 == 'Electro') and (E2 == 'Cryo'):
                return ('Transformative', 'Superconduct')

