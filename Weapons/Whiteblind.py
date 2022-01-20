#from Characters.Weapons.Whiteblind import Stack

class Whiteblind:

    baseATK = 510
    secondaryStat = (0.517, "DEF%")
    hit_stack = 0
    stack_timer = 0

    stacks = []

    # scaling for the refinement passive
    refinement_passive_scaling = {
        1:0.06,
        2:0.075,
        3:0.09,
        4:0.105,
        5:0.12
    }

    def __init__(self, LVL, refinement):
        self.LVL = LVL
        self.refinement = refinement
    
    # Passive effect on hit normal or charged attacks increase ATK and DEF by 12% (R5)

    def passive_stacks(self, attack_info, frame):

        for stack in self.stacks:
                if stack.final_frame < frame:
                    self.stacks.remove(stack)

        if(attack_info[1] == "NormalATK"):

            new_stack = Stack(attack_info[0], frame)
            self.stacks.append(new_stack)

            self.hit_stack = self.hit_stack + 1
            buff = self.hit_stack*self.refinement_passive_scaling[self.refinement]
            atk_buff = buff
            def_buff = buff
            
        return atk_buff, def_buff, self.stack_timer


    def pass_buffs(self, attack_info, frame):

        buffs = {
        'atk_buff' : self.passive_stacks(attack_info, frame)[0],
        'def_buff' : self.passive_stacks(attack_info, frame)[1] + self.secondaryStat,
        'target' : 'whiteblind_user'
        }

        return buffs

# we can make the stacks a queue 
# if hit (normal/charged) add into queue
# once timer ends take stack out of queue
class Stack:

    def __init__(self, atk_type, initial_frame):
        self.atk_type = atk_type
        self.initial_frame = initial_frame
        self.final_frame = initial_frame + 6*60
