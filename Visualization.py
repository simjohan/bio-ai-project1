import matplotlib.pyplot as plt
import filereader
import numpy as np


def plot_solution(customers, depots, solution=None):
    fig = plt.figure()
    x_customers = customers[:, 1]
    y_customers = customers[:, 2]
    x_depots = depots[:, 2]
    y_depots = depots[:, 3]
    plt.plot(x_depots, y_depots, "bs")
    plt.plot(x_customers, y_customers, "ko")
    '''for depot_car, path in solution.solution_map.items():
        depot, car = depot_car
        x_path = list(map(lambda c: customers[c - 1][1], path))
        y_path = list(map(lambda c: customers[c - 1][2], path))
        x_path.insert(0, depots[depot - 1][1])
        x_path.append(depots[depot - 1][1])
        y_path.insert(0, depots[depot - 1][2])
        y_path.append(depots[depot - 1][2])
        plt.plot(x_path, y_path)'''

    plt.show()

depo_specs, customers = filereader.read_file()
plot_solution(customers, depo_specs)