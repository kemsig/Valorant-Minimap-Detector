import json
import cv2
import pandas as pd
import os
import uuid
from Augmenter import get_rand_img

def overlay_map_background(name, map_img_path, output_path, tp_image_path='Data Augmentation\\Backgrounds\\BG_TRANSPARENT\\TP_LOTUS.png'):
    # Load the images
    foreground = cv2.imread(tp_image_path, cv2.IMREAD_UNCHANGED)
    background = cv2.imread(map_img_path)

    # Split the foreground image into its RGB channels and create a mask
    b_channel, g_channel, r_channel, alpha_channel = cv2.split(foreground)
    mask = cv2.merge((alpha_channel, alpha_channel, alpha_channel))

    # Convert the images to float32 for blending
    foreground = foreground.astype(float)
    background = background.astype(float)
    mask = mask.astype(float)/255

    # Perform alpha blending
    foreground = cv2.multiply(mask, foreground[:, :, :3])
    background = cv2.multiply(1.0 - mask, background)

    # Add the images together
    result = cv2.add(foreground, background)

    # Convert the result back to uint8
    result = result.astype('uint8')

    # Display or save the result
    cv2.imshow('Merged Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for i in range(100):
    map_path = get_rand_img(foldername=''
                            root_path='',
                            exclusive=True,
                            file_type='png')


def crop_single_image(output_path, images_path, labels_path):
    # open json
    with open(labels_path, 'r') as file:
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
        identifier = str(uuid.uuid4())
        cv2.imwrite(os.path.join(folder_path, f'{name}_{identifier}.png'), cropped_image)
    

'''
output_path = 'Data Augmentation\\test_output'
labels_path = 'C:\\Users\\kayne\\OneDrive\\Desktop\\LABELSTUDIO\\label-studio\\mydata\\TrainingLabels'
images_path = 'C:\\Users\\kayne\\OneDrive\\Desktop\\LABELSTUDIO\\label-studio\\mydata\\TrainingSetRandom'

for label in os.listdir(labels_path):
    item_path = os.path.join(labels_path, label)
    
    # don't access directory
    if not os.path.isfile(item_path):
        continue
    
    print(label)
    crop_single_image(output_path, images_path=images_path, labels_path=item_path)
    '''








