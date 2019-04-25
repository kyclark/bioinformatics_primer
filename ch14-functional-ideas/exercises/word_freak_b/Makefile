.PHONY: doc test clean

test:
	pytest -v test.py

clean:
	rm -rf __pycache__ .pytest_cache

doc:
	pandoc README.md -o README.pdf

