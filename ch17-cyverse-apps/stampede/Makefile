.PHONY: clean up template job app test

APP = stampede2-template-0.0.1

clean:
	find . \( -name \*.out -o -name \*.param \) -exec rm {} \;

up:
	copy_from_manifest.py

template:
	jobs-template -A $(APP) > job.json

job:
	jobs-submit -F job.json

app:
	apps-addupdate -F app.json

test:
	sbatch test.sh
