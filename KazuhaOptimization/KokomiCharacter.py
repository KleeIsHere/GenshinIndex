import pandas

class KokomiInfo:

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

    def determine_Stats():
        x = 0
        # here we shall define all of their conditional effects
        # off to the main fuction that will apply any external buffs
        # we will populate a 

    def normal_ATK(name):

        # use name to pull SM from KokomiSkills sheet
        # can be either single value or a list for all three normals
        # name will be the name of the type of attack or attack string
        
        SM = 0

        # determine any character buffs
        buff_Value = 0
        buff_Type = 0

        # determine any team buffs, and if TRUE then pass back to main function in some format
        team_Buff_Value = 0
        team_Buff_Type = 0

        return SM, buff_Value, buff_Type, team_Buff_Value, team_Buff_Type

    def charged_ATK(name):

        # use name to pull SM from KokomiSkills sheet
        SM = 0

        # determine any character buffs
        buff_Value = 0
        buff_Type = 0

        # determine any team buffs, and if TRUE then pass back to main function in some format
        team_Buff_Value = 0
        team_Buff_Type = 0

        return SM, buff_Value, buff_Type, team_Buff_Value, team_Buff_Type

    def normal_ATK(name):

        # use name to pull SM from KokomiSkills sheet
        SM = 0

        # determine any character buffs
        buff_Value = 0
        buff_Type = 0

        # determine any team buffs, and if TRUE then pass back to main function in some format
        team_Buff_Value = 0
        team_Buff_Type = 0

        return SM, buff_Value, buff_Type, team_Buff_Value, team_Buff_Type

    def create_attack_string():
        x = 0
        #talentMultipliers = pull the multipliers out from table into a dictionary based on 
        # after identifying that we are in fact doing a normal attack then we need to determine the sequence of attacks
        # 3 Talents [Normal, Elemental, Burst] then we can number hits afterwards. also we can use A for all hits
        # pass in the atk sequnce string and then return multipliers with atk type classification