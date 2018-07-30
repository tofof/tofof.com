START /B pelican.exe --debug --autoreload -r content
cd output
START /B python -m http.server
cd ..