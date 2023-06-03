install:
	pip install -r requirements.txt

lint:
	pylint --disable R,C num_sqrt.py

test:
	python -m pytest -vv test_numSqrt.py