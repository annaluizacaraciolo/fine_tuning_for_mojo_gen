import csv
import json
# generate train
with open('data/instruct/InstructFormat-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/InstructFormat-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# generate validation
with open('data/instruct/InstructFormat-Validation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/InstructFormat-Validation.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# generate test
with open('data/instruct/Instruct-Test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/Instruct-Test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)