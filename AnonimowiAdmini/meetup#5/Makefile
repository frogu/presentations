all: presentation slideshare clean

presentation: aa5.wiki
	wiki2beamer aa5.wiki > aa5.latex
	pdflatex presentation.latex

slideshare: aa5.wiki
	sed -r "s#\+*<[0-9][-]>\{(.*)\}# \1#" aa5.wiki > slideshare.wiki
	sed -i "s#<[0-9]>##g" slideshare.wiki
	sed -i "s#<[0-9]-[0-9]>##g" slideshare.wiki
	sed -i "s#\[\[.*\]\(\[.*\)\]#\1#" slideshare.wiki
	sed -i 's#^\[\(.*\)\]$$#\1#' slideshare.wiki
	sed "s#aa5#slideshare#" presentation.latex > selenium-for-ops.latex
	wiki2beamer slideshare.wiki > slideshare.latex
	pdflatex selenium-for-ops.latex

clean:
	rm -f *.toc *.snm *.out *.nav *.log *.aux
	rm -f slideshare*
	rm -f selenium-for-ops.latex
	rm -f aa5.latex

run: presentation clean
	impressive -q -tCrossfade presentation.pdf
   
.PHONY: all clean
