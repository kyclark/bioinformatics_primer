.PHONY: doc test data

data:
	wget ftp://ftp.imicrobe.us/biosys-analytics/exercises/unclustered-proteins.tgz

doc:
	pandoc README.md -o README.pdf

test:
	python3 -m pytest -v test.py
