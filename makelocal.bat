pelican.exe -d content
call grunt
python -m http.server --directory output/