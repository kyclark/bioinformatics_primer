pdf: md
	pandoc re.md -F ../../bin/include.hs -o $(shell basename $(shell pwd)).pdf

md:
	jupyter nbconvert --to markdown re.ipynb
