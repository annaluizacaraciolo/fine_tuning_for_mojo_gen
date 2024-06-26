import json
import random
import csv

def split_user_input_randomly(file_path, output_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    results = []
    
    for item in data:
        text = item["user_input"]
        if len(text) > 2:
            split_points = sorted(random.sample(range(1, len(text)), 2))
            part1 = text[:split_points[0]]
            part2 = text[split_points[1]:]
            results.append({"user_input": part1 + "<FILL_ME>" + part2, "system_answer": item["system_answer"]})
    
    with open(output_path, 'w') as outfile:
        json.dump(results, outfile, indent=4)
    
    return output_path

# Generate train
with open('data/code_completion/CodeCompletion-Train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/infilling/Infilling-Train.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
    
# Generate validation
with open('data/code_completion/CodeCompletion-Validation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('data/infilling/Infilling-Validation.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# Generate test
file_path = 'data/code_completion/CodeCompletion-Test.json'  
output_path = 'data/infilling/Infilling-Test.json' 
result_file_path = split_user_input_randomly(file_path, output_path)
