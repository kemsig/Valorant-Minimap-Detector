import cv2
import numpy as np

def read_labels(label_file_path):
    with open(label_file_path, 'r') as file:
        lines = file.readlines()
        labels = []
        for line in lines:
            parts = line.strip().split()
            label = {
                'class': int(parts[0]),
                'x_center': float(parts[1]),
                'y_center': float(parts[2]),
                'width': float(parts[3]),
                'height': float(parts[4])
            }
            labels.append(label)
    return labels

def draw_boxes(image, labels):
    img_height, img_width, _ = image.shape
    for label in labels:
        x_center = int(label['x_center'] * img_width)
        y_center = int(label['y_center'] * img_height)
        width = int(label['width'] * img_width)
        height = int(label['height'] * img_height)
        x_min = int(x_center - width / 2)
        y_min = int(y_center - height / 2)
        x_max = int(x_center + width / 2)
        y_max = int(y_center + height / 2)
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    return image

def main():
    '''
    image_path ='model\\yoloset_test\\images\\Train\\LOTUS_frame31.jpg'
    label_file_path = 'model\\yoloset_test\\labels\\Train\\LOTUS_frame31.txt' 

 
    image_path = 'Data Augmentation\\testset\\images\\test_2.jpg'
    label_file_path = 'Data Augmentation\\testset\\labels\\test_2.txt'
     '''

    image_path = 'model\\yoloset_with_daug_bb5px\\images\\Train\\daug_lotus_bbvar_5px_1.jpg'
    label_file_path = 'model\\yoloset_with_daug_bb5px\\labels\\Train\\daug_lotus_bbvar_5px_1.txt'

    image = cv2.imread(image_path)
    labels = read_labels(label_file_path)
    image_with_boxes = draw_boxes(image, labels)

    cv2.imshow('Image with Boxes', image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('Data Augmentation\\asd.png', image_with_boxes)

if __name__ == "__main__":
    main()
