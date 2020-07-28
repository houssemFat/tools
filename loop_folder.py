"""
Collect svg files in single file
"""
import os
import sys

from os.path import dirname, join, isfile
from os import listdir

if len(sys.argv) > 1:
    target_folder = sys.argv[1]
else:
    target_folder = dirname(os.path.realpath(__file__))
    print("looking js files in folder {}".format(target_folder))

files = [f for f in listdir(target_folder) if isfile(join(target_folder, f))]
output = ""
for f in files:
    if ".js" in f:
        class_name = os.path.splitext(f)[0]
        output += "export {{default as {f}}} from './{f}'".format(f=class_name)
        output += "\n"

print(output)
