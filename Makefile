WEEK ?= 05

.PHONY: test

test:
	python -m pytest -q weeks/week-$(WEEK)/tests
