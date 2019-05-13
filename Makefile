pdf:
	pandoc README.md -o README.pdf

book:
	./bin/compile.sh

chapters:
	./bin/mk-chapters.sh
