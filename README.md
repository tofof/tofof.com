The source for my personal website.

# Setup
pip install markdown  
pip install pelican  
pip install typogrify  
git clone --recursive https://github.com/getpelican/pelican-plugins  
npm install
npm init
npm install grunt --save-dev
npm install grunt-modernizr --save-dev
npm install grunt-purifycss -save-dev
npm install grunt-purgecss --save-dev 
npm install grunt-contrib-clean --save-dev
npm install grunt-contrib-copy --save-dev
npm install grunt-contrib-uglify --save-dev
npm install grunt-contrib-htmlmin --save-dev 
npm install -g firebase-tools
firebase login

# Usage
***pelican content***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Build the site from source files (markdown and images) contained in `content`

***grunt default***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Postprocess the output from pelican for minifying css/js/html

***firebase deploy***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Upload the site to firebase hosting