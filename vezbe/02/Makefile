PYTHON ?= python3
.PHONY: all check clean
all:
	$(PYTHON) ../PROVERA/build.py 02
check:
	$(PYTHON) code/provera.py
clean:
	latexmk -c 02_sinteza_kola_srednjeg_stepena_integracije.tex
