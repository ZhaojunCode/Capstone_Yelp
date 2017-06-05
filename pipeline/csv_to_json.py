import csv
import json

csvfile = open('../IUC-businesses.csv', 'r')
jsonfile = open('IUC-businesses.json', 'w')

fieldnames = (['id', 'name', 'longitude', 'latitude'])
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
