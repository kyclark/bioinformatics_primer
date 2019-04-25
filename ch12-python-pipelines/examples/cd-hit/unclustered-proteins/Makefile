all: clean info

clean:
	find . \( -name unclustered-proteins.fa -o -name clean-proteins.fa -o -name \*.o \) -exec rm {} \;

clustered-ids:
	grep -ve '^>' cdhit60.3+.clstr | awk '{print $$3}' | awk -F"|" '{print $$2}' | sort > clustered-ids.o

clean-proteins:
	sed "s/|.*//" proteins.fa > clean-proteins.fa

protein-ids: clean-proteins
	grep -e '^>' clean-proteins.fa | sed "s/^>//" | sort > protein-ids.o

unclustered-ids: clustered-ids protein-ids
	comm -23 protein-ids.o clustered-ids.o > unclustered-ids.o

unclustered-proteins: unclustered-ids
	seqmagick convert --include-from-file unclustered-ids.o clean-proteins.fa unclustered-proteins.fa

info: unclustered-proteins
	seqmagick info unclustered-proteins.fa

dist: clean
	(cd .. && tar czvf unclustered-proteins.tgz unclustered-proteins)

check: unclustered-proteins
	./check.sh
