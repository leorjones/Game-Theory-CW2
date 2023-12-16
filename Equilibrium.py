def scorefinder(total, Acurrent, Amultiplier):
    #Takes total players, proportion who choose the bulb (A), and the resistance multiplyer of the bulb
    # Returns the scores for the two options
    Bcurrent = total-Acurrent
    Bmultiplier = 1/(Amultiplier*(Acurrent**2))
    Ascore = Acurrent*Amultiplier
    Bscore = Bcurrent*Bmultiplier
    #print("B multiplier is ",Bmultiplier)
    return Ascore, Bscore

import numpy as np
import matplotlib.pyplot as plt

def equilibrium(total, Acurrent, Amultiplier):
    Ascore, Bscore = scorefinder(total, Acurrent, Amultiplier)
    Bcurrent = total - Acurrent
    Acurrents = [Acurrent]
    Bcurrents = [Bcurrent]
    Ascores = [Ascore]
    Bscores = [Bscore]
    Resistance = 1/((Acurrent**2)*Amultiplier)
    Resistances = [Resistance]
    iterations = 1
    while abs(Ascore-Bscore) > 0.05 and iterations < 3000:
        if Ascore > Bscore:
            Acurrent = Acurrent - min(0.005,abs(((Ascore-Bscore)/Ascore)))*Acurrent
        elif Bscore > Ascore:
            Acurrent = Acurrent + min(0.003,abs(((Ascore-Bscore)/Ascore)))*Acurrent
        else:
            iterations = 10000
        
        #print(Acurrent)
        Bcurrent = total - Acurrent
        Acurrents.append(Acurrent)
        Bcurrents.append(Bcurrent)
        Ascore, Bscore = scorefinder(total, Acurrent, Amultiplier)
        Ascores.append(Ascore)
        Bscores.append(Bscore)
        Resistance = 1/((Acurrent**2)*Amultiplier)
        Resistances.append(Resistance)
        iterations += 1
    
    total = len(Ascores)
    xaxis = list(np.linspace(1, total, total))
                 
    L=400
    print(total)
    plt.title("Player Scores over Iterations")
    plt.plot(xaxis[L:], Ascores[L:])
    plt.plot(xaxis[L:], Bscores[L:])
    solutionlist = [7.895]*(total-L)
    #plt.plot(xaxis[L:], solutionlist)
    plt.axhline(y = 7.895, color = 'b', xmax= 784, linestyle = ':') 
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend(['$S_B$', '$S_L$', 'True Voltage']) 
    plt.show()
    
    plt.title("Players choosing L over Iterations")
    plt.plot(xaxis[L:], Bcurrents[L:])
    plt.xlabel("Iterations")
    plt.ylabel(r"$I_L$")
    plt.axhline(y = 98.421, color = 'b', xmax = 784, linestyle = ':') 
    plt.legend(['$I_L$','True Current']) 
    plt.ylim(88, 100)
    plt.show()
    
    plt.title("$R_L$ over Iterations")
    plt.plot(xaxis[L:], Resistances[L:])
    solutionlist = [7.895]*(total-L)
    plt.xlabel("Iterations")
    plt.ylabel("$R_L$")
    plt.axhline(y = 0.080217, color = 'b',xmax= 784, linestyle = ':') 
    plt.legend(['$R_L$','True Resistance']) 
    plt.ylim(0, 0.09)
    plt.show()

equilibrium(100,80,5)