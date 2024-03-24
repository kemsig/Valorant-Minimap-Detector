import cv2
import numpy as np
import datetime
import random
import os

def write_to_image(image, width, height, character_name, c_width, c_height, x_off, y_off):
    # get random position for object
    x = random.randint(0, width - c_width - x_off)
    y = random.randint(0, height - c_height - y_off)
    

def get_rand_img(character, is_char):
    # parse the underscore

    print("got class")

def generate_data_YOLO(name, image_path, out_image_path, out_label_path):
    # open image
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    
    # get random amount of characters to add
    max_blue = random.randint(0, 5)
    max_red = random.randint(0, 5)
    dead_blue = 5-max_blue
    dead_red = 5-max_red
    bomb = random.randint(0, 1)
    
    classes = {"max_blue":max_blue,
               "max_red":max_red,
               "dead_blue":dead_blue,
               "dead_red":dead_red,
               "bomb":bomb
            }
    
    # put pixels on position
    #
    #
    
    for c in classes:
        # get class image and num
        #
        class_num = classes.index(c)
        names = ['fade', 'kj', 'raze', 'omen', 'viper']
        is_char = False
        for count in c:
            char_choice = c
            # pick a random character exclusive
            if class_num == 0:
                picked_name = random.choice(names)
                char_choice = f'{names.remove(picked_name)} blue'
                is_char = True
            elif class_num == 1:
                picked_name = random.choice(names)
                char_choice = f'{names.remove(picked_name)} red'
                is_char = True
                
            # get a random image of the character
            char_img = get_rand_img(char_choice, is_char)
                
            write_to_image(
                image=img,
                width=width,
                height=height,
                character_name= char_img,
                c_width= "PLACEHOLDER",
                c_height= "PLACEHOLDER"
            )
            
            # calculate label positions in yolo format
            # <object-class> <x> <y> <width> <height>
            x_center = 0
            y_center = 0
            norm_width = 0
            norm_height = 0
            


            # append to label file
            output_file = os.path.join(out_label_path, f"{name}.txt")
            
            with open(output_file, 'a') as f:
                f.write(f"{class_num} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}")
    
            # put character image on spot
    
    # save image
    #cv2.imwrite(out_image_path)
max_blue = random.randint(0, 5)
max_red = random.randint(0, 5)
dead_blue = 5-max_blue
dead_red = 5-max_red
bomb = random.randint(0, 1)

classes = {"max_blue":max_blue,
        "max_red":max_red,
        "dead_blue":dead_blue,
        "dead_red":dead_red,
        "bomb":bomb
    }

for c in classes:
    print(c)