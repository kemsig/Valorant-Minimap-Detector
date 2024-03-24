import cv2
import random
# Load the map
main_image = cv2.imread('Data Augmentation\\Backgrounds\\LOTUS_2.jpg')

def draw_on_image_rand(imagepath):
    # Load the asset
    small_image = cv2.imread(imagepath, cv2.IMREAD_UNCHANGED)

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

draw_on_image('Data Augmentation\\test_output\\bomb\\bomb_7c4e08c5-732b-49be-a92e-d354acaf6e9c.png')

draw_on_image('Data Augmentation\\test_output\\fade red\\fade red_1f428ac5-4edb-4f80-b73b-ec5471183be1.png')


# Display the resulting image
cv2.imshow('Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resulting image
#cv2.imwrite('result_image.jpg', main_image)
