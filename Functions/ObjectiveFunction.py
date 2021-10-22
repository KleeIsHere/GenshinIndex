import pandas as pd

# need to pass the character values here in order to determine the damage
# need to split the objective function into skill damage (based off of multipliers) [includes melt / vape]
# and also need to split into transformative reaction damage, add modularity for number of enemies
# here we need a 
class ObjectiveFunction:

    # Currently initilizing the object of the ObjectiveFunction with the stats of the character and weapon, and number of reactions
    def __init__(self, cumulative_skill_multiplier, number_of_reactions, character, weapon):

        self.cumulative_skill_multiplier = cumulative_skill_multiplier
        self.number_of_reactions = number_of_reactions
        self.character = character
        self.weapon = weapon

    # Function for the objective function, this gets passed an array x of variables that are to be optimized (substats in this case)
    def objective(self, x):

        attackPercent = x[0] #ATK%
        flatAttack = x[1] #flat atk
        hpPercent = x[2] #HP%
        flatHP = x[3] #flat hp
        critRate = x[4] #crit rate
        critDamage = x[5] #crit dmg
        elementalMastery = x[6] #elemental mastery

        C1 = (1+EB)*(SM)*((100+CharLVL)/(100 + character.LVL + 100 + EnemyLVL)) *(1-EnemyRes) #calculating C1
        C2 = TotalBaseATK # setting C2 to the total base attack

        # reaction damage formula missing here set to 1 for testing purposes
        reaction_Damage = 1

        # damage formula, might want to rewrite this, also there are hard coded values for the main stats and others
        # that should be added in a modular fashion from input and also from the character class
        attack_Term = (C2*(1+0.18+0.466+CharATKB+WeapATKB+0.0495*a)+311+f*16.5)
        crit_Term = (1+(0.311+WeapCR+CharCR+0.033*r)*(WeapCD+CharCD+0.066*d))
        skill_Damage = (-1)*C1*attack_Term*crit_Term

        # if we make the objective function general then we can call it to calculate damage for each frame 
        # based on whatever is changing (buffs timing effect) 
        # we will need a main loop that takes in instructions and excecutes actions in order based on the input
        # we can also approach this by writing the functions out for each action and then just writing a python script for the logic
        # this would give us the most power to make the sim do exactly what we want it to and would work well for small scale analysis

        return self.cumulative_skill_multiplier*skill_Damage + self.number_of_reactions*reaction_Damage

    # Write out the Optimization function here to optimize the objective function
    # This way we can call the Optimize function first in order to determine the optimized substats
    # then we can call the objective function and evaluate the damage for each instance


