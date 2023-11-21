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
    #frame_index = int(timestamp * fps)
    frame_index = timestamp

    # Jump to the specified frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    ret, frame = video.read()
    bg_sub = cv2.createBackgroundSubtractorKNN()
    if ret:
        # Crop the frame to the specified minimap region
        other = cv2.imread('MapTemplates/120.png')
        cropped_frame = frame[y:y+height, x:x+width]


        cv2.imwrite(output_image_path, cropped_frame)

    video.release()

# Parameters for the minimap region and timestamp
video_path = 'Video/fullraw_minimap.mp4'
output_image_path = 'Temp/'
timestamp_to_crop = 7300  # Timestamp in seconds

times = [216721, 216722, 216723, 216724, 216725, 216726, 216727, 216728, 216729, 216730, 216731, 216969, 216970, 216971, 216972, 216973, 216974, 216975, 216976, 216977, 216978, 216979, 216980, 216981, 216982]
# Crop the video at the specified timestamp and export as an image
for time in times:
    op = f'Temp/{time}.png'
    crop_video_at_timestamp(video_path, op, time, ASCENT)

