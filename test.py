from Characters.Functions.DamageEngine import DamageEngine
from Characters.IttoCharacter import Itto
from Characters.Weapons.Whiteblind import Whiteblind
from Characters.Weapons.Whiteblind import Whiteblind

# initializing objects for engines, characters, and weapons
itto_obj = Itto(90, 10, 10, 10, 0)
attack_sequence = itto_obj.create_attack_sequence("N4")
print(attack_sequence)

whiteblind = Whiteblind(90, 1)

actionList = attack_sequence
team = [itto_obj]

engine = DamageEngine(actionList, team)

engine.runEngine("", team)

