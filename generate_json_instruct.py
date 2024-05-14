import csv
import json
# generate train
with open('data/InstructFormat-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/InstructFormat-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# generate test
with open('data/InstructFormat-Test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/InstructFormat-Test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)