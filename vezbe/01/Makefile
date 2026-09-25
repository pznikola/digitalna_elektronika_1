PYTHON ?= python3
.PHONY: all check clean
all:
	$(PYTHON) ../PROVERA/build.py 01
check:
	$(PYTHON) code/provera.py
clean:
	latexmk -c 01_kombinacione_hazardi.tex
