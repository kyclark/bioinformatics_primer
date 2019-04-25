.PHONY: cat head doc test 

test:
	python3 -m pytest -v test.py

cat:
	./cat-n.sh files/sonnet-29.txt

head:
	./head.sh files/issa.txt

doc:
	pandoc README.md -o README.pdf
