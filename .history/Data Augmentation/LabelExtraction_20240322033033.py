import json
import cv2
import pandas as pd

file_path = 'Data Augmentation/20'

def crop_single_image(file_path='Data Augmentation/20'):
    with open(file_path, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    df = pd.json_normalize(data)


    image_path = df['task.data.image'].values[0]
    image = cv2.imread(image_path)

    for value in df['result'].values[0]:
        name = value['value']['rectanglelabels'][0]
        x = value['value']['x']
        y = value['value']['y']
        width = value['value']['width']
        height = value['value']['height']


print(df['result'].values[0][0]['value'])





