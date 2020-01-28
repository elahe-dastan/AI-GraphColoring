import math
import random
from random import randrange
import copy as cp
from Chromosome import Chromosome


class SimulatedAnnealing:
    def __init__(self):
        self.current = Chromosome()

    def execute(self, schedule, initial_temperature, alpha):
        for t in range(10000):
            temperature = schedule(initial_temperature, alpha, t)
            if temperature != 0:
                next = self.random_chromosome_successor()
                fitness_differentiate = next.fitness_function() - self.current.fitness_function()
                if fitness_differentiate > 0:
                    self.current = next
                else:
                    probability = math.e ** (fitness_differentiate / temperature)
                    if random.uniform(0, 1) < probability:
                        self.current = next
        print(self.current.fitness_function())

    def random_chromosome_successor(self):
        random_color = randrange(4)
        random_genome = randrange(len(self.current.nodes))
        next_chromosome = cp.deepcopy(self.current)
        next_chromosome.nodes[random_genome].color = random_color
        return next_chromosome

    def first_schedule(self, initial_temperature, alpha, time):
        if alpha < 0.8 or alpha > 0.9:
            print("alpha should be between 0.8 and 0.9")
            return 0
        time_temperature = initial_temperature * (alpha ** time)
        return time_temperature

    def second_schedule(self, initial_temperature, alpha, time):
        if alpha <= 1:
            print("alpha should be greater than 1")
            return 0
        time_temperature = initial_temperature / (1 + alpha * math.log2(1 + time))
        return time_temperature

    def third_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature / (1 + alpha * time)
        return time_temperature

    def fourth_schedule(self, initial_temperature, alpha, time):
        time_temperature = initial_temperature / (1 + alpha * (time ** 2))
        return time_temperature