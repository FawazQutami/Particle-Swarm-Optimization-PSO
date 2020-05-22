"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics - Particle Swarm Optimization
-- File Name    :   main.py
-- *********************************************
"""

# load Packages
import datetime as dt

# load local packages
from eHandler import PrintException as EH
from PSO import PSO
from plotting import plotPSO
from setup import install_required_Packages


def runPSO(funcName, bounds, Dimension,particles, iterations, options):
    """
    Run PSO Function
    :param funcName: string
    :param bounds: list
    :param Dimension: int
    :param particles: int
    :param iterations: int
    :param options: dict
    :return: obj
    """
    try:
        # Total execution time

        s = PSO(funcName
                , bounds
                , particles
                , iterations
                , Dimension
                , options)
        return s

    except:
        EH()

def evaluations(funcName, bounds, Dimension):
    """
    Evaluation Function
    :param funcName: string
    :param bounds: list
    :param Dimension: int
    :return: None
    """
    try:

        # number of particles - Swarm Size
        particles = 100
        # Max number of iterations - Stopping Tolerance
        iterations = 500
        # for minimization problem
        # _initialFitness = float("inf")
        """ 
        w (Inertia Weight): is used to control the velocity:
        The acceleration coefficients: c1 (cognitive) and c2 (social)
        c1 (cognitive): expresses how much confidence a particle has in itself:
        c2 (social): expresses how much confidence a particle has in its neighbors
        """
        options = {'w': 0.85, 'c1': 1.0, 'c2': 1.5}

        print("\n Starting SPO ...")

        totalExecutionTime = 0
        solutions =[]

        for i in range(1, 26):
            start = dt.datetime.now()
            pso = runPSO(funcName, bounds, Dimension,particles, iterations, options)
            pso.run()
            solutions.append(pso)
            end = dt.datetime.now()
            totalExecutionTime += (end - start).seconds

        # Sort the resulted array:
        sortedList = sorted(solutions, key=lambda PSO: PSO.fitness)

        # Rotate through the results and choose the best one:
        print("\n-- Resulted Fitness:")
        for i, s in enumerate(sortedList):
            print(f"PSO {i + 1}, best fitness is {s.fitness}")

        print()
        bestPSO = sortedList[0]
        print("Best Solution: \n", bestPSO)

        print(f'Total Execution Time in seconds (repetitions: 25): {totalExecutionTime}')

        # Plot evaluation
        plotPSO(bestPSO.Evaluation, funcName, bestPSO.fitness)

    except:
        EH()


def main():
    """
    Main Function
    :return: None
    """
    try:
        while True:
            func_name, bounds = None, None
            flag = None
            D_range = [2, 50, 500]
            print("\n Choose a dimension from the following list: [2, 50, 500]")
            print("\t or press any other KEY to EXIT .....")
            Dimension = int(input("\n Enter a dimension --> "))

            if Dimension in D_range:
                flag = True
                if flag:
                    print(f"\n 1: Shifted Sphere"
                          f"\n 2: Shifted Schwefel"
                          f"\n 3: Shifted Rosenbrock"
                          f"\n 4: Shifted Rastrigin"
                          f"\n 5: Shifted Griewank"
                          f"\n 6: Shifted Ackley"
                          f"\n ... Press any key to EXIT")
                    choice = int(input("\n Enter a choice? "))
                    if choice == 1:
                        func_name = "Shifted Sphere"
                        bounds = [(-100, 100) for i in range(Dimension)]
                    elif choice == 2:
                        func_name = "Shifted Schwefel"
                        bounds = [(-100, 100) for i in range(Dimension)]
                    elif choice == 3:
                        func_name = "Shifted Rosenbrock"
                        bounds = [(-100, 100) for i in range(Dimension)]
                    elif choice == 4:
                        func_name = "Shifted Rastrigin"
                        bounds = [(-5, 5) for i in range(Dimension)]
                    elif choice == 5:
                        func_name = "Shifted Griewank"
                        bounds = [(-600, 600) for i in range(Dimension)]
                    elif choice == 6:
                        func_name = "Shifted Ackley"
                        bounds = [(-32, 32) for i in range(Dimension)]
                    else:
                        print("\n--------------------")
                        print("The program interrupted ... function not found!")
                        print("--------------------\n")
                        flag = False
                        break
                if flag:
                    evaluations(func_name, bounds, Dimension)
            else:
                print("\n----------------------------------------------------------")
                print("Required dimension is not in the list [2, 50, 100, 500]!")
                print("----------------------------------------------------------\n")
                break

    except:
        EH()


if __name__ == "__main__":
    try:
        # Install Required packages
        install_required_Packages()
        main()

    except:
        EH()