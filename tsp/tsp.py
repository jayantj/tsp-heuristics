from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import matplotlib.pyplot as plt


class TSPSolver(object):
    nodes = set()
    partial_tour = []
    distances = {}

    def __init__(self, nodes, distances):
        self.nodes = nodes
        self.distances = distances
        self.partial_tour = []

    def initialize(self):
        raise NotImplementedError

    def select(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def run(self):
        self.partial_tour = []
        self.initialize()
        while len(self.partial_tour) < len(self.nodes):
            selected = self.select()
            self.insert(selected)
        self.solution = self.partial_tour + [self.partial_tour[0]]
        return self.solution

    def get_traversed_nodes(self):
        return set(self.partial_tour)

    def get_remaining_nodes(self):
        return self.nodes - set(self.partial_tour)

    def get_nearest_remaining_node(self, given_node):
        remaining_nodes = self.get_remaining_nodes()
        node_distances = self.distances[given_node]
        remaining_distances =  {node:node_distances[node] for node in remaining_nodes}
        return min(remaining_distances, key=remaining_distances.get)

    def get_total_distance(self):
        total_distance = 0
        for i in range(len(self.solution)-1):
            current_node = self.solution[i]
            next_node = self.solution[i+1]
            total_distance += self.distances[current_node][next_node]
        return total_distance

    def get_mst_weight(self):
        num_nodes = len(self.nodes)
        distance_matrix = [[0 for j in range(num_nodes)] for i in range(num_nodes)]
        node_labels = self.distances.keys()
        node_labels_dict = dict(zip(range(num_nodes), node_labels))
        for (i, node_i) in node_labels_dict.iteritems():
            for (j, node_j) in node_labels_dict.iteritems():
                distance_matrix[i][j] = self.distances[node_i][node_j]
        X = csr_matrix(distance_matrix)
        mst = minimum_spanning_tree(X)
        return mst.sum()

    def plot_solution(self, locations):
        x_all = [locations[node][0] for node in self.solution]
        y_all = [locations[node][1] for node in self.solution]
        for i, (x, y) in enumerate(zip(x_all, y_all)):
            if i is 0 or i is len(self.solution) - 1:
                c = 'b'
                plt.annotate('start', xy=(x, y))
            elif i is len(self.solution) - 2:
                c = 'r'
                plt.annotate('end', xy=(x, y))
            else:
                c = 'g'
            plt.scatter(x, y, color=c,)
        plt.plot(x_all, y_all)
        plt.xlim(min(x_all) - 5, max(x_all) + 5)
        plt.ylim(min(y_all) - 5, max(y_all) + 5)

