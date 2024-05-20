import csv
import json
# generate train
with open('data/CodeCompletion-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/CodeCompletion-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    
# generate validation
with open('data/CodeCompletion-Validation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/CodeCompletion-Validation.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
