import csv
import sys
import os
import json

from os.path import dirname, abspath, join

if len(sys.argv) < 2:
    raise FileNotFoundError("A csv file is required")
curdir = dirname(os.path.realpath(__file__))
filename = join(curdir, sys.argv[1])
print("## reading file : " + filename)
locales_by_index = {}
locales = {}
key_index = int(sys.argv[2]) if len(sys.argv) > 2 else 0
i = key_index
print(i)
with open(filename, encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file)
    for row in rows:
        if i == key_index:
            for index, entry in enumerate(row[key_index + 1:]):
                if len(entry) > 0:
                    locales[entry.lower()] = {}
                    locales_by_index[index] = entry.lower()
            print(locales_by_index)
        else:
            if i > key_index:
                key = row[key_index]
                for index, entry in enumerate(row[key_index + 1:]):
                    locales[locales_by_index[index]][key] = entry
        i = i + 1

save_to = os.path.dirname(os.path.realpath(__file__))
save_to = join(save_to, '..', 'assets', 'i18n')

if not os.path.exists(save_to):
    os.makedirs(save_to)

for lang, values in locales.items():
    with open(join(save_to, lang + '.json'), 'w') as file:
        # print("writing " + lang + ".json file ")
        file.write(json.dumps(values))
