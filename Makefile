clean:
	find . -name .pytest_cache -exec rm -rf {} \; 2>/dev/null
	find . -name __pycache__ -exec rm -rf {} \; 2>/dev/null
	rm -rf tex2pdf* 2>/dev/null

pdf:
	pandoc README.md -o README.pdf

book:
	./bin/compile.py

chapters:
	./bin/mk-chapters.sh
