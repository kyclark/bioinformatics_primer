.PHONY: pdf test clean

test:
	pytest -v test.py

pdf:
	pandoc README.md -o README.pdf

clean:
	rm -rf __pycache__ .pytest_cache gapminder
