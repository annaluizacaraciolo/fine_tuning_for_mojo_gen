import csv
import json

with open('MojoDataset-TestFormatado.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]


with open('MojoTest-Formatado.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
