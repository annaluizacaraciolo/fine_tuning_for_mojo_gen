import json
import random

def split_text_randomly_and_write(file_path, output_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    results = []
    
    for item in data:
        text = item["text"]
        if len(text) > 2:
            split_points = sorted(random.sample(range(1, len(text)), 2))
            part1 = text[:split_points[0]]
            part2 = "<FILL_ME>"
            part3 = text[split_points[1]:]
            results.append({"text": part1 + part2 + part3})

    # Write results to a new JSON file
    with open(output_path, 'w') as outfile:
        json.dump(results, outfile, indent=4)
    
    return output_path


def split_user_input_randomly(file_path, output_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    results = []
    
    for item in data:
        text = item["user_input"]
        if len(text) > 2:  # Ensure there's enough length to split into three parts
            split_points = sorted(random.sample(range(1, len(text)), 2))
            part1 = text[:split_points[0]]
            part2 ="<FILL_ME>"
            part3 = text[split_points[1]:]
            results.append({"user_input": part1 + part2 + part3, "system_answer": item["system_answer"]})
    
    # Write results to a new JSON file
    with open(output_path, 'w') as outfile:
        json.dump(results, outfile, indent=4)
    
    return output_path

# Generate train
file_path = 'data/code_completion/CodeCompletion-Train.json'  
output_path = 'data/infilling/Infilling-Train.json' 
result_file_path = split_text_randomly_and_write(file_path, output_path)

# Generate validation
file_path = 'data/code_completion/CodeCompletion-Validation.json'  
output_path = 'data/infilling/Infilling-Validation.json' 
result_file_path = split_text_randomly_and_write(file_path, output_path)

# Generate test
file_path = 'data/code_completion/CodeCompletion-Test.json'  
output_path = 'data/infilling/Infilling-Test.json' 
result_file_path = split_user_input_randomly(file_path, output_path)
