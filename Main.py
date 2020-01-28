from Population import Population
from SimulatedAnnealing import SimulatedAnnealing

# population = Population(10, 50)
# population.evolution(2, 0.01)
#
# population = Population(10, 500)
# population.evolution(2, 0.01)
#
# population = Population(10, 5000)
# population.evolution(2, 0.01)
#
# population = Population(100, 50)
# population.evolution(2, 0.01)
#
# population = Population(100, 50)
# population.evolution(5, 0.01)
#
# population = Population(100, 50)
# population.evolution(10, 0.01)
#
# population = Population(1000, 50)
# population.evolution(2, 0.01)
#
# population = Population(1000, 50)
# population.evolution(5, 0.01)
#
# population = Population(1000, 50)
# population.evolution(10, 0.01)
#
# population = Population(10, 50)
# population.evolution(2, 0.02)
#
# population = Population(10, 50)
# population.evolution(2, 0.05)
#
# population = Population(10, 50)
# population.evolution(2, 0)
#
# population = Population(10, 50)
# population.evolution(2, 1)


simulated_annealing_algorithm = SimulatedAnnealing()

simulated_annealing_algorithm.execute(simulated_annealing_algorithm.first_schedule, 50, 0.85)

simulated_annealing_algorithm.execute(simulated_annealing_algorithm.second_schedule, 50, 40)

simulated_annealing_algorithm.execute(simulated_annealing_algorithm.third_schedule, 50, 0.85)

simulated_annealing_algorithm.execute(simulated_annealing_algorithm.fourth_schedule, 50, 0.85)