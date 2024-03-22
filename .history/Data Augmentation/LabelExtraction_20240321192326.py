import json


file_path = 'Data Augmentation/20'

with open(file_path, 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

print(data)

