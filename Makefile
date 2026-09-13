PYTHON ?= python3
PDFLATEX ?= pdflatex
.PHONY: paper figures verify
figures:
	PDFLATEX="$(PDFLATEX)" $(PYTHON) scripts/draw_affine_q3.py
paper:
	PDFLATEX="$(PDFLATEX)" $(PYTHON) scripts/build_paper.py
verify:
	$(PYTHON) scripts/verify.py
