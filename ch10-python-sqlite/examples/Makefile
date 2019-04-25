DB = centrifuge.db
DEF = tables.sql

db:
	find . -name $(DB) -exec rm {} \;
	sqlite3 $(DB) < $(DEF)

load:
	./load_centrifuge.py *.tsv

data:
	wget ftp://ftp.imicrobe.us/projects/75/samples/1375/YELLOWSTONE_SMPL_20717.centrifuge.tsv.gz
	wget ftp://ftp.imicrobe.us/projects/75/samples/1376/YELLOWSTONE_SMPL_20719.centrifuge.tsv.gz
	wget ftp://ftp.imicrobe.us/projects/75/samples/1377/YELLOWSTONE_SMPL_20721.centrifuge.tsv.gz
	wget ftp://ftp.imicrobe.us/projects/75/samples/1378/YELLOWSTONE_SMPL_20723.centrifuge.tsv.gz
	wget ftp://ftp.imicrobe.us/projects/75/samples/1379/YELLOWSTONE_SMPL_20725.centrifuge.tsv.gz
	wget ftp://ftp.imicrobe.us/projects/75/samples/1380/YELLOWSTONE_SMPL_20727.centrifuge.tsv.gz
	gunzip *.gz

tabulate:
	python3 -m pip install tabulate --user
