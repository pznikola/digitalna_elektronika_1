MAIN := 04_aritmeticke_operacije
PYTHON ?= python3
FIGURES := $(shell find Images -name "*.tex" 2>/dev/null)
FIGPDF := $(FIGURES:.tex=.pdf)
HDL_SOURCES := $(shell rg --files code -g "*.sv")
.PHONY: all check clean
all: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex $(FIGPDF) $(HDL_SOURCES)
	latexmk -pdf -shell-escape -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex
Images/%.pdf: Images/%.tex
	cd $(dir $<) && latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error $(notdir $<)
check:
	$(PYTHON) code/provera.py
clean:
	latexmk -c $(MAIN).tex
	@for f in $(FIGURES); do (cd "$$(dirname "$$f")" && latexmk -c "$$(basename "$$f")"); done
