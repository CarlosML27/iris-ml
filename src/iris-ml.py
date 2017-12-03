import csv
import argparse
import random
import math

DEFAULT_FILENAME = '../data/iris.csv'
DEFAULT_SPLIT_RATIO = 0.66

def restricted_float(x):
	x = float(x)
	if x < 0.0 or x > 1.0:
		raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x,))
	return x

def retrieve_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--original", help="use R.Fisher original data", action='store_true')
	parser.add_argument("-r", "--ratio", help="change split ratio of the data (default=0.66)", action="store", default=DEFAULT_SPLIT_RATIO, type=restricted_float)
	return parser.parse_args()
	
def get_filename(args):
	return '../data/iris-original.csv' if args.original else DEFAULT_FILENAME

def get_split_ratio(args):
	return args.ratio

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

def main():
	args = retrieve_args()
	filename = get_filename(args)
	rows = get_rows(filename)
	split_ratio = get_split_ratio(args)
	training_set, test_set = split_data(rows, split_ratio)
	print("Train: {}".format(repr(len(training_set))))
	print("Test: {}".format(repr(len(test_set))))
	data1 = [2, 7, -1, 'a']
	data2 = [0, 6, 4, 'b']
	distance = calculate_distance(data1, data2, len(data1)-1)
	print("Distance: {}".format(repr(distance)))
main()
