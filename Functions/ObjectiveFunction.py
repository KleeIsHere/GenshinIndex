import pandas as pd

class ObjectiveFunction:


    def __init__(self, cumulative_skill_multiplier, number_of_reactions, character, weapon):

        self.cumulative_skill_multiplier = cumulative_skill_multiplier
        self.number_of_reactions = number_of_reactions
        self.character = character
        self.weapon = weapon

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

        reaction_Damage = 1

        attack_Term = (C2*(1+0.18+0.466+CharATKB+WeapATKB+0.0495*a)+311+f*16.5)
        crit_Term = (1+(0.311+WeapCR+CharCR+0.033*r)*(WeapCD+CharCD+0.066*d))
        skill_Damage = (-1)*C1*attack_Term*crit_Term


        return self.cumulative_skill_multiplier*skill_Damage + self.number_of_reactions*reaction_Damage