.PHONY: shell parallel halt

JOBS = 'jobs'

shell:
	bash $(JOBS)

parallel:
	parallel -j 2 < $(JOBS)

halt:
	parallel -j 2 --halt soon,fail=1 < $(JOBS)

names:
	./run_names.sh
