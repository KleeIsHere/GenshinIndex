import pandas as pd
from pathlib import Path

class SkillSearch:

    def __init__(self, char_name):
        self.char_name = char_name

        # accessing the correct file
        self.character_Table_String =  char_name + "Tables.xlsx"
        self.data_folder = Path("../GenshinIndex/Characters/DataTables/")
        self.full_path = self.data_folder / self.character_Table_String

        # create three dataframes that hold the data for each skill
        self.normal_ATK_dataframe = pd.read_excel(self.full_path, sheet_name='NormalATK', index_col=0, engine='openpyxl')
        self.e_skill_dataframe = pd.read_excel(self.full_path, sheet_name='ESkill', index_col=0, engine='openpyxl')
        self.burst_dataframe = pd.read_excel(self.full_path, sheet_name='ULT', index_col=0, engine='openpyxl')

    # function receives info on which type of attack is being done, and then selects the value of skill multiplier from the corresponding dataframe 
    # from the attack name [case] and the skill level
    # returns a list of multipliers
    def getSkillMultipliers(self, skill_list, talent_LVL_list):

        index = 0
        skillMultiplierList = []
        level = 0

        # looping through the talent types list
        for skill in skill_list:

            if(skill[1] == "NormalATK"):
                table = self.normal_ATK_dataframe
                level = talent_LVL_list[0]
            elif(skill[1] == "ESkill"):
                table = self.e_skill_dataframe
                level = talent_LVL_list[1]
            elif(skill[1] == "ULT"):
                table = self.burst_dataframe
                level = talent_LVL_list[2]
            else:
                print("One of the skill types is invalid")
                return None

            # appending the corresponding multiplier searching with the right index skill_names and skill_levels
            skillMultiplierList.append(table.loc[skill_list[index][0], level])
            index = index + 1

        return skillMultiplierList

    # defining a classifier function here because this is where the tables exist
    def classify_Skill(self, skill_String):

        #print(skill_String)

        # pull in the first column of each dataframe as a list
        normal_ATK_names = self.normal_ATK_dataframe.index.values
        e_skill_names = self.e_skill_dataframe.index.values
        burst_names = self.burst_dataframe.index.values

        skill_String_Types = []

        for skill_index in range(len(skill_String)):

            if skill_String[skill_index] in normal_ATK_names:

                classified_skill = (skill_String[skill_index], "NormalATK")
                skill_String_Types.append(classified_skill)

            elif skill_String[skill_index] in e_skill_names:

                classified_skill = (skill_String[skill_index], "ESkill")
                skill_String_Types.append(classified_skill)

            elif skill_String[skill_index] in burst_names:

                classified_skill = (skill_String[skill_index], "ULT")
                skill_String_Types.append(classified_skill)

        #print(skill_String_Types)
        return skill_String_Types

        # check each list to see if the skill falls underneath it

test = SkillSearch("Itto")

skillList = "1_Hit", "Arataki_Kesagiri_Combo_Slash"
#print(test.getSkillMultipliers("NormalATK", 10, "1_Hit", "Arataki_Kesagiri_Combo_Slash"))
#print(test.e_skill_dataframe)
#print(test.burst_dataframe)