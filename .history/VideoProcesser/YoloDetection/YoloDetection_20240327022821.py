import random
import cv2
import numpy as np
from ultralytics import YOLO

classes = [
    'blue',
    'red',
    'dead blue',
    'dead red',
    'bomb'
]

# Generate random colors for class list
detection_colors = []
for i in range(len(classes)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))