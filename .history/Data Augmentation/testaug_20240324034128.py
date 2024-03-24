import cv2
import random
# Load the main image
main_image = cv2.imread('Data Augmentation\\Backgrounds\\LOTUS_2.jpg')

m_height, m_width, _ = main_image.shape
# Load the smaller image
small_image = cv2.imread('Data Augmentation\\test_output\\bomb\\bomb_7c4e08c5-732b-49be-a92e-d354acaf6e9c.png', cv2.IMREAD_UNCHANGED)
s_height, s_width, _ = small_image.shape



y = random.randint(0, m_height-s_height)
# Define the coordinates where you want to place the smaller image
x_offset = 50  # Specify the x-coordinate for placement
y_offset = m_height-s_height-1  # Specify the y-coordinate for placement

# Get the shape of the smaller image
rows, cols, channels = small_image.shape

# Define the region of interest (ROI) on the main image
roi = main_image[y_offset:y_offset+rows, x_offset:x_offset+cols]

# Overlay the smaller image onto the ROI of the main image
for i in range(rows):
    for j in range(cols):
        roi[i, j] = small_image[i, j][:3]

# Display the resulting image
cv2.imshow('Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resulting image
cv2.imwrite('result_image.jpg', main_image)
