PYTHON ?= python3
LECTURE ?=
export PYTHONDONTWRITEBYTECODE := 1
.PHONY: all check review clean inventory test preview
all:
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)"
check:
	$(PYTHON) _alati/provera.py --lecture "$(LECTURE)"
review:
	$(PYTHON) _alati/uporedni_pregled.py --lecture "$(LECTURE)"
clean:
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)" --clean
inventory:
	$(PYTHON) _alati/inventar.py
test:
	$(PYTHON) -m unittest discover -s _alati/tests -v
preview:
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)" --preview
