import math


class Gene:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def euclidean_distance(self, gene2):
        return math.sqrt((self.x - gene2.x)**2 + (self.y - gene2.y)**2)


class Customer(Gene):
    def __init__(self, i: int, x: int, y: int, d: int, q: int):
        Gene.__init__(self, x, y)
        self.i = i
        self.d = d
        self.q = q


class Depo(Gene):
    def __init__(self, i: int, x: int, y: int, max_duration: int, max_load: int, max_num_vehicles: int):
        Gene.__init__(self, x, y)
        self.i = i
        self.max_load = max_load
        self.max_num_vehicles = max_num_vehicles

        self.max_duration = max_duration
        if max_duration == 0:
            self.max_duration = float('inf')




g1 = Gene(2, 2)
g2 = Gene(4, 5)
c1 = Customer(0, 3, 9, 0, 0)
d1 = Depo(20, 44, 0, 0)

print(c1.euclidean_distance(d1))

print(g1.euclidean_distance(c1))
