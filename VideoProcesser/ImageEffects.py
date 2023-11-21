import cv2
import numpy as np
import copy
def apply_canny(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaus = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(gaus, 100, 200, apertureSize=3)

def apply_color(frame):
    # Define the range of gray colors in HSV
    new_frame = copy.deepcopy(frame)
    lower_gray = np.array([120, 120, 120], dtype=np.uint8)
    upper_gray = np.array([165, 165, 165], dtype=np.uint8)

    # Create a mask for the gray colors
    mask_gray = cv2.inRange(frame, lower_gray, upper_gray)

    # Convert the gray colors to light green in the original RGB image
    new_frame[mask_gray > 0] = [40, 255, 255]
    return new_frame

def apply_KNN(frame, bg_subtractor):
    frame = apply_color(frame)
    return bg_subtractor.apply(frame)
