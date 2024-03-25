import json
import cv2
import pandas as pd

file_path = 'Data Augmentation/20'

with open(file_path, 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

df = pd.json_normalize(data)

print(df['task.data.image'].values)



