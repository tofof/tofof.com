START /B C:\Python27\Scripts\pelican.exe --debug --autoreload -r content
cd output
START /B C:\Python27\python -m SimpleHTTPServer
cd ..