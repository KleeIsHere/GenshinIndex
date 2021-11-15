

# the hit class will include any information about the hit that needs to be sent back to the character / weapon class 
# in order to check for buffs, (hit number, hit type, etc..)
class Hit:

    def __init__(self, name, type, number):
        self.name = name
        self.type = type
        self.number = number
