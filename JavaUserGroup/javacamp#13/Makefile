all: presentation slideshare clean

presentation: jc13.wiki
	wiki2beamer jc13.wiki > jc13.latex
	pdflatex presentation.latex

slideshare: jc13.wiki
	sed -r "s#\+*<[0-9][-]>\{(.*)\}# \1#" jc13.wiki > slideshare.wiki
	sed -i "s#<[0-9]>##g" slideshare.wiki
	sed -i "s#<[0-9]-[0-9]>##g" slideshare.wiki
	sed -i "s#\[\[.*\]\(\[.*\)\]#\1#" slideshare.wiki
	sed -i 's#^\[\(.*\)\]$$#\1#' slideshare.wiki
	sed "s#jc13#slideshare#" presentation.latex > docker_for_developers.latex
	wiki2beamer slideshare.wiki > slideshare.latex
	pdflatex docker_for_developers.latex

clean:
	rm -f *.toc *.snm *.out *.nav *.log *.aux
	rm -f slideshare*
	rm -f docker_on_a_developers_desktop.latex
	rm -f jc13.latex

run: presentation clean
	impressive -q -tCrossfade presentation.pdf
   
.PHONY: all clean
