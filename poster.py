#-------------------------------------------------------------------------------
# Name:        poster
# Purpose:     DLF Forum 2014 Poster Presentation
#
# Author:      Jeremy Nelson
#
# Created:     2014/22/08
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     GPLv2
#-------------------------------------------------------------------------------
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = "Jeremy Nelson"
__license__ = 'GPLv2'
__copyright__ = '(c) 2014 by Jeremy Nelson'

import os
import sys
from flask import Flask, render_template, abort

poster = Flask(__name__)

@poster.route("/references")
def references():
    return render_template("references.html")

@poster.route("/")
def home():
    return render_template("index.html")

def main():
    host = '0.0.0.0'
    port = 3030
    poster.run(debug=True,
               host=host,
               port=port)

if __name__ == '__main__':
    main()
