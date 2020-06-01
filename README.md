# Metahourestics - Continuous Cases
I have chosen Particle Swarm Optimization (PSO) algorithm, to minimize the functions, because it has some parameters 
which I can tweak to reach a reasonable solution.
 
# Particle Swarm Optimization (PSO)
"is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. 
It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according 
to simple mathematical formulae over the particle's position and velocity. Each particle's movement is influenced by its local best known position, 
but is also guided toward the best known positions in the search-space, which are updated as better positions, found by other particles. 
This is expected to move the swarm toward the best solutions." from:[PSO wikipedia](https://en.wikipedia.org/wiki/Particle_swarm_optimization)

## Parameters that I have used in this simulation are:
	1. w (Inertia Weight): is used to control the velocity:
    2. The acceleration coefficients: c1 (cognitive) and c2 (social)
        * c1 (cognitive): expresses how much confidence a particle has in itself
        * c2 (social): expresses how much confidence a particle has in its neighbors
	3. number of particles - Swarm Size
    4. Max number of iterations - Stopping Tolerance
	
## Study Cases 
I have tried, through the below cases, to understand the principle of PSO and how it works, especially, when tweaking the parameters to achieve 
the best "global optimum".
For the sake of illustration, I have used the same parameters for all functions.
In addition, I have recorded the total execution time in seconds for each function - after 25 repetitions, to produce the best solution possible.

### Unimodal Functions (2 functions):

#### Shifted Sphere Function:
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : 23406.54663258832
	 Function Name             : Shifted Sphere
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 3
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 77
![Shifted Sphere for Dimension = 50](/images/PSO_ShiftedSphere_50.png)
	
	Best Solution: 
    ----------------------------------------------------------
	 Best Fitness - Cost       : 1854383.698877279
	 Function Name             : Shifted Sphere
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 33
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 808
![Shifted Sphere for Dimension = 500](/images/PSO_ShiftedSphere_500.png)
		 
#### Shifted Schwefel’s Function:
	Best Solution: 
	----------------------------------------------------------
	 Best Fitness - Cost       : -350.0
	 Function Name             : Shifted Schwefel
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 4
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 100
![Shifted Schwefel for Dimension = 50](/images/PSO_ShiftedSchwefel_50.png)
	
	Best Solution: 
	 ----------------------------------------------------------
	 Best Fitness - Cost       : -284.2050102477849
	 Function Name             : Shifted Schwefel
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 44
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 1128
![Shifted Schwefel for Dimension = 500](/images/PSO_ShiftedSchwefel_500.png)

### Multimodal Functions (4 functions):

#### Shifted Rosenbrock’s Function:
	Best Solution: 
	----------------------------------------------------------
	 Best Fitness - Cost       : 12962830594.928587
	 Function Name             : Shifted Rosenbrock
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 4
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 101
![Shifted Rosenbrock for Dimension = 50](/images/PSO_ShiftedRosenbrock_50.png)
	
	Best Solution: 
 	----------------------------------------------------------
	 Best Fitness - Cost       : 1495758943556.2048
	 Function Name             : Shifted Rosenbrock
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 46
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 1178
 ![Shifted Rosenbrock for Dimension = 500](/images/PSO_ShiftedRosenbrock_500.png)
 
#### Shifted Rastrigin’s Function:
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : 61.65953346130971
	 Function Name             : Shifted Rastrigin
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 7
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 178
![Shifted Rastrigin for Dimension = 50](/images/PSO_ShiftedRastrigin_50.png)
	
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : 9764.689230057094
	 Function Name             : Shifted Rastrigin
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 72
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 1788
![Shifted Rastrigin for Dimension = 500](/images/PSO_ShiftedRastrigin_500.png)

#### Shifted Griewank’s Function:
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : 261.9756391505077
	 Function Name             : Shifted Griewank
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 9
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 227
![Shifted Griewank for Dimension = 50](/images/PSO_ShiftedGriewank_50.png)

	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : 16329.931567348067
	 Function Name             : Shifted Griewank
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 92
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 2321
![Shifted Griewank for Dimension = 500](/images/PSO_ShiftedGriewank_500.png)

#### Shifted Ackley’s Function:
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : -121.02136935446579
	 Function Name             : Shifted Ackley
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 50
	 Execution Time in seconds : 5
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 129
![Shifted Ackley for Dimension = 50](/images/PSO_ShiftedAckley_50.png)
	
	Best Solution:
	----------------------------------------------------------
	 Best Fitness - Cost       : -118.8606492874814
	 Function Name             : Shifted Ackley
	 Options                   : {'w': 0.85, 'c1': 1.0, 'c2': 1.5}
	 Max  Iterations           : 500
	 No of Particles           : 100
	 Dimension                 : 500
	 Execution Time in seconds : 55
	----------------------------------------------------------
	Total Execution Time in seconds (repetitions: 25): 1350
![Shifted Ackley for Dimension = 500](/images/PSO_ShiftedAckley_500.png)
	
# Code written in Python 
This code is meant to be used as either a research tool or a study guide for anyone interested in learning about Particle Swarm Optimization. 

To start the execution open main.py file and then run the program.
You need the below libraries:

	1. numpy
	2. matplotlib
 
