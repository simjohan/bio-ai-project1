from typing import List
from Chromosome import Chromosome
import copy


class Population:

    def __init__(self, population_size: int, depots, customers):
        self.population = []
        self.population_size = population_size
        self.total_load = 0
        self.depots = depots
        self.customers = customers


    def generate_population(self, customers: List, depot_spec: List) -> List:
        # generates a list of solutions
        for i in range(self.population_size):
            copy_depots = copy.deepcopy(self.depots)



    def crossover(self):
        # find best in population
        # select lucky few
        pass
