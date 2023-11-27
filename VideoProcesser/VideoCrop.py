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
    bg_sub = cv2.createBackgroundSubtractorKNN(550, 200, False)
    num = 1
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    print("Cropping Start")
    while True:
        ret, frame = video.read()

        if not ret:
            break

        cropped_frame = frame[y:y+height, x:x+width]




        if cropped_frame.shape[0] > 0 and cropped_frame.shape[1] > 0:
            canny = ie.apply_canny(cropped_frame)
            color = ie.apply_color(cropped_frame)
            KNN = ie.apply_KNN(cropped_frame, bg_sub)
            print(num)
            cv2.imwrite(f'Temp/Canny/{num}.png', canny)
            cv2.imwrite(f'Temp/Color/{num}.png', color)
            cv2.imwrite(f'Temp/KNN/{num}.png', KNN)
            num +=1
            out.write(cropped_frame)


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
input_video_path = 'Video/y2mate.is - Loud vs Drx _ Valorant Champions 2023-ZQk2HM5GsIc-720p-1700701607.mp4'
output_video_path = 'Video/minis.mp4'

# Crop the video based on the minimap coordinates and dimensions
crop_video(input_video_path, output_video_path, LOTUS)

