import csv
import json
# generate train
with open('data/code_completion/CodeCompletion-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/code_completion/CodeCompletion-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    
# generate validation
with open('data/code_completion/CodeCompletion-Validation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/code_completion/CodeCompletion-Validation.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# generate test
with open('data/code_completion/CodeCompletion-Test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/code_completion/CodeCompletion-Test.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
