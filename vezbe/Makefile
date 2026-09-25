VEZBE := 01 02 03 04 05 07 08
PYTHON ?= python3
.PHONY: all check audit clean clean-build $(VEZBE)

all:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba; done

check:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba check; done
	$(PYTHON) PROVERA/structure.py
	$(PYTHON) PROVERA/negative_checks.py
	$(PYTHON) PROVERA/registry_check.py

audit: all check
	$(PYTHON) PROVERA/audit.py --render --require-complete

clean:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba clean; done

$(VEZBE):
	$(MAKE) -C $@

clean-build:
	$(PYTHON) PROVERA/clean_build.py
