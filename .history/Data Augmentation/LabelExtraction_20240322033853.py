import json
import cv2
import pandas as pd
import os


def crop_single_image(file_path='Data Augmentation/20', output_path):
    with open(file_path, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    df = pd.json_normalize(data)


    image_path = df['task.data.image'].values[0]
    image = cv2.imread(image_path)
  
    original_height, original_width, _ = image.shape

    for value in df['result'].values[0]:
        name = value['value']['rectanglelabels'][0]
        x = value['value']['x']
        y = value['value']['y']
        width = value['value']['width']
        height = value['value']['height']

        # Make path
        os.makedirs(os.path.join(dest_dir, 'images', 'Train'), exist_ok=True)

        pixel_x = x / 100.0 * original_width
        pixel_y = y / 100.0 * original_height
        pixel_width = width / 100.0 * original_width
        pixel_height = height / 100.0 * original_height
        
        cropped_image = image[pixel_y:pixel_y+pixel_height, pixel_x:pixel_x+pixel_width]
        
        # crop image
        cv2.imwrite("cropped_image.jpg", cropped_image)
    
    print(df['result'].values[0][0]['value'])







