# advanced-testing
Doing advanced testing techniques

## Setup 

1. Create a python virtual environment

```bash
python3 -m venv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. Create scaffold

```bash
touch Makefile && touch test_hello.py && touch hello.py. && requirements.txt
```

3. Populate `Makefile`

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

