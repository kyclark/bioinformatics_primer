imicrobe: clean
	sbatch fq2fa.sh -i $(SCRATCH)/imicrobe/fasta

clean:
	find . \( -name slurm-\* -o -name \*.param \) -exec rm {} \;
