import csv

filename = '../data/iris.csv'

with open(filename, 'rt') as csvfile:
	dataset = csv.reader(csvfile)
	datasetlist = list(dataset)
	rows = datasetlist[1:]
	separator = ', '
	for row in rows:
		print(separator.join(row))
