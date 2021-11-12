import pandas
import sys
from ...Functions import SkillSearch

class Itto:

    # Itto's base stats (later we will pull these based off his lvl from a table) LVL 90 right now
    baseATK = 191
    baseDEF = 930
    attackBonus = 0
    critDamage = 0.5
    critRate = 0.242
    elementalBonus = 0
    elementalMastery = 0
    NormalAttackCounter = 1
    type = "Geo"

    # constructor (used to initialize and instance of the Itto class)
    def __init__(self, LVL, T1, T2, T3, Con):
        self.LVL = LVL
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.Con = Con
    
    # defining different skill combos as lists of strings in a dictionary
    # each skill corresponds to a separate hit and will be treated as such in the damage calculation
    def search_Skill_Combos(combo_name):

        combos = {

            "N1": ["1_Hit"],
            "N1C" : ["1_Hit", "Arataki_Kesagiri_Combo_Slash", "Arataki_Kesagiri_Final_Slash"],
            "N2C" : ["1_Hit", "2_Hit", "Arataki_Kesagiri_Combo_Slash", "Arataki_Kesagiri_Final_Slash"]

        }

        return combos[combo_name]



    def create_attack_sequence(self, combo_name):

        x = 0
        #talentMultipliers = pull the multipliers out from table into a dictionary based on combo name
    
        skill_List = self.search_Skill_Combos(combo_name)

        # we need to classify each skill if they are a normal / Eskill / ULT to query the right table with skill search



        # 3 Talents [Normal, Elemental, Burst] then we can number hits afterwards. also we can use A for all hits
        # pass in the atk sequnce string and then return multipliers with atk type classification

#test = Itto(90, 10, 10, 10, 0)
#util = SkillSearch.SkillSearch("Itto")


#util.classify_Skill(test.create_attack_sequence("N2C"))


    # Normal Attack Cycle
    # Function that will increase the normal attack counter and just pull the correct multiplier for it
    
    # Specific Normal Attack
    # Pass a number to specify which normal attack that we want

    # Charged Attacks

    # Plunging Attacks

    # Burst (just buffs him and changes his dmg type)
    # This will pass the buffs

    # Passive Talents
    # Arataki Ichiban - Gets an Atk Speed increase 10% on charged attacks
    # Bloodline - Arataki Kasegiri DMG is increased by 35% of DEF
    # Woodchuck - omit
    # Warrior's Burden - E skill or sprint activation will not reset his attack skill combo

    # 