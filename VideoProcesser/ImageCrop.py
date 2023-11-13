import cv2

LOTUS = {
        'x': 37,  # :3 kyun!
        'y': 54,
        'width': 225,
        'height': 199
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

    if ret:
        # Crop the frame to the specified minimap region
        cropped_frame = frame[y:y+height, x:x+width]
        sized = cv2.resize(cropped_frame, (1000, 1000), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(output_image_path, cropped_frame)

    video.release()

# Parameters for the minimap region and timestamp
video_path = 'y2mate.is - Loud vs Drx _ Valorant Champions 2023-ZQk2HM5GsIc-720p-1698720721.mp4'
output_image_path = 'noninterp.png'
timestamp_to_crop = 3075  # Timestamp in seconds

# Crop the video at the specified timestamp and export as an image
crop_video_at_timestamp(video_path, output_image_path, timestamp_to_crop, LOTUS)
