import math
import random
from random import randrange
import copy as cp

from Chromosome import Chromosome


class SimulatedAnnealing:
    def __init__(self):
        self.current = Chromosome()

    def execute(self, schedule):
        for t in range(10000):
            temperature = schedule(1, 1, t)
            if temperature == 0:
                return self.current
            next = self.random_chromosome_successor()
            fitness_differentiate = next.fitness_function() - self.current.fitness_function()
            if fitness_differentiate < 0:
                self.current = next
            probability = math.e ** (fitness_differentiate/temperature)
            if random.uniform(0, 1) < probability:
                self.current = next

        print()

    def random_chromosome_successor(self):
        random_color = randrange(4)
        random_genome = randrange(len(self.current.nodes))
        next_chromosome = cp.deepcopy(self.current)
        next_chromosome.nodes[random_genome].color = random_color
        return next_chromosome

    def first_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature * (alpha ** time)
        return time_temperature

    def second_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature / (1 + alpha * math.log2(1 + time))
        return time_temperature

    def third_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature / (1 + alpha * time)
        return time_temperature

    def fourth_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature / (1 + alpha * (time ** 2))
        return time_temperature