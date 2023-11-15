import cv2
import ImageEffects as ie

ASCENT = {
        'x': 45,
        'y': 34,
        'width': 222,
        'height': 233
    }


def crop_video_at_timestamp(video_path, output_image_path, timestamp, map):
    x = map['x']
    y = map['y']
    height = map['height']
    width = map['width']

    video = cv2.VideoCapture(video_path)

    # Calculate frame index based on timestamp (assuming 30 fps)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_index = int(timestamp * fps)

    # Jump to the specified frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    ret, frame = video.read()
    bg_sub = cv2.createBackgroundSubtractorKNN()
    if ret:
        # Crop the frame to the specified minimap region
        other = cv2.imread('MapTemplates/120.png')
        cropped_frame = other[y:y+height, x:x+width]


        cv2.imwrite(output_image_path, cropped_frame)

    video.release()

# Parameters for the minimap region and timestamp
video_path = 'Video/fullraw_minimap.mp4'
output_image_path = 'ASCENT_KNN.png'
timestamp_to_crop = 7300  # Timestamp in seconds

# Crop the video at the specified timestamp and export as an image
crop_video_at_timestamp(video_path, output_image_path, timestamp_to_crop, ASCENT)
