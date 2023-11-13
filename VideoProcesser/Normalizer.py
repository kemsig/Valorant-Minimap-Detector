import cv2
import numpy as np

def normalize_video(video_path):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Get video properties
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object to save the normalized video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('normalized_video.avi', fourcc, fps, (width, height))

    while video_capture.isOpened():
        ret, frame = video_capture.read()

        if not ret:
            break

        # Normalize the frame pixel values to [0, 1]
        normalized_frame = frame / 255.0  # Assuming the pixel values range from 0 to 255

        # You can perform further processing on the normalized_frame if needed

        # Convert back to 8-bit unsigned integer
        normalized_frame = (normalized_frame * 255).astype(np.uint8)

        # Write the frame to the output video
        out.write(normalized_frame)

        cv2.imshow('Normalized Video', normalized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()