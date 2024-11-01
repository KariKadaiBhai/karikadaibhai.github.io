import numpy as np 

def fitness(individual, target): 
    return np.sum(individual == target) 

def crossover(parent1, parent2): 
    point = np.random.randint(1, len(parent1) - 1) 
    child1 = np.concatenate((parent1[:point], parent2[point:])) 
    child2 = np.concatenate((parent2[:point], parent1[point:])) 
    return child1, child2 

def mutate(individual, mutation_rate=0.01): 
    for i in range(len(individual)): 
        if np.random.rand() < mutation_rate: 
            individual[i] = 1 - individual[i]  # Flip bit 

def genetic_algorithm(target_str, population_size=100, generations=1000, 
                     mutation_rate=0.01): 
    target = np.array([int(bit) for bit in target_str])  # Convert target string to array 
    chromosome_length = len(target) 
    population = np.random.randint(2, size=(population_size, chromosome_length)) 
    
    for generation in range(generations): 
        fitness_scores = np.array([fitness(ind, target) for ind in population]) 
        
        if np.max(fitness_scores) == chromosome_length: 
            best_match_idx = np.argmax(fitness_scores) 
            print(f"Target reached in generation {generation}!") 
            return population[best_match_idx] 
        
        probabilities = fitness_scores / fitness_scores.sum() 
        selected_idx = np.random.choice(range(population_size), size=population_size // 2, 
                                         p=probabilities) 
        parents = population[selected_idx] 
        
        next_population = [] 
        for i in range(0, len(parents), 2): 
            parent1, parent2 = parents[i], parents[i + 1] 
            child1, child2 = crossover(parent1, parent2) 
            mutate(child1, mutation_rate) 
            mutate(child2, mutation_rate) 
            next_population.extend([child1, child2]) 
        
        population = np.array(next_population) 
    
    best_match_idx = np.argmax(fitness_scores) 
    print(f"Best match after {generations} generations:") 
    return population[best_match_idx] 

if __name__ == "__main__": 
    target = "1010101010"  # Target binary string 
    best_solution = genetic_algorithm(target) 
    print(f"Best solution found: {''.join(map(str, best_solution))}")
