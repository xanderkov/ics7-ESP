.PHONY: rep clean

FILE = main

rep:
	tectonic $(FILE).tex
	mv main.pdf "РК_ЭПИ_ИУ7-86_КовельАД.pdf"

clean:
	rm *.aux *.bbl *.blg *.log *.out *.toc pages/*.aux inc/*.aux inc/*.bbl inc/*.blg inc/*.log inc/*.out inc/*.toc *.synctex.gz
	echo "Clear:Ready"