import csv
import json
# generate test
with open('data/MojoDataset-Test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/MojoDataset-Test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)