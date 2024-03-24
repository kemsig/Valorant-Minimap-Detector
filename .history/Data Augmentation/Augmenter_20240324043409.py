import cv2
import numpy as np
import datetime
import random
import os

def write_to_image(main_image, asset_image_path, x_off=0, y_off=0):
    # Load the asset
    small_image = cv2.imread(asset_image_path, cv2.IMREAD_UNCHANGED)

    # get dimension of all
    m_height, m_width, _ = main_image.shape
    s_height, s_width, _ = small_image.shape

    # Define the coordinates where you want to place the smaller image
    x_offset = random.randint(0, m_width-s_width)  
    y_offset = random.randint(0, m_height-s_height)  

    # Define the region of interest (ROI) on the main image
    roi = main_image[y_offset:y_offset+s_height, x_offset:x_offset+s_width]

    # Overlay the smaller image onto the ROI of the main image
    for i in range(s_height):
        for j in range(s_width):
            roi[i, j] = small_image[i, j][:3]
    
    # return roi PIXEL details since they are bounding box info
    return x_offset, y_offset, s_width, s_height
    

def get_rand_img(folder_name, root_path='Data Augmentation\\test_output'):
    folder_path = os.path.join(root_path, folder_name)
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    random_png = random.choice(png_files)
    return os.path.join(folder_path, random_png)


def generate_data_YOLO(name, main_img_path, out_image_path, out_label_path):
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
    
    for class_name, int_value in classes.items():
        print(f'Generating "{class_name}" "{int_value}" times.')

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
            char_img_path = get_rand_img(char_choice)
            print(char_img_path)
            
            write_to_image(
                main_image=main_img,
                asset_image_path= char_img_path,
            )
            # Display the resulting image
            cv2.imshow('Result', main_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            '''
            # calculate label positions in yolo format
            # <object-class-NUM> <x> <y> <width> <height>
            x_center = 0
            y_center = 0
            norm_width = 0
            norm_height = 0
            


            # append to label file
            output_file = os.path.join(out_label_path, f"{name}.txt")
            
            with open(output_file, 'a') as f:
                f.write(f"{class_num} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}")
    
            # put character image on spot
            '''

generate_data_YOLO('test', 'Data Augmentation\\Backgrounds\\LOTUS_2.jpg', '', '')