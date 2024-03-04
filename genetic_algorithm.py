import random
import matplotlib.pyplot as plt
import time

start_time = time.time()


def generate_population(size):
	population = []
	for _ in range(size):
		genes = [0, 1]
		chromosome = []
		for _ in range(len(items)):
			chromosome.append(random.choice(genes))
		population.append(chromosome)
	
	return population


def calculate_fitness(chromosome):
	total_weight = 0
	total_value = 0
	for i in range(len(chromosome)):
		if chromosome[i] == 1:
			total_weight += items[i][0]
			total_value += items[i][1]
	if total_weight > max_weight:
		return 0
	else:
		return total_value


def select_chromosomes(population):
    fitness_values = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome)
        fitness_values.append(fitness)
    
    # Check if the sum of fitness values is zero
    sum_fitness = sum(fitness_values)
    if sum_fitness == 0:
        # If sum is zero, return chromosomes with equal probability
        return random.choices(population, k=2)
    
    # Normalize fitness values
    fitness_values = [float(fitness)/sum_fitness for fitness in fitness_values]
    
    # Select parent chromosomes based on normalized fitness values
    parent1 = random.choices(population, weights=fitness_values, k=1)[0]
    parent2 = random.choices(population, weights=fitness_values, k=1)[0]
    
    return parent1, parent2




def crossover(parent1, parent2):
	crossover_point = random.randint(0, len(items)-1)
	child1 = parent1[0:crossover_point] + parent2[crossover_point:]
	child2 = parent2[0:crossover_point] + parent1[crossover_point:]
	
	return child1, child2


def mutate(chromosome):
	mutation_point = random.randint(0, len(items)-1)
	if chromosome[mutation_point] == 0:
		chromosome[mutation_point] = 1
	else:
		chromosome[mutation_point] = 0
	
	return chromosome

# function to get the best chromosome from the population
def get_best(population):
	fitness_values = []
	for chromosome in population:
		fitness_values.append(calculate_fitness(chromosome))
#		print(calculate_fitness(chromosome))

	max_value = max(fitness_values)
#	print("best",max_value)
	max_index = fitness_values.index(max_value)
	return population[max_index]

# function to replace worst chromosome in the new population with the best chromosome in the old population
def elitist(population, new_population):
    best_chromosome = get_best(population)
    new_population.sort(key=lambda x: calculate_fitness(x))
    new_population[0] = best_chromosome
    return new_population



items = []


with open(r'C:\Users\omesh\Desktop\CW\spring_2023\EXP_SYS\Final_project\items3.txt', 'r') as file:
    for line in file:
        # split the line into weight and value and convert them to integers
        weight, value = map(int, line.strip().split())
        
        # add the weight and value as a new item to the items list
        items.append([weight, value])


print("Available items:\n", items)


max_weight = int(input("Enter the capacity of the knapsack:"))
population_size = 100
mutation_probability = 0.2
generations = 150

print("\nGenetic algorithm parameters:")
print("Max weight:", max_weight)
print("Population:", population_size)
print("Mutation probability:", mutation_probability)
print("Generations:", generations, "\n")


# generate a random population
population = generate_population(population_size)

 
best_fitness = 0

value_list = []  # just for plot of the value of a solution from each generation

# evolve the population for specified number of generations
for generation in range(generations):
    best = get_best(population)
    # select two chromosomes for crossover
    parent1, parent2 = select_chromosomes(population)

    # perform crossover to generate two new chromosomes
    child1, child2 = crossover(parent1, parent2)

    # perform mutation on the two new chromosomes
    if random.uniform(0, 1) < mutation_probability:
        child1 = mutate(child1)
    if random.uniform(0, 1) < mutation_probability:
        child2 = mutate(child2)

    # create a new population with the two new chromosomes
    new_population = [child1, child2] + population[2:]

    # add the best chromosome from the previous generation to the new population
    population = elitist(population, new_population)
    
    # print the maximum fitness value at each generation
    max_fitness = max([calculate_fitness(chromosome) for chromosome in population])
    print("Generation:", generation+1, "Max Fitness:", max_fitness)
    value_list.append(max_fitness)
print("\nMaximum fitness in each generation:",value_list)
print("Selected Items:",best)
# get the best chromosome from the population
best = get_best(population)


# get the weight and value of the best solution
total_weight = 0
total_value = 0
for i in range(len(best)):
    if best[i] == 1:
        total_weight += items[i][0]
        total_value += items[i][1]


print("\n\nThe best solution:")
print("\nKnapsack capacity:",max_weight)
print("Total weight in Knapsack:", total_weight)
print("Maximum value in Knapsack:", total_value)
print("SOLUTION GENERATED BY GENETIC ALGORITHM")

end_time = time.time()
elapsed_time = end_time - start_time

print("Time taken to execute the program:", elapsed_time, "seconds")




plt.plot(range(1, generations+1), value_list)
plt.title('Maximum Fitness Value at Each Generation')
plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.show()