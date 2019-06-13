# Species Abundance Bubble Plot

Centrifuge is a program that will make taxonomic assignments to short DNA reads. Write a program called `plot.py` that will read the `.tsv` output file from Centrifuge that gives a summary of the species and abundance for a given sample. The program should take the output directory containing a number of samples and use `matplotlib` to create a bubble plot showing the abundance of taxa at various `-r|--rank` assignments.

````
$ ./plot.py
usage: plot.py [-h] [-r str] [-m float] [-M float] [-x str] [-t str] [-o str]
               DIR
plot.py: error: the following arguments are required: DIR
$ ./plot.py -h
usage: plot.py [-h] [-r str] [-m float] [-M float] [-x str] [-t str] [-o str]
               DIR

Plot Centrifuge out

positional arguments:
  DIR                   Centrifuge output directory

optional arguments:
  -h, --help            show this help message and exit
  -r str, --rank str    Tax rank (default: species)
  -m float, --min float
                        Minimum percent abundance (default: 0.0)
  -M float, --multiplier float
                        Multiply abundance (default: 1.0)
  -x str, --exclude str
                        Tax IDs or names to exclude (default: )
  -t str, --title str   Figure title (default: )
  -o str, --outfile str
                        Output file (default: bubble.png)
````
