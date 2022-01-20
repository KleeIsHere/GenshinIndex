# translator will translate the codename of the skill / skill string and pull the list of multipliers from the 
# character's skills class

class SkillTranslator:

    def __init__(self, name):
        self.name = name
    
    # lets store the list of skills in a dictionary, the key is the codename and then the contents will be the case names
    # EX:
    skill_List = {'NA3': ['1_Hit', '2_Hit', '3_Hit_a', '3-Hit_b']}

    # function will bring in the codename and return the contents 