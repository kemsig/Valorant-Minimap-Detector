import cv2
import random
import os

root_path = 'Data Augmentation\\test_output'

fn = 'bomb'

def get_rand_img(folder_name):
    folder_path = os.path.join(root_path, folder_name)
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    random_png = random.choice(png_files)
    return os.path.join(folder_path, random_png)


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

# put pixels on position
#
#




for class_name, int_value in classes.items():
    print(c)
    # get class image and num
    #
    names = ['fade', 'kj', 'raze', 'omen', 'viper']
    is_char = False
    for count in c:
        char_choice = c
        # pick a random character exclusive
        if names:
            if char_choice == 'max_blue':
                picked_name = random.choice(names)
                print(picked_name)
                char_choice = f'{picked_name} blue'
                names.remove(picked_name)
                is_char = True
            elif char_choice == 'max_red':
                picked_name = random.choice(names)
                char_choice = f'{picked_name} red'
                names.remove(picked_name)
                is_char = True
            
        # get a random image of the character
        char_img = get_rand_img(char_choice)






'''
# Load the map
main_image = cv2.imread('Data Augmentation\\Backgrounds\\LOTUS_2.jpg')

def write_to_image_rand(main_image, asset_image):
    # Load the asset
    small_image = cv2.imread(asset_image, cv2.IMREAD_UNCHANGED)

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

write_to_image_rand(main_image, 'Data Augmentation\\test_output\\bomb\\bomb_7c4e08c5-732b-49be-a92e-d354acaf6e9c.png')

write_to_image_rand(main_image, 'Data Augmentation\\test_output\\fade red\\fade red_1f428ac5-4edb-4f80-b73b-ec5471183be1.png')


# Display the resulting image
cv2.imshow('Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resulting image
#cv2.imwrite('result_image.jpg', main_image)
'''