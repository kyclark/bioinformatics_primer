FASTA_DIR = "/rsgrps/bhurwitz/kyclark/blast-test/fasta"
OUT_DIR = "/rsgrps/bhurwitz/kyclark/blast-test"
BLAST_DB = "/rsgrps/bhurwitz/hurwitzlab/data/blast/gos/gos"

run: clean
	./00-controller.sh -b $(BLAST_DB) -f $(FASTA_DIR) -o $(OUT_DIR) 

clean:
	find . \( -name \*.conf -o -name \*.OU \) -exec rm {} \;
