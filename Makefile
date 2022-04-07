run:
	python ./src/main.py

unittest:
	coverage run -m unittest discover

pylint:
	pylint ./src/
