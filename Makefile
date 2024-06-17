#!/usr/bin/make
.PHONY: buildout cleanall instance test
all: buildout

bin/pip:
	python3.8 -m venv .
	touch $@

bin/buildout: bin/pip
	./bin/pip install -r requirements.txt
	touch $@

buildout: bin/buildout
	./bin/buildout -t 7

instance: buildout
	./bin/instance fg

test: buildout
	./bin/test

cleanall:
	rm -rf bin develop-eggs downloads include lib lib64 parts .installed.cfg .mr.developer.cfg bootstrap.py parts/omelette local share

