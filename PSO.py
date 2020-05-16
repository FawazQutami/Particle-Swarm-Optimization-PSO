"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics - Continuous Cases
-- File Name    :   PSO.py
-- *********************************************
"""

# load Packages
import random
import datetime as dt

# load local packages
from costFunctions import costFunction
from eHandler import PrintException as EH


class Particle:
    """ Particles Class """
    def __init__(self
                 ,_bounds
                 ,Dimension
                 ,options
                 ):
        """
        
        :param _bounds: list
        :param Dimension: int 
        :param _inertia: float
        :param _cognitive: float
        :param _social: float
        """
        try:
            # Particle position
            self.position = []
            # Particle velocity
            self.velocity = []
            # Best position of the particle - which is the best individual position of that particle
            self.bestPosition = []
            # Initial cost function value of the best particle position
            self.fitness = float("inf")
            # Cost function value of the particle position
            self.candidate = float("inf")
            # Dimension
            self.Dimension = Dimension
            # (Inertia Weight) is used to control the velocity
            # c1 (cognitive) expresses how much confidence a particle has in itself
            # c2 (social) expresses how much confidence a particle has in its neighbors
            self.options = options

            for i in range(Dimension):
                # # Initialize the particle's position with a uniformly distributed random vector:
                self.position.append(
                    random.uniform(_bounds[i][0], _bounds[i][1]))
                # Initialize the particle's velocity:
                self.velocity.append(random.uniform(-1, 1))
        except :EH()

    def evaluate(self, fName):
        """
        Evaluate the Fitness
        :param fname: string
        :return: None
        """
        try:
            #print(self.position)
            self.candidate = costFunction(fName, self.Dimension, self.position)
            if self.candidate < self.fitness:
                # Update the best position
                self.bestPosition = self.position
                # Update the fitness of the best position
                self.fitness = self.candidate
        except: EH()

    def updateVelocity(self, gbp_Position):
        """
        Update the particle's velocity
        :param gbp_Position: list
        :return:None
        """
        try:
            for i in range(self.Dimension):
                # Random vectors:
                # rand₁ and rand₂ are random numbers where 0 ≤ rand ≤ 1 and
                # they control the influence of each value: Social and cognitive
                rand1 = random.random()
                rand2 = random.random()

                cognitiveVelocity = self.options['c1'] * rand1 \
                                     * (self.bestPosition[i] - self.position[i])
                socialVelocity = self.options['c2'] * rand2 \
                                  * (gbp_Position[i] - self.position[i])
                self.velocity[i] = self.options['w'] \
                                   * self.velocity[i] \
                                   + cognitiveVelocity \
                                   + socialVelocity
        except: EH()

    def updatePosition(self, _bounds):
        """
        Update the particle's position
        :param _bounds: list
        :return:None
        """
        try:
            for i in range(self.Dimension):
                self.position[i] = self.position[i] + self.velocity[i]

                # check and repair to satisfy the upper bounds
                if self.position[i] > _bounds[i][1]:
                    self.position[i] = _bounds[i][1]
                # check and repair to satisfy the lower bounds
                if self.position[i] < _bounds[i][0]:
                    self.position[i] = _bounds[i][0]
        except:
            EH()


class PSO():
    """ Particle Swarm Optimization """
    def __init__(self
                 ,funcName
                 ,bound
                 ,particleSize
                 ,iterations
                 ,Dimension
                 ,options
                 ):
        """

        :param funcName: string
        :param bound: list
        :param particleSize: int
        :param iterations: int
        :param Dimension: int
        :param options: dict
        """
        try:
            # Fitness global best particle position:
            self.fitness = float("inf")
            # Global Best particle position - list
            self.gbp_Position = []
            # Swarm particles
            self.swarmParticles = []
            # Iterations
            self.iterations = iterations
            self.iterationsList = []
            # Cost function Number
            self.funcName = funcName
            # Particle Size
            self.particleSize = particleSize
            # Bounds
            self.bounds = bound
            # Function execution time
            self.executionTime = 0
            #
            #self.Dimension = Dimension
            # Initialize the particle's position with a uniformly distributed random vector:
            for i in range(particleSize):
                sp = Particle(bound, Dimension, options)
                self.swarmParticles.append(sp)

            self.Evaluation = []
            #self.target = 1
            #self.target_error =  10e-8
            self.options = options
            self.Dimension = Dimension
        except:
            EH()

    def __repr__(self):
        """
        Print format
        :return: String
        """
        try:
            printStatement = (
                f"\n ----------------------------------------------------------"
                f"\n Best Fitness - Cost       : {self.fitness}"
                f"\n Function Name             : {self.funcName}"
                f"\n Options                   : {self.options}"     
                f"\n Max  Iterations           : {self.iterations}"
                f"\n No of Particles           : {self.particleSize}"
                f"\n Dimension                 : {self.Dimension}"
                f"\n Execution Time in seconds : {self.executionTime}"
                f"\n ----------------------------------------------------------"
                #f"\n Optimal solution:         : {self.gbp_Position}\n"
                #f"\n Fitness Evaluation List   : {self.Evaluation}\n"
                )
            return printStatement

        except:
            EH()

    def run(self):
        """
        Run PSO - Search Space
        :return: None
        """
        try:
            start = dt.datetime.now()
            # for each iteration:
            for i in range(self.iterations):
                self.iterationsList.append(self.iterations)
                # for each particle:
                for j in range(self.particleSize):
                    # Update the swarm's best known position:
                    self.swarmParticles[j].evaluate(self.funcName)
                    if self.swarmParticles[j].candidate < self.fitness:
                        self.gbp_Position = \
                            list(self.swarmParticles[j].position)
                        self.fitness = \
                            float(self.swarmParticles[j].candidate)

                for j in range(self.particleSize):
                    # Update the particle's velocity:
                    self.swarmParticles[j].updateVelocity(self.gbp_Position)
                    # Update the particle's position:
                    self.swarmParticles[j].updatePosition(self.bounds)

                # Finally, record the best fitness if it is smaller than swarm error:
                self.Evaluation.append(self.fitness)

            end = dt.datetime.now()
            self.executionTime = (end - start).seconds
        except:EH()