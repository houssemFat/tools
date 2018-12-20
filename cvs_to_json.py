import csv
import sys
import os
import json

from os.path import dirname, abspath, join

curdir = dirname(os.path.realpath(__file__))
filename = join(curdir, sys.argv[1])
print("## reading file : " + filename)
locales_by_index = {}
locales = {}
i = 0
with open(filename, encoding='utf-8') as csv_file:
  rows = csv.reader(csv_file)
  for row in rows:
    if i == 0:
      for index, entry in enumerate(row):
        if (len(entry) > 0):
          locales[entry.lower()] = {}
          locales_by_index[index] = entry.lower()
    else:
      print(locales)
      print(locales_by_index)
      key = row[0]
      for index, entry in enumerate(row[1:]):
        #print(key)
        #print("###")
        #print(entry)
        locales[locales_by_index[index + 1]][key] = entry
    i = i + 1

save_to = dirname(dirname(abspath(__file__)))
save_to = join(save_to, 'src', 'assets', 'i18n')
print (save_to)

for lang, values in locales.items():
  with open(join(save_to, lang + '.json'), 'w') as file:
    # print("writing " + lang + ".json file ")
    file.write(json.dumps(values))
