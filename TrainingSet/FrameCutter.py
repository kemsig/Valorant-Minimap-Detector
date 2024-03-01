import cv2

video_path = 'minimap_seen_video.mp4'
output_path = 'Images/'

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(fps*count))
    # Save each frame as an image
    cv2.imwrite(output_path + 'LOTUS_frame{:d}.jpg'.format(count), frame)
    count += 1

cap.release()
