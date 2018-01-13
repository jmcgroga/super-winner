#!/bin/sh
wget -O index.html http://localhost:5000/~jmcgroga/editor/
scp -p index.html jmcgroga@sage.jamesmcgrogan.net:public_html/editor/
scp -pr aggredit/editor/static/js jmcgroga@sage.jamesmcgrogan.net:public_html/editor/js
scp -pr aggredit/editor/static/css jmcgroga@sage.jamesmcgrogan.net:public_html/editor/css
