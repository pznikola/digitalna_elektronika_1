VEZBE := 03 04 05 07 08
.PHONY: all check clean $(VEZBE)

all:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba; done

check:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba check; done

clean:
	@set -e; for vezba in $(VEZBE); do $(MAKE) -C $$vezba clean; done

$(VEZBE):
	$(MAKE) -C $@
