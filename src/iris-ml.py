import csv
import argparse
import random
import math
import operator

DEFAULT_FILENAME = '../data/iris.csv'
ORIGINAL_FILENAME = '../data/iris-original.csv'
DEFAULT_SPLIT_RATIO = 0.66
DEFAULT_K_VALUE = 3

def restricted_float(x):
	x = float(x)
	lower_value = 0.0
	upper_value = 1.0
	if x < lower_value or x > upper_value:
		raise argparse.ArgumentTypeError("{} is not in the range [{}, {}]".format(x, lower_value, upper_value))
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
	parser.add_argument("-k", "--neighbours", help="change number of neighbours used in kNN (default={})".format(DEFAULT_K_VALUE), action="store" ,default=DEFAULT_K_VALUE, type=positive_int)
	return parser.parse_args()

def get_filename(args):
	return ORIGINAL_FILENAME if args.original else DEFAULT_FILENAME

def get_split_ratio(args):
	return args.ratio

def get_k_value(args):
	return args.neighbours	

def get_rows(filename):
	with open(filename, 'rt') as csvfile:	
		dataset = csv.reader(csvfile)
		datasetlist = list(dataset)
		rows = datasetlist[1:]
		for x in range(len(rows)):
			for y in range(len(rows[x])-1):
				rows[x][y] = float(rows[x][y])
		return rows

def print_rows(rows):
	separator = ', '
	for row in rows:
		print(separator.join(row))

def split_data(data, split_ratio):
	training_set = []
	test_set = []
	for x in range(len(data)):
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

def get_distances(training_set, test_instance):
	distances = []
	length = len(test_instance)-1
	for x in range(len(training_set)):
		distance = calculate_distance(training_set[x], test_instance, length)
		distances.append((training_set[x], distance))
	distances.sort(key=operator.itemgetter(1))	
	return distances

def get_neighbour_instance(distances, x):
	return distances[x][0]

def get_k_nearest_instances(distances, k):
	neighbours = []
	for x in range(k):
		neighbour = get_neighbour_instance(distances, x)
		neighbours.append(neighbour)
	return neighbours

def get_neighbours(training_set, test_instance, k):
	distances = get_distances(training_set, test_instance)
	neighbours = get_k_nearest_instances(distances, k)
	return neighbours

def get_class(instance):
	return instance[-1]

def get_prediction(training_set, test_instance, k):
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

def get_performance(predictions):
	correct = 0
	length = len(predictions)
	for x in range(length):
		if predictions[x][0] == predictions[x][1]:
			correct += 1
	return (correct/float(length)) * 100.0

def main():
	args = retrieve_args()
	filename = get_filename(args)
	split_ratio = get_split_ratio(args)
	k_value = get_k_value(args)
	rows = get_rows(filename)
	training_set, test_set = split_data(rows, split_ratio)
	test_set_length = len(test_set)
	predictions = [[0 for x in range(2)] for y in range(test_set_length)]
	for x in range(test_set_length):
		instance = test_set[x]
		prediction = get_prediction(training_set, instance, k_value)
		instance_class = get_class(instance)
		predictions[x][0] = instance_class
		predictions[x][1] = prediction
		print("> predicted={}, actual={}".format(repr(prediction), repr(instance_class)))
	print(">>> ACCURACY: {}%".format(get_performance(predictions)))

if __name__ == '__main__':
	main()
