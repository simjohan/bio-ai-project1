from typing import List
import numpy as np


def read_file() -> List:
    file = open("testing_data/data_files/p01", "r")

    # read first line
    mnt = np.array(list(map(lambda f: int(f), file.readline().split())))

    # read depo max duration and max load
    depo_specs = []
    for i in range(int(mnt[-1])):
        depo_specs.append(list(map(lambda f: int(f), file.readline().split())))

    # read customer information
    customer_info = []
    for i in range(int(mnt[1])):
        customer = list(map(lambda f: int(f), file.readline().split()))
        customer = customer[0:5]
        customer_info.append(customer)

    # read and add depo coordinates. Only keep coordinates, discard rest.
    for i in range(len(depo_specs)):
        depo_coordinate = file.readline().strip().split()
        #depo_coordinate = (int(depo_coordinate[1]), int(depo_coordinate[2]))

        depo_specs[i].append(int(depo_coordinate[1]))
        depo_specs[i].append(int(depo_coordinate[2]))

    return np.array(depo_specs), np.array(customer_info)


print(read_file())