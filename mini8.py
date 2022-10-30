import numpy as np
import random
import operator

def crossover(a, b):
    node = []
    nodeA = []

    nA = int(random.random()* len(a))
    nB = int(random.random()* len(b))
    
    start_gene = min(nA, nB)
    end_gene = max(nA,nB)
    
    for i in range(start_gene,end_gene):
        nodeA.append(a[i])
        
    node = nodeA + [item for item in b if item not in nodeA]
  
    return node

def mutate(route, prob):
    route = np.array(route)
    
    for i in range(len(route)):
        if(random.random() < prob):
            new_node = np.random.randint(0, len(route))
            
            temp_route = route[i]
            new_route = route[new_node]

            route[new_node] = temp_route
            route[i] = new_route
    
    return route

def selection(pop, size):
    selection = []
    result = []

    for i in pop:
        result.append(i[0])

    for i in range(0, size):
        selection.append(result[i])
    
    return selection

def best_route(population, cities):
    results = {}

    for i in range(0, len(population)):
        score = 0
        for j in range(1, len(population[i])):
            k = int(population[i][j-1])
            l = int(population[i][j])

            results[i] = score + np.sqrt((cities[k][0] - cities[l][0])**2 + (cities[k][1] - cities[l][1])**2)

    return sorted(results.items(), key = operator.itemgetter(1), reverse = False)

def ga(city_map):
    pop = []
    initial_dist = []
    population = []
    cities = len(city_map)
    
    for i in range(0, 1000):
        pop = set(np.arange(cities, dtype=int))
        route = list(random.sample(pop, cities))
        
        population.append(route)
    
    initial_dist.append(best_route(population, city_map)[0][1])
    
    print("City route " + str(population[0]))
    print("Route distance " + str(initial_dist[0]))

    for i in range(0, 100):
        noderen = []
        result = selection(best_route(population, city_map), 50)
        nodes = []
        next_gen = []

        for i in range(0, len(result)):
            nodes.append(population[result[i]])
            
        for i in range(len(nodes)-1):
            noderen.append(crossover(nodes[i], nodes[i+1]))

        for i in noderen:
            new_mutation = mutate(i, 0.05)
            next_gen.append(new_mutation)

        initial_dist.append(best_route(next_gen, city_map)[0][1])
    
    rank = best_route(next_gen,city_map)[0]
    
    print("Best Route " + str(next_gen[rank[0]]))
    print("New distance " + str(rank[0]))


city_map = []

for i in range(0, 25):
    x = int(random.random() * 200)
    y = int(random.random() * 200)
    city_map.append((x,y))

ga(city_map)

