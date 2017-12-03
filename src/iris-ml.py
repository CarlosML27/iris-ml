import csv
import argparse

defaultfilename = '../data/iris.csv'

parser = argparse.ArgumentParser()
parser.add_argument("--original", help="use R.Fisher original data", action='store_true')
args = parser.parse_args()
filename = defaultfilename
if args.original:
	filename = '../data/iris-original.csv'
with open(filename, 'rt') as csvfile:
	dataset = csv.reader(csvfile)
	datasetlist = list(dataset)
	rows = datasetlist[1:]
	separator = ', '	
	print(filename)
	for row in rows:
		print(separator.join(row))
