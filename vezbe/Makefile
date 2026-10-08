VEZBE := 01 02 03 04 05 07 08
PYTHON ?= python3
.PHONY: all check check-sv check-equivalence check-pdf-code audit clean clean-build $(VEZBE)

all:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba; done

check:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba check; done
	$(PYTHON) PROVERA/structure.py
	$(MAKE) check-pdf-code
	$(PYTHON) PROVERA/negative_checks.py
	$(PYTHON) PROVERA/registry_check.py
	$(MAKE) check-sv
	$(MAKE) check-equivalence
	$(PYTHON) PROVERA/systemverilog_check.py negative

check-sv:
	$(PYTHON) PROVERA/systemverilog_check.py 01 --only students
	$(PYTHON) PROVERA/systemverilog_check.py 02 --only students

check-equivalence:
	$(PYTHON) PROVERA/systemverilog_check.py 01 --only equivalence
	$(PYTHON) PROVERA/systemverilog_check.py 02 --only equivalence

check-pdf-code:
	$(PYTHON) PROVERA/pdf_code_check.py

audit: all check
	$(PYTHON) PROVERA/audit.py --render --require-complete

clean:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba clean; done

$(VEZBE):
	$(MAKE) -C $@

clean-build:
	$(PYTHON) PROVERA/clean_build.py
