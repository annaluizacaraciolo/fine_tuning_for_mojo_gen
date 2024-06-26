import csv
import json
# Generate train
with open('data/instruct/Instruct-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/Instruct-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# Generate validation
with open('data/instruct/Instruct-Validation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/Instruct-Validation.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# Generate test
with open('data/instruct/Instruct-Test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/instruct/Instruct-Test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)