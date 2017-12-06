import csv
import argparse
import random
import math
import operator

DEFAULT_FILENAME = '../data/iris.csv'
DEFAULT_SPLIT_RATIO = 0.66
DEFAULT_K = 3

def restricted_float(x):
	x = float(x)
	if x < 0.0 or x > 1.0:
		raise argparse.ArgumentTypeError("{} not in range [0.0, 1.0]".format(x))
	return x

def positive_int(x):
	x = int(x)
	if x <= 0:
		raise argparse.ArgumentTypeError("{} is not a positive integer".format(x))
	return x

def retrieve_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--original", help="use R.Fisher original data", action='store_true')
	parser.add_argument("-r", "--ratio", help="change split ratio of the data (default={})".format(DEFAULT_SPLIT_RATIO), action="store", default=DEFAULT_SPLIT_RATIO, type=restricted_float)
	parser.add_argument("-k", "--neighbours", help="change number of neighbours used in kNN (default={})".format(DEFAULT_K), action="store" ,default=DEFAULT_K, type=positive_int)
	return parser.parse_args()
	
def get_filename(args):
	return '../data/iris-original.csv' if args.original else DEFAULT_FILENAME

def get_split_ratio(args):
	return args.ratio

def get_k(args):
	return args.neighbours	

def print_rows(rows):
	separator = ', '
	for row in rows:
		print(separator.join(row))

def get_rows(filename):
	with open(filename, 'rt') as csvfile:	
		dataset = csv.reader(csvfile)
		datasetlist = list(dataset)
		return datasetlist[1:]

def split_data(data, split_ratio):
	training_set = []
	test_set = []
	for x in range(len(data)):
		for y in range(4):
			data[x][y] = float(data[x][y])
		if random.random() < split_ratio:
			training_set.append(data[x])
		else:
			test_set.append(data[x])	
	return training_set, test_set

def euclidean_distance(instance1, instance2):
	distance = 0
	for x in range(len(instance1)):
		distance += pow((instance1[x]-instance2[x]), 2)
	return math.sqrt(distance)

def calculate_distance(instance1, instance2, length):
	return euclidean_distance(instance1[:length], instance2[:length])

def get_neighbour_instance(distances, x):
	return distances[x][0]

def get_neighbours(training_set, test_instance, k):
	distances = []
	length = len(test_instance)-1
	for x in range(len(training_set)):
		distance = calculate_distance(training_set[x], test_instance, length)
		distances.append((training_set[x], distance))
	distances.sort(key=operator.itemgetter(1))
	neighbours = []
	for x in range(k):
		neighbour = get_neighbour_instance(distances, x)
		neighbours.append(neighbour)
	return neighbours

def get_class(instance):
	return instance[-1]

def get_result(training_set, test_instance, k):
	neighbours = get_neighbours(training_set, test_instance, k)
	class_votes = {}
	for x in range(len(neighbours)):
		result = get_class(neighbours[x])
		if result in class_votes:
			class_votes[result] += 1
		else:
			class_votes[result] = 1
	sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_votes[0][0]

def main():
	args = retrieve_args()
	filename = get_filename(args)
	rows = get_rows(filename)
	split_ratio = get_split_ratio(args)
	training_set, test_set = split_data(rows, split_ratio)
	k = get_k(args)
	for x in range(len(test_set)):
		result = get_result(training_set, test_set[x], k)
		print("> predicted={}, actual={}".format(repr(result), repr(get_class(test_set[x]))))

main()
