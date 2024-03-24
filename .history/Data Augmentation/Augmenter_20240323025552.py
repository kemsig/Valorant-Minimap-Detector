import cv2
import numpy as np
import datetime
import random
import os

def write_to_image(image, width, height, character_name, c_width, c_height):
    # get random position for object
    x = random.randint(0, width - c_width)
    y = random.randint(0, height - c_height)
    

def get_rand_img(character):
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

        for count in c:
            char_choice = c
            # pick a random character exclusive
            if class_num == 0 or class_num == 1:
                picked_name = random.choice(names)
                char_choice = names.remove(picked_name)
                
            # get a random image of the character
            # get_rand_img(character)
                
            write_to_image(
                image=img,
                width=width,
                height=height,
                character_name= char_choice,
                c_width= "PLACEHOLDER",
                c_height= "PLACEHOLDER"
            )
            
            # calculate label positions in yolo format
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