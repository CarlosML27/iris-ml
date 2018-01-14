# iris-ml

This project consists of a classification of [iris flowers](https://en.wikipedia.org/wiki/Iris_(plant))  with machine learning algorithms in Python.

The data set used for this project is the [Bezdek variation](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data) of the world famous [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) introduced by Ronald Fisher in 1936. The [original data set](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) made by Fisher is also included in the data folder of the project.

## Getting started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to have installed Python 3. This version is installed by default on modern versions of Ubuntu.

To check if you have Python 3 already installed, use the following command.

	python3 --version
	
If your terminal returns the sentence "Python 3.X.Y" (being X and Y two positive numbers) or something similar, you're done!

Otherwise, you would need to install it using the following command line:

	sudo apt-get install python3
	
### Installing

Besides from the prerequisites, you won't need any other applications to run the program.

Simply download or clone the project to a folder of your local machine. 

If you want to clone the project into an empty folder, execute the following command:

	git clone git@github.com:CarlosML27/iris-ml.git

If the folder isn't empty, execute the following commands to clone the project:

	git init
	git remote add origin https://github.com/CarlosML27/iris-ml.git
	git fetch
	git checkout -t origin/master

Now you are ready to execute the project!

## Execution

To run the project, open a terminal window in "src" folder and type the following command:

	python3 iris-ml.py
	
### Optional arguments

You can use additional options in the arguments of the program. The following are the optional arguments supported:

- -h / --help: Shows a help message about the usage of the program. This argument will stop the execution of the program.

		python3 iris-ml.py --help
		
- -o / --original: Uses original data set made by Ronald Fisher instead of the default data set.

		python3 iris-ml.py --original
		
- -r RATIO / --ratio RATIO: Changes the split ratio between the training set and the test set. This value must be between 0.0 and 1.0. Its default value is 0.66.

		python3 iris-ml.py -r 0.82
		
- -k NEIGHBOURS / --neighbours NEIGHBOURS: Changes the "k" value for the kNN algorithm. This value must be a positive integer. Its default value is 3.

		python3 iris-ml.py -k 5
		

The combination of this optional arguments is also allowed, as you can see in the following example:

	python3 iris-ml.py --original -r 0.75 -k 4
	
## Authors

- **Carlos Morente** - *Initial work* - [CarlosML27 (Github)](https://github.com/CarlosML27) 

See also the list of the [contributors](https://github.com/CarlosML27/iris-ml/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/CarlosML27/iris-ml/blob/master/LICENSE) file for details.

## Acknowledgements

- **UCI Machine Learning Repository** for the data
- **Machine Learning Mastery** for the tutorial and the starting idea
- **StackOverflow and its community** for all the help
- **PurpleBooth@Github** for this README.md template
