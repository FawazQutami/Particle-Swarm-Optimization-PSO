"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Plotting Functions
-- File Name    :   plotting.py
-- *********************************************
"""

# load Packages

import matplotlib.pyplot as plt
from eHandler import PrintException as EH


def plotPSO(Evaluation, funcName, fitness):
    try:
        #print(len(iterations))
        plt.figure(figsize=(10, 5))
        plt.grid('on')
        plt.rc('axes', axisbelow=True)
        plt.plot(Evaluation, "r-", label=funcName, lw=2)
        plt.xlabel("Iterations")
        plt.ylabel("Cost")
        plt.title('PSO - ' + funcName)
        #plt.annotate('local max', xy=(index, fitness_gbp_Position),arrowprops=dict(facecolor='black', shrink=0.05))
        best = [ i for i, ev in enumerate(Evaluation) if ev ==fitness]
        for i in best:
            plt.scatter(i, fitness, 50
                    , marker='o', facecolors='c', edgecolors='k',
                    linewidths=1)
        plt.legend()
        plt.show()

    except:
        EH()
