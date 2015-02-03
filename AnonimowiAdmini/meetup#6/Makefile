all: presentation slideshare clean

presentation: aa6.wiki
	wiki2beamer aa6.wiki > aa6.latex
	pdflatex presentation.latex

slideshare: aa6.wiki
	sed -r "s#\+*<[0-9][-]>\{(.*)\}# \1#" aa6.wiki > slideshare.wiki
	sed -i "s#<[0-9]>##g" slideshare.wiki
	sed -i "s#<[0-9]-[0-9]>##g" slideshare.wiki
	sed -i "s#\[\[.*\]\(\[.*\)\]#\1#" slideshare.wiki
	sed -i 's#^\[\(.*\)\]$$#\1#' slideshare.wiki
	sed "s#aa6#slideshare#" presentation.latex > unprivileged_lxc.latex
	wiki2beamer slideshare.wiki > slideshare.latex
	pdflatex unprivileged_lxc.latex

clean:
	rm -f *.toc *.snm *.out *.nav *.log *.aux
	rm -f slideshare*
	rm -f unprivileged_lxc.latex
	rm -f aa6.latex

run: presentation clean
	impressive -q -tCrossfade presentation.pdf
   
.PHONY: all clean
