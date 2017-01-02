import os

import matplotlib.pyplot as plt

from tsp import NearestNeighbourSolver
from tsp import NearestInsertionSolver
from util import euclidean_dist, read_data


RESULTS_DIR = 'results'
DATA_DIR = 'data'

def solve_and_plot():
	node_locations, node_distances = read_data(os.path.join(DATA_DIR, 'locations.txt'))

	node_labels = set(node_locations.keys())
	nn_solver = NearestNeighbourSolver(node_labels, node_distances)
	ni_solver = NearestInsertionSolver(node_labels, node_distances)
	nn_solution = nn_solver.run()
	ni_solution = ni_solver.run()

	fig = plt.figure()

	ax1 = fig.add_subplot(211)
	nn_solver.plot_solution(node_locations)
	ax2 = fig.add_subplot(212)
	ni_solver.plot_solution(node_locations)

	num_trials = 10
	nn_average_distance = 0
	ni_average_distance = 0
	for i in range(1,num_trials+1):
	    nn_solver.run()
	    nn_average_distance += nn_solver.get_total_distance()/num_trials

	    ni_solver.run()
	    ni_average_distance += ni_solver.get_total_distance()/num_trials

	print("Average distance for Nearest-Neighbour Solution: " + str(nn_average_distance))
	print("Average distance for Nearest-Insertion Solution: " + str(ni_average_distance))
	print("Lower bound for solution (minimum spanning tree weight): " + str(nn_solver.get_mst_weight()))

	fig.suptitle("Lower bound for solution (MST weight): " + str(nn_solver.get_mst_weight()))
	ax1.set_title('Nearest-Neighbour Solution (Avg. Distance: %f)' % nn_average_distance)
	ax2.set_title('Nearest-Insertion Solution (Avg. Distance: %f)' % ni_average_distance)
		
	plt.savefig(os.path.join(RESULTS_DIR, 'general-solution.png'), dpi=300)
	plt.show()

if __name__ == "__main__":
	solve_and_plot()

