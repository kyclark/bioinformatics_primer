pdf: md
	pandoc re.md -o $(shell basename $(shell pwd)).pdf

md:
	jupyter nbconvert --to markdown re.ipynb
