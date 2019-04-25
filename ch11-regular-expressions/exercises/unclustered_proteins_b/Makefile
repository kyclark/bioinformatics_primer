.PHONY: doc test data

doc:
	pandoc README.md -o README.pdf

data:
	wget ftp://ftp.imicrobe.us/biosys-analytics/exercises/unclustered-proteins.tgz

test:
	pytest -v test.py
