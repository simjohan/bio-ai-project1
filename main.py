from Population import Population
import filereader

population_size = 100

depot_spec, customers = filereader.read_file()

population = Population(population_size).generate_population(customers, depot_spec)

