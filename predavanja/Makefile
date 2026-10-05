PYTHON ?= python3
.DEFAULT_GOAL := all
LECTURE ?=
export PYTHONDONTWRITEBYTECODE := 1
.PHONY: all check review notes clean inventory test preview require-lecture test-redizajn
require-lecture:
	@test -n "$(LECTURE)" || { echo 'Obavezan je LECTURE=<pun_folder_predavanja>.'; exit 2; }
all: require-lecture
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)"
check: require-lecture
	$(PYTHON) _alati/provera.py --lecture "$(LECTURE)"
review: require-lecture
	$(PYTHON) _alati/uporedni_pregled.py --lecture "$(LECTURE)"
notes: require-lecture
	$(PYTHON) _alati/redizajn.py notes --lecture "$(LECTURE)"
clean: require-lecture
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)" --clean
inventory:
	$(PYTHON) _alati/inventar.py
test:
	$(PYTHON) -m unittest discover -s _alati/tests -v
test-redizajn:
	$(PYTHON) _alati/proba_redizajna.py
preview: require-lecture
	$(PYTHON) _alati/izgradnja.py --lecture "$(LECTURE)" --preview
