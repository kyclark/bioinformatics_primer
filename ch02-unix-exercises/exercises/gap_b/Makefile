.PHONY: doc test clean

test:
	pytest -v test.py

doc:
	pandoc README.md -o README.pdf

clean:
	rm -rf __pycache__ .pytest_cache gapminder
