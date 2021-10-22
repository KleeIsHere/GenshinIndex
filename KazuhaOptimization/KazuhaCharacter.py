import pandas

class Kazuha:

    #making 
    baseATK = 297
    attackBonus = 0
    critDamage = 0.5
    critRate = 0.05
    elementalBonus = 0
    elementalMastery = 115.2
    type = "Anemo"

    #
    def __init__(self, LVL, T1, T2, T3):
        self.LVL = LVL
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3

    def create_attack_string():
        x = 0
        #talentMultipliers = pull the multipliers out from table into a dictionary based on 
        # after identifying that we are in fact doing a normal attack then we need to determine the sequence of attacks
        # 3 Talents [Normal, Elemental, Burst] then we can number hits afterwards. also we can use A for all hits
        # pass in the atk sequnce string and then return multipliers with atk type classification