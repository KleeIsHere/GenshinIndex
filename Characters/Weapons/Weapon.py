import pandas as pd

class Weapon:

    weapon_df = pd.read_excel(r'C:\Users\Michael\Desktop\Genshin_Repository\GenshinOptimization-main\GenshinOptimization-main\KazuhaOptimization\DataTables\KazuhaTables.xlsx', sheet_name='WeapLVL90', index_col=0)

    def __init__(self, name):

        self.name = name

        self.baseATK = self.weapon_df.loc[name, "Base ATK"]
        self.attackBonus = self.weapon_df.loc[name, "ATK%"]
        self.critRate = self.weapon_df.loc[name, "CR"]
        self.critDamage = self.weapon_df.loc[name, "CD"]
        self.elementalBonus = self.weapon_df.loc[name, "EB"]