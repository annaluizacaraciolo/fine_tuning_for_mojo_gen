import csv
import json
# generate train
with open('data/MojoDataset-TrainFormatado.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/MojoTrain-Formatado.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    
# generate test
with open('data/MojoDataset-TestFormatado.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/MojoTest-Formatado.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
