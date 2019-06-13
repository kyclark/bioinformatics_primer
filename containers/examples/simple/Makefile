.PHONY = img img_old shell run clean

SINGULARITY = /usr/local/bin/singularity
IMG = hello-0.0.1.img
DEF = image.def

img: clean
	sudo $(SINGULARITY) build $(IMG) $(DEF)

img_old: clean
	sudo $(SINGULARITY) create --size 512 $(IMG)
	sudo $(SINGULARITY) bootstrap $(IMG) $(DEF)

shell:
	sudo $(SINGULARITY) shell --writable -B $(shell pwd):/tmp $(IMG)

run:
	sudo $(SINGULARITY) exec $(IMG) hello.sh

clean:
	rm -f $(IMG)
