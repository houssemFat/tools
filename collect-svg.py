"""
Collect svg files in single file
"""
import csv
import sys
import os
import json

from os.path import dirname, join, isfile
from os import listdir

current_dir = dirname(os.path.realpath(__file__))

files = [f for f in listdir(current_dir) if isfile(join(current_dir, f))]
html = ""
for f in files:
    if ".svg" in f:
        html += "<h1>{}<h1>".format(f)
        with open(join(current_dir, f), 'r') as fo:
            html += fo.read()

with open(join(current_dir, 'html'), 'w') as fw:
    fw.write(html)
