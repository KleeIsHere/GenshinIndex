import numpy as np
from scipy.optimize import minimize
import pandas as pd
import csv

from Functions import KazuhaSkills
from Weapons import Weapon
from Characters import KazuhaCharacter

# USER INPUT
# we need to be able to input up to 4 different characters with 4 different weapons
inputParametersChar = ['Kazuha', '90']
inputParametersEnemy = ['Hilichurl','90']
inputWeaponName = 'BlackcliffPole'
inputWeaponNameList = "BlackcliffSlasher,PrototypeArchaic,Rainslasher,RoyalGreatsword,SerpentSpine,TheBell,WhiteBlind,SacrificialGreatsword,Snow-TombedStarsilver,FavoniusGreatsword,LithicBlade,SkywardPride,Wolf'sGravestone,TheUnforged,SongOfBrokenPines,SkyriderGreatsword"
inputArtifactMainStats = ["CritRate","Electro%", "ATK"]
inputArtifactSubStats = 0 # Call optimization function or get user input

# first initialize the character / weapon / skill classes [new class]
    # create instances of character objects and weapon objects
    # we will need instructions class to check all weapon conditionals at each point of damage calculation
    # we can probably use a function that just calls the other functions inside of a while loop?
    # for Optimization we can just use maxxed out values
kazuha = KazuhaCharacter.Kazuha(inputParametersChar)
weapon = Weapon.Weapon(inputWeaponName) # probably should have a new class for each weapon
kazuhaSkills = KazuhaSkills.KazuhaSkills(inputParametersChar[0])



# then choose to optimize substats or not [new class] including reaction damage
    # feed the values into the objective function or not



# use atk sequence to calculate instances of damage and complete damage sequence Monte Carlo it to get avg value

fight_duration = 90 # in seconds
frame = 0

# create character classes that keep track of their stats (basically like core in gsim)

while (frame < fight_duration):
    # select next skill from list
    # implement any buffs from the skill
    # implement any elemental application (keep track of ICD)
    # track ER
    # calculate average damage done by the skill
    # calculate reaction damage done by the skill
    # keep track of buffs on characters
    # increment the frame by 1 and check the states of everything
    # we are going to want to log the data as we go for further analysis
    x = 0

# IF we use a key logger, we can probably figure out a way to parse the data to figure out the attack sequence that
# is happening

# then export data for either one or more weapons [new class]

