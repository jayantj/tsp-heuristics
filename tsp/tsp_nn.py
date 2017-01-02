import random

from tsp import TSPSolver


class NearestNeighbourSolver(TSPSolver):
    def initialize(self):
        starting_node = random.choice(tuple(self.nodes))
        self.partial_tour.append(starting_node)

    def select(self):
        current_node = self.partial_tour[-1]
        next_node = self.get_nearest_remaining_node(current_node)
        return next_node

    def insert(self, next_node):
        self.partial_tour.append(next_node)

