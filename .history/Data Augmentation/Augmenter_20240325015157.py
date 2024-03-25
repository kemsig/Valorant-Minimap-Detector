import cv2
import numpy as np
import datetime
import random
import os

def write_to_image(main_image, asset_image_path, vari_x=0, vari_y=0, vari_w=0, vari_h=0):
    # Load the asset
    small_image = cv2.imread(asset_image_path, cv2.IMREAD_UNCHANGED)

    # get dimension of all
    m_height, m_width, _ = main_image.shape
    s_height, s_width, _ = small_image.shape

    # Define the coordinates where you want to place the smaller image
    x_offset = random.randint(vari_x, m_width-s_width -vari_w)  
    y_offset = random.randint(vari_y, m_height-s_height -vari_h)  

    # Define the region of interest (ROI) on the main image
    roi = main_image[y_offset:y_offset+s_height, x_offset:x_offset+s_width]

    # Overlay the smaller image onto the ROI of the main image
    for i in range(s_height):
        for j in range(s_width):
            roi[i, j] = small_image[i, j][:3]
    
    # return roi PIXEL details since they are bounding box info
    return x_offset-vari_x, y_offset-vari_y, s_width+vari_w, s_height+vari_h
    

def get_rand_img(folder_name, file_type, root_path='Data Augmentation\\test_output', exclusive=False):
    folder_path = os.path.join(root_path, folder_name)
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith(f'.{file_type}')]
    random_png = random.choice(png_files)
    if not exclusive:
        png_files.remove(random_png)
    return os.path.join(folder_path, random_png)

def generate_data_YOLO(name, main_img_path, out_image_path, out_label_path, bb_variance=True, variance_pixel_range=5):
    # open image
    main_img = cv2.imread(main_img_path)
    
    # get random amount of characters to add
    max_blue = random.randint(0, 5)
    max_red = random.randint(0, 5)
    dead_blue = 5-max_blue
    dead_red = 5-max_red
    bomb = random.randint(0, 1)
    
    classes = {"max_blue":max_blue,
               "max_red":max_red,
               "dead blue":dead_blue,
               "dead red":dead_red,
               "bomb":bomb
            }
    
    class_index = 0
    for class_name, int_value in classes.items():
        print(f'Generating "{class_name}" with Index "{class_index} "{int_value}" times.')

        names = ['fade', 'kj', 'raze', 'omen', 'viper']
        for count in range(int_value):
            char_choice = class_name
            # pick a random character exclusive
            if names:
                if char_choice == 'max_blue':
                    picked_name = random.choice(names)
                    char_choice = f'{picked_name} blue'
                    names.remove(picked_name)
                    is_char = True
                elif char_choice == 'max_red':
                    picked_name = random.choice(names)
                    char_choice = f'{picked_name} red'
                    names.remove(picked_name)
                    is_char = True
            
            # get a random image of the character
            char_img_path = get_rand_img(char_choice, 'png')
            print(char_img_path)
            
            # add bounding box variance
            if bb_variance:
                x_center, y_center, norm_width, norm_height = write_to_image(
                    main_image=main_img,
                    asset_image_path= char_img_path,
                    vari_x= random.randint(0, variance_pixel_range),
                    vari_y= random.randint(0, variance_pixel_range),
                    vari_w= random.randint(0, variance_pixel_range),
                    vari_h= random.randint(0, variance_pixel_range)
                )
            else:
                x_center, y_center, norm_width, norm_height = write_to_image(
                    main_image=main_img,
                    asset_image_path= char_img_path,
                )

            m_height, m_width, _ = main_img.shape
            def convert_to_yolo_format(x, y, width, height, image_width, image_height):
                x_norm = x / image_width
                y_norm = y / image_height
                width_norm = width / image_width
                height_norm = height / image_height
                return x_norm, y_norm, width_norm, height_norm
            
            # calculate label positions in yolo format - <object-class-NUM> <x> <y> <width> <height>
            x_center, y_center, norm_width, norm_height = convert_to_yolo_format(
                x_center, y_center, norm_width, norm_height, m_width, m_height
            )

            # append to label file
            output_file = os.path.join(out_label_path, f"{name}.txt")
            with open(output_file, 'a') as f:
                f.write(f"{class_index} {x_center} {y_center} {norm_width} {norm_height}\n")

        # Iterate class index up
        class_index += 1
    
    # save the image
    cv2.imwrite(os.path.join(out_image_path, f'{name}.jpg'), main_img)
    
            
def generate_yolo_batch(count, name, background_path, output_path):
    # create output folder
    os.makedirs(output_path, exist_ok=True)
    
    # create label and image path + folders
    out_label_path = os.path.join(output_path, 'labels')
    out_image_path = os.path.join(output_path, 'images')
    
    os.makedirs(out_label_path, exist_ok=True)
    os.makedirs(out_image_path, exist_ok=True)
    
    #maps = ['LOTUS']
    for c in range(count):
        # get random map image
        map_img_path = get_rand_img('', 'jpg', root_path=background_path)
        generate_data_YOLO(
            name= f'{name}_{c}',
            main_img_path= map_img_path,
            out_image_path=out_image_path,
            out_label_path=out_label_path
        )
        print(f'Generated image {name}_{c}')

if __name__ == "__main__":
    generate_yolo_batch(count=1000, name='daug_lotus', background_path='Data Augmentation\\Backgrounds', output_path='TrainingSet\\DAUG_YOLO_SET')