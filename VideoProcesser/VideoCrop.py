import cv2
import ImageEffects as ie

# Map Constants
LOTUS = {
        'x': 35,  # :3 kyun!
        'y': 53,
        'width': 227,
        'height': 202
    }
# Function to crop the video to the region containing the minimap
def crop_video(video_path, output_path, map):
    x = map['x']
    y = map ['y']
    width = map['width']
    height = map['height']

    video = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    num = 1
    out = cv2.VideoWriter(output_path, fourcc, fps, (751-528, 40))
    print("Cropping Start")
    while True:
        ret, frame = video.read()

        if not ret:
            break

        #cropped_frame = frame[y:y+height, x:x+width]
        cropped_score = frame[7:47, 528:751]
        if cropped_score.shape[0] > 0 and cropped_score.shape[1] > 0:
            out.write(cropped_score)


    video.release()
    out.release()
    print("Process Successful")

# Define the coordinates and size of the minimap region
# Example values, please adjust according to your video
minimap_x = 37  # X coordinate of the top-left corner of the minimap
minimap_y = 54  # Y coordinate of the top-left corner of the minimap
minimap_width = 225  # Width of the minimap
minimap_height = 199  # Height of the minimap

# Path to your input video and desired output path for the cropped video
input_video_path = 'Video/Loud vs Drx _ Valorant Champions 2023.mp4'
output_video_path = 'Video/minis.mp4'

# Crop the video based on the minimap coordinates and dimensions
crop_video(input_video_path, output_video_path, LOTUS)

