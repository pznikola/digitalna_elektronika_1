MAIN := 07_staticke_karakteristike
PYTHON ?= python3
FIGURES := $(shell find Images -name "*.tex" 2>/dev/null)
FIGPDF := $(FIGURES:.tex=.pdf)
.PHONY: all check clean
all: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex $(FIGPDF)
	latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex
Images/%.pdf: Images/%.tex
	cd $(dir $<) && latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error $(notdir $<)
check:
	$(PYTHON) code/provera.py
clean:
	latexmk -c $(MAIN).tex
	@for f in $(FIGURES); do (cd "$$(dirname "$$f")" && latexmk -c "$$(basename "$$f")"); done
