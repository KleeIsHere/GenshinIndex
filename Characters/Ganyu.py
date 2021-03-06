from os import name
import pandas
import sys

from Functions import SkillSearch
#from Functions import SkillSearch

class Ganyu:

    # Itto's base stats (later we will pull these based off his lvl from a table) LVL 90 right now
    name = "Itto"
    baseATK = 335
    baseDEF = 630
    attackBonus = 0
    critDamage = 0.884
    critRate = 0.05
    elementalBonus = 0
    elementalMastery = 0

    # stacks will just be an array of tuplesindicating their start frames and end frames
    passiveUndividedHeart = []
    type = "Cryo"

    frame_Data = {
        '1_Hit':20,
        '2_Hit':25,
        '3_Hit':30,
        'Charge_ATK':60,
        'dash':20
    }

    util = SkillSearch.SkillSearch("Ganyu")

    # constructor (used to initialize and instance of the Itto class)
    def __init__(self, LVL, T1, T2, T3, Con):
        self.LVL = LVL
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.Con = Con
    
    # defining different skill combos as lists of strings in a dictionary
    # each skill corresponds to a separate hit and will be treated as such in the damage calculation
    def search_Skill_Combos(self, combo_name):

        combos = {

            "N1": ["1_Hit", "Dash"],
            "N4": ["1_Hit", "2_Hit", "3_Hit", "4_Hit"],
            "C" : ["Arataki_Kesagiri_Combo_Slash", "Arataki_Kesagiri_Final_Slash"],
            "N1+E" : ["1_Hit", "EPressDMG"]

        }

        #print (type(combos[combo_name]))
        return combos[combo_name]



    # talentMultipliers = pull the multipliers out from table into a dictionary based on combo name
    def create_attack_sequence(self, combo_name):

        names_list = [self.name]

        #creating list of talent Levels
        talent_LVL_List = [self.T1, self.T2, self.T3]
    
        # creating a list of the skill names
        skill_name_List = self.search_Skill_Combos(combo_name)

        # we need to classify each skill to its Talent to query the right table with skill search
        skill_talent_List = self.util.classify_Skill(skill_name_List)

        # passing talent / LVL / name lists into the skillSearch class to get the Skill Multipliers
        skill_multipliers = self.util.getSkillMultipliers(skill_talent_List, talent_LVL_List)

        # correcting charged attacks based on superlativeStacks adding the charged attack at the beginning of each list
        if skill_talent_List[0][0] == 'Arataki_Kesagiri_Combo_Slash':
            skill_multipliers.insert(0, skill_multipliers[0]*len(self.superlativeStrength))
            names_list = names_list*len(skill_multipliers)
            skill_talent_List.insert(0, skill_talent_List[0]*len(self.superlativeStrength))
        
        else:
            names_list = names_list*len(skill_multipliers)

        return names_list, skill_multipliers, skill_talent_List

        # 3 Talents [Normal, Elemental, Burst] then we can number hits afterwards. also we can use A for all hits
        # pass in the atk sequnce string and then return multipliers with atk type classification

    def initiate_skill(self, skillMultiplier, skillinfo, frame):
        skill_multiplier = skillMultiplier
        skill_name = skillinfo[0]
        skill_type = skillinfo[1]
        start_frame = frame
        end_frame = start_frame + self.frame_Data[skill_name]

    def checkSuperlativeStrength(self, skill, frame):

        if skill == ("2_Hit"):
            self.superlativeStrength.append(SS_Stack(frame))
        elif skill == ("4_Hit"):
            self.superlativeStrength.append(SS_Stack(frame))
            self.superlativeStrength.append(SS_Stack(frame))
        else:
            for stack in self.superlativeStrength:
                if stack.endFrame == frame:
                    self.superlativeStrength.remove(stack)

    def checkChargedAttack(self, skill, frame):

        #removes the first 
        if skill == "Arataki_Kesagiri_Combo_Slash":
            del self.superlativeStrength[0]
    
        elif skill == "Arataki_Kesagiri_Final_Slash":
            del self.superlativeStrength[0]


    def runChecks(self, skill, frame):
        self.checkSuperlativeStrength(skill, frame)
        self.checkChargedAttack(skill, frame)

    def getStats(self):
        stats = {
            "name" : self.name,
            "baseATK" : self.baseATK,
            "baseDEF" : self.baseDEF,
            "attackBonus" : self.attackBonus,
            "critRate" : self.critRate,
            "elementalBonu" : self.elementalBonus,
            "elementalMastery" : self.elementalMastery,
            "NormalAttackCounter" : self.NormalAttackCounter,
        }
        return stats
        
class UndividedHeartPassive:

    def __init__(self, frame):
        self.startFrame = frame
        self.endFrame = self.startFrame + 60*5 
        


test = Itto(90, 10, 10, 10, 0)
print(test.create_attack_sequence('N4'))
print(test.create_attack_sequence('C'))

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