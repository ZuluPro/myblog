.PHONY: all test clean docs

clean:
	rm -rf *.egg-info/ build/ dist/ coverage_html_report .coverage
	find . -name "*.pyc" -delete

test:
	python setup.py test

install:
	python setup.py install

build:
	python setup.py build

# docs:
# 	cd docs && make html
