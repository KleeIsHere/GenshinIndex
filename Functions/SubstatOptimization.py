import numpy as np
from scipy.optimize import minimize
import pandas as pd

class OptimizeSubstats:

    

    def optimize(objective, x):

        stats_List = []
        rolls_List = []

        #x0 = [1,1,1,1,1,1]
        x0 = [0,0,0,18,0,0,0] # initialization for how many favourable rolls we want to have
        print(objective(x0))

        def constraint1(x) :
            return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]-20

        highBound = (0.0, 20.0)
        lowBound = (0.0, 15)
        bnds = (highBound,highBound,highBound,highBound,lowBound,lowBound, lowBound)
        constraint1 = {'type': 'eq', 'fun': constraint1}

        constraints = [constraint1]

        sol = minimize(objective, x0, method = 'SLSQP', bounds=bnds, constraints = constraints)

        def printStats(x) :

            a = x[0] #ATK%
            f = x[1] #flat atk
            z = x[2] #HP%
            h = x[3] #flat hp
            r = x[4] #crit rate
            d = x[5] #crit dmg
            e = x[6] #elemental mastery

            HPatkBonusES = (0.0506)*(BaseHP*(0.466+1+0.0495*z)+254*h+4780)

            '''
            # conditional for reaching max HP bonus cap
            if (HPatkBonusES > 4*C2) :
                HPatkBonusES = 4*C2
            '''

            ATK = C2 + C2*(1+CharATKB + WeapATKB + 0.0495*a)+311+f*16.5
            #+0.018*(BaseHP*(1+0.0495*z)+254*h+4780)
            HP = BaseHP*(1+0.0495*z)+254*h+4780
            CR = CharCR+WeapCR+0.033*r
            CD = CharCD+WeapCD+0.066*d
            EM = 280.2 + 3*187 + e 

            #print("Avg Optimized DMG = " + str(objective(sol.x)))
            #print("Total ATK = " + str(ATK))
            #print("Total HP = " + str(HP))
            #print("Total CR = " + str(CR))
            #print("Total CD = " + str(CD))

            stats_List.append((-1)*objective(sol.x))
            stats_List.append(ATK)
            stats_List.append(HP)
            stats_List.append(CR)
            stats_List.append(CD)
            stats_List.append(EM)
            
            rolls_List.append(a)
            rolls_List.append(f)
            rolls_List.append(z)
            rolls_List.append(h)
            rolls_List.append(r)
            rolls_List.append(d)
            rolls_List.append(e)

            #print(str((-1)*objective(sol.x)))
            #print(str(ATK))
            #print(str(HP))
            #print(str(CR))
            #print(str(CD))

    #x0 = [1,1,1,1,1,1]
    x0 = [0,0,0,18,0,0,0] # initialization
    print(objective(x0))

    highBound = (0.0, 20.0)
    lowBound = (0.0, 15)
    bnds = (highBound,highBound,highBound,highBound,lowBound,lowBound, lowBound)
    con1 = {'type': 'eq', 'fun': constraint1}

    cons = [con1]

    sol = minimize(objective, x0, method = 'SLSQP', bounds=bnds, constraints = cons)

    #print(sol)
    printStats(sol.x)

    print(stats_List)
    print(rolls_List)

    return stats_List, rolls_List

        print(stats_List)
        print(rolls_List)

        return stats_List, rolls_List