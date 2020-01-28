from random import randrange
from matplotlib import pyplot as plt
from Chromosome import Chromosome


def choose_best_fit(chromosomes):
    best_fit_value = 0
    best_fit_chromosome = None
    for chromosome in chromosomes:
        fitness = chromosome.fitness_function()
        if fitness > best_fit_value:
            best_fit_chromosome = chromosome
            best_fit_value = fitness
    return best_fit_chromosome


def crossover(x, y):
    crossover_partitioning = randrange(len(x.nodes))
    new_chromosome = Chromosome()
    new_chromosome.nodes[0:crossover_partitioning] = x.nodes[0:crossover_partitioning]
    new_chromosome.nodes[crossover_partitioning:] = y.nodes[crossover_partitioning:]
    return new_chromosome


class Population:
    chromosomes = []
    parents = []
    best_fitness_list = []
    average_fitness_list = []
    worst_fitness_list = []

    def __init__(self, population_size, number_of_generations):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        for i in range(population_size):
            self.chromosomes.append(Chromosome())

    def tornument_selection(self, tornument_size):
        number_of_tornuments = int(self.population_size/tornument_size)
        for i in range(number_of_tornuments):
            self.parents.append(self.select_parent(tornument_size))

    def select_parent(self, tornument_size):
        random_chromosomes = []
        for i in range(tornument_size):
            random_chromosomes.append(self.chromosomes[randrange(self.population_size)])
        return choose_best_fit(random_chromosomes)

    def new_population(self):
        self.chromosomes = []
        for i in range(self.population_size):
            x = self.parents[randrange(len(self.parents))]
            while True:
                y = self.parents[randrange(len(self.parents))]
                if x != y:
                    break
            self.chromosomes.append(crossover(x, y))

    def mutation(self, mutation_rate):
        number_of_genomes = len(self.chromosomes[0].nodes)
        mutated_genomes = int(self.population_size * number_of_genomes * mutation_rate)
        for i in range(mutated_genomes):
            random_chromosome = randrange(self.population_size)
            random_genome = randrange(number_of_genomes)
            random_color = randrange(4)
            self.chromosomes[random_chromosome].nodes[random_genome].color = random_color

    def evolution(self, tornument_size, mutation_rate):
        for i in range(self.number_of_generations):
            self.best_fitness_list.append(self.best_fitness_value())
            self.worst_fitness_list.append(self.worst_fitness_value())
            self.average_fitness_list.append(self.avg_fitness_value())
            self.tornument_selection(tornument_size)
            self.new_population()
            self.mutation(mutation_rate)
        self.plot()

    def best_fitness_value(self):
        best_fit_value = 0
        for chromosome in self.chromosomes:
            chromosome_fitness = chromosome.fitness_function()
            if chromosome_fitness > best_fit_value:
                best_fit_value = chromosome_fitness
        return best_fit_value

    def worst_fitness_value(self):
        worst_fit_value = 1000000
        for chromosome in self.chromosomes:
            chromosome_fitness = chromosome.fitness_function()
            if chromosome_fitness < worst_fit_value:
                worst_fit_value = chromosome_fitness
        return worst_fit_value

    def avg_fitness_value(self):
        sum_fit_value = 0
        for chromosome in self.chromosomes:
            sum_fit_value += chromosome.fitness_function()
        return sum_fit_value / self.population_size

    def plot(self):
        plt.plot(self.best_fitness_list, label="Best")
        plt.plot(self.worst_fitness_list, label="Worst")
        plt.plot(self.average_fitness_list, label="average")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend()
        plt.show()



