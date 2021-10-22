import pandas as pd

class KazuhaSkills:

    normal_ATK_dataframe = pd.read_excel(r'C:\Users\Michael\Desktop\Genshin_Repository\GenshinOptimization-main\GenshinOptimization-main\KazuhaOptimization\DataTables\KazuhaTables.xlsx', sheet_name='NormalATK', index_col=0)
    e_skill_dataframe = pd.read_excel(r'C:\Users\Michael\Desktop\Genshin_Repository\GenshinOptimization-main\GenshinOptimization-main\KazuhaOptimization\DataTables\KazuhaTables.xlsx', sheet_name='ESkill', index_col=0)
    burst_dataframe = pd.read_excel(r'C:\Users\Michael\Desktop\Genshin_Repository\GenshinOptimization-main\GenshinOptimization-main\KazuhaOptimization\DataTables\KazuhaTables.xlsx', sheet_name='ULT', index_col=0)

    def __init__(self, name):
        self.name = name

    # function receives info on which type of attack is being done, and then selects the value of skill multiplier from the corresponding dataframe 
    # from the attack name [case] and the skill level
    def getValue(self, dataframe_name, case, skill_level):

        value = 0

        if dataframe_name == "Normal":
            value  = self.normal_ATK_dataframe.loc[case, skill_level]

        elif dataframe_name == "E Skill":
            value  = self.normal_ATK_dataframe.loc[case, skill_level]

        elif dataframe_name == "Burst":
            value  = self.normal_ATK_dataframe.loc[case, skill_level]

        return value

test = KazuhaSkills("test")

#print(test.getValue("Normal", "1_Hit", 1))
#print(test.e_skill_dataframe)
#print(test.burst_dataframe)