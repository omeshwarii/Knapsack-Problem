# Knapsack-Problem-Solver
 Contains a Python implementation of two approaches to solve the Knapsack 
## Approaches
Dynamic Programming.
Genetic Algorithm.

## Dynamic Programming Approach: 
solve problems by breaking them down into simpler subproblems and solving each subproblem only once, storing the solutions to avoid redundant computations.
- In the context of the Knapsack Problem, the solution is generated iteratively using a memorizable table to store the maximum value achievable at each capacity.
- Each cell represents the maximum value achievable with a certain capacity and a subset of items.


## Genetic Algorithm Approach
It is inspired by the process of natural selection and evolution, uses principles such as selection, crossover, and mutation to iteratively evolve a population of candidate solutions toward an optimal solution.
- The fitness of each chromosome is evaluated based on the total value of the selected items and their cumulative weight.
- Parents are selected from the population based on their fitness, typically using selection methods like roulette wheel selection or tournament selection.
- Crossover is performed between pairs of parent chromosomes to create offspring, inheriting traits from both parents.
- Mutation is applied to introduce randomness and explore new areas of the solution space, preventing premature convergence.
- Through successive generations, the population evolves, with fitter individuals increasingly dominating the population.
  
## Usage
1. Ensure you have Python installed on your system.
2. Run the provided Python scripts
3. Follow the prompts.
4. The script will output the maximum value achievable and the selected items along with their weights and values.
5. Execution time for each method will be displayed after completion.

## Dataset
- The items and their corresponding weights and values are read from the `items1.txt`, `items2.txt` and `items3.txt` files.

## Performance Comparison
- Both approaches aim to find the best solution to the Knapsack Problem but utilize different algorithms.
- The dynamic programming approach may be more suitable for smaller problem instances due to its efficient runtime complexity.
- The genetic algorithm approach offers the advantage of being able to handle larger problem instances and may provide near-optimal solutions in such cases.


