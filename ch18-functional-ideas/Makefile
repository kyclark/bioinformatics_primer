pdf: md
	pandoc functional_ideas.md -F ../../bin/include.hs -o $(shell basename $(shell pwd)).pdf

md:
	jupyter nbconvert --to markdown functional_ideas.ipynb
