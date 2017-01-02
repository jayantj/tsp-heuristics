import random

from tsp import TSPSolver


class NearestInsertionSolver(TSPSolver):
    def initialize(self):
        starting_node = random.choice(tuple(self.nodes))
        self.partial_tour.append(starting_node)
        next_node = self.get_nearest_remaining_node(starting_node)
        self.partial_tour.append(next_node)

    def select(self):
        remaining_nodes = self.get_remaining_nodes()
        return random.choice(tuple(remaining_nodes))

    def get_insertion_metric(self, node, insert_after, insert_before):
        metric = self.distances[node][insert_after] + self.distances[node][insert_before] - self.distances[insert_after][insert_before]
        return metric

    def insert(self, node):
        insert_index = 1
        metrics = []
        minimized_metric = self.get_insertion_metric(node, self.partial_tour[0], self.partial_tour[1])
        for i in range(0,len(self.partial_tour)-1):
            metric = self.get_insertion_metric(node, self.partial_tour[i], self.partial_tour[i+1])
            metrics.append(metric)
            if metric < minimized_metric:
                minimized_metric = metric
                insert_index = i + 1
        self.partial_tour.insert(insert_index, node)

