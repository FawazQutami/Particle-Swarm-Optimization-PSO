# Metahourestics - Continuous optimization:
Given 6 functions 2 

I have chosen Particle Swarm Optimization (PSO), Algorithm to minimize the functions, because it has some parameters in which I can tweak to reach a reasonable solution 
 
# Particle Swarm Optimization (PSO):
"is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. 
It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according 
to simple mathematical formulae over the particle's position and velocity. Each particle's movement is influenced by its local best known position, 
but is also guided toward the best known positions in the search-space, which are updated as better positions, found by other particles. 
This is expected to move the swarm toward the best solutions." from: https://en.wikipedia.org/wiki/Particle_swarm_optimization


## Parameters that I have used in this simulation are:
	1. w (Inertia Weight): is used to control the velocity:
    2. The acceleration coefficients: c1 (cognitive) and c2 (social)
        * c1 (cognitive): expresses how much confidence a particle has in itself
        * c2 (social): expresses how much confidence a particle has in its neighbors
	3. number of particles - Swarm Size
    4. Max number of iterations - Stopping Tolerance
	

I have tried, through the below cases, to understand the principle of PSO and how it works, especially, when tweaking the parameters to achieve 
the best "global optimum". In addition, I've included the execution time in seconds for each function. 

## Study Cases: 

### Unimodal Functions (2):
#### Shifted Sphere Function:
		 ----------------------------------------------------------
		 Best Fitness - Cost       : 31423.124170769403
		 Function Name             : Shifted Sphere
		 Options                   : {'w': 0.75, 'c1': 1.6, 'c2': 1.6}
		 Max  Iterations           : 100
		 No of Particles           : 50
		 Dimension                 : 50
		 Execution Time in seconds : 24
		 ----------------------------------------------------------
![Shifted Sphere for Dimension = 50](/images/PSO_ShiftedSphere_50.png)
![Shifted Sphere for Dimension = 50](/images/PSO_ShiftedSphere_50.png)
		 
#### Shifted Schwefel’s Function:
		
		
		

### Multimodal Functions (4):
	1. Shifted Rosenbrock’s Function
	2. Shifted Rastrigin’s Function
	3. Shifted Griewank’s Function 
	4. Shifted Ackley’s Function
 
#### Shifted Sphere Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)

#### Shifted Schwefel’s Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)
#### Shifted Rosenbrock’s Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)
#### Shifted Rastrigin’s Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)
#### Shifted Griewank’s Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)
#### Shifted Ackley’s Function:
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)


	
![The fitness curves](/images/dj_fitnessCurve.png)

![Best Route](/images/dj_routeCurve.png)

	
# Code written in Python. 
This code favors readability and ease of understanding over speed and robustness 
and is meant to be used as either a research tool or a study guide for anyone 
intrested in learning about particle swarm optimization.  

To start the execution open main.py file and then run the program.
You need the below libraries:

	1. numpy
	2. matplotlib and basemap
 