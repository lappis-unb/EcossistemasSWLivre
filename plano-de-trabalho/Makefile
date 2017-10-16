
BASE_NAME = plano-minc

LATEX     = latex
PDFLATEX  = pdflatex
BIBTEX    = bibtex
MAKEINDEX = makeindex

SOURCES = texto/00-resumo.tex texto/01-introducao.tex texto/02-convenente.tex texto/03-justificativa.tex texto/04-objeto.tex texto/05-metas.tex texto/06-metodologia.tex texto/07-gestao.tex texto/08-orcamento.tex texto/09-pesquisa.tex

pdf: $(BASE_NAME).pdf
	evince $(BASE_NAME).pdf &
ps: $(BASE_NAME).ps

$(BASE_NAME).pdf: $(BASE_NAME).tex $(SOURCES)
	$(PDFLATEX) $(BASE_NAME).tex
	$(BIBTEX) $(BASE_NAME)
	$(MAKEINDEX) $(BASE_NAME)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(BASE_NAME).ps: $(BASE_NAME).tex
	$(LATEX) $<
	$(BIBTEX) $(BASE_NAME)
	$(MAKEINDEX) $(BASE_NAME)
	$(LATEX) $<
	$(LATEX) $<

clean:
	rm -f $(BASE_NAME)*.ps $(BASE_NAME)*.dvi *.log \
	      *.aux *.blg *.toc *.brf *.ilg *.ind \
	      missfont.log $(BASE_NAME)*.bbl $(BASE_NAME)*.pdf $(BASE_NAME)*.out \
		  $(BASE_NAME)*.lof $(BASE_NAME)*.lot  *.swp
