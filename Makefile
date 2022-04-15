run:
	python src/main.py

run_tui:
	python src/tui_engine.py

unittest:
	coverage run -m unittest discover

pylint:
	pylint ./src/

coverage:
	coverage -report -m 
