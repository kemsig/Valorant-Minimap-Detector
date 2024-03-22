import json
import cv2
import pandas as pd
import os
import datetime


def crop_single_image(output_path, images_path, labels_path, file_path='Data Augmentation/20'):
    # open json
    with open(file_path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    df = pd.json_normalize(data)

    filename = os.path.basename(df['task.data.image'].values[0])
    image_path = os.path.join(images_path, filename)
    image = cv2.imread(image_path)
  
    original_height, original_width, _ = image.shape

    for value in df['result'].values[0]:
        name = value['value']['rectanglelabels'][0]
        x = value['value']['x']
        y = value['value']['y']
        width = value['value']['width']
        height = value['value']['height']

        # Make path
        folder_path = os.path.join(output_path, name)
        os.makedirs(folder_path, exist_ok=True)

        pixel_x = int(x / 100.0 * original_width)
        pixel_y = int(y / 100.0 * original_height)
        pixel_width = int(width / 100.0 * original_width)
        pixel_height = int(height / 100.0 * original_height)
        
        # crop image
        cropped_image = image[pixel_y:pixel_y+pixel_height, pixel_x:pixel_x+pixel_width]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        cv2.imwrite(os.path.join(folder_path, f'{name}_{timestamp}.png'), cropped_image)
    


output_path = 'Data Augmentation\\test_output'
labels_path = 'C:\\Users\\kayne\\OneDrive\\Desktop\\LABELSTUDIO\\label-studio\\mydata\\TrainingLabels'
images_path = 'C:\\Users\\kayne\\OneDrive\\Desktop\\LABELSTUDIO\\label-studio\\mydata\\TrainingSetRandom'

for label in os.listdir(labels_path):
    print(label)

#crop_single_image(output_path, images_path=images_path, labels_path=labels_path, file_path='Data Augmentation/20')







