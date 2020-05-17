"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics - Continuous Cases
-- File Name    :   costFunctions.py
-- *********************************************
"""

# load Packages
import math
import numpy as np
import pandas as pd

# load local packages
from eHandler import PrintException as EH


# Exterior penalty multipliers
f_bias = np.array([-450.0 , -450.0 , 390.0 , -330.0 , -180.0 , -140.0])


def values(fileName):
    """
    Values
    :param fileName: string
    :return: list[float]
    """
    try:
        _value = []

        with open(fileName, "r") as f:
            for line in f:
                stripped_line = line.split(",")
                for it in stripped_line:
                    if it != '\n':
                        _value.append(float(it))
        #print(len(_value))
        return _value
    except:
        EH()


# shifts:
sphere = values("data/sphere.txt")
schwefel = values("data/schwefel.txt")
rosenbrock = values("data/rosenbrock.txt")
rastrigin = values("data/rastrigin.txt")
griewank = values("data/griewank.txt")
ackley = values("data/ackley.txt")


def costFunction(funcName, dim, x):
    """"""

    try:

        if dim > 1000:
            dim = 1000

        if funcName == "Shifted Sphere":
            return Shifted_Sphere(dim, x)
        elif funcName == "Shifted Schwefel" :
            return Schwefel_Problem(dim, x)
        elif funcName == "Shifted Rosenbrock":
            return Shifted_Rosenbrock(dim, x)
        elif funcName == "Shifted Rastrigin":
            return Shifted_Rastrigin(dim, x)
        elif funcName == "Shifted Griewank":
            return Shifted_Griewank(dim, x)
        elif funcName == "Shifted Ackley":
            return Shifted_Ackley(dim, x)
        else:
             print("Error : Function number out of range\n")
             exit()
    except:
        EH()


# Uni-modal Functions: ------------------------------------------------
def Shifted_Sphere(dim , x):
    """"""
    try:
        F = 0   # objective function
        #print(len(sphere))
        for i in range(dim):
            F += math.pow(x[i] - sphere[i],  2)
        #print(F + f_bias[0])
        return F + f_bias[0]

    except:
        EH()


def Schwefel_Problem(dim , x):
    """"""
    try:
        F = np.abs(x[0])
        for i in range(1, dim):
            z = x[i] - schwefel[i]
            F = max(F, np.abs(z))

        return F + f_bias[1]
    except:
        EH()


# Multi-modal Functions:
def Shifted_Rosenbrock(dim , x):
    """"""
    try:
        z = []
        F = 0
        for i in range(dim):
            z.append(x[i] - rosenbrock[i] + 1)

        for i in range(dim-1):
            F = F + 100 *(math.pow(
                (math.pow(z[i], 2) - z[i + 1]), 2)) \
                + math.pow((z[i] - 1), 2)

        return F + f_bias[2]
    except:
        EH()


def Shifted_Rastrigin(dim , x):
    """"""
    try:
        F = 0
        for i in range(dim):
            z = x[i] - rastrigin[i]
            F = F + (math.pow(z, 2) - 10 * np.cos(2 * np.pi * z) + 10)

        return F + f_bias[3]
    except:
        EH()


def Shifted_Griewank(dim , x):
    """"""
    try:
        F1 = 0
        F2 = 1
        for i in range(dim):
            z = x[i] - griewank[i]
            F1 += ( math.pow(z, 2) / 4000)
            F2 *= ( np.cos(z / np.sqrt(i + 1)))

        F = F1 - F2 + 1 + f_bias[4]

        return F
    except:
        EH()


def Shifted_Ackley(dim, x):
    """"""
    try:
        Sum1 = 0
        Sum2 = 0
        for i in range(dim):
            z = x[i] - ackley[i]
            Sum1 += math.pow(z , 2)
            Sum2 += np.cos(2 * np.pi * z)

        F = -20 * np.exp(-0.2 * np.sqrt(Sum1 / dim)) \
            - np.exp(Sum2 / dim) + 20 + np.e + f_bias[5]

        return F
    except:
        EH()