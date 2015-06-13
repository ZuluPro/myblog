clean:
	rm -rf myblog.egg-info/ build/ myblog/static/*
	touch myblog/static/.empty

test:
	python setup.py test

install:
	python setup.py install

build:
	python setup.py build
