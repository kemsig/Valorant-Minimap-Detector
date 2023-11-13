import cv2

# Load the minimap template
minimap_template = cv2.imread('ASCENT.png', cv2.IMREAD_GRAYSCALE)  # Replace with the path to your cropped minimap template

# Load your video file
video = cv2.VideoCapture('fullrawcropped.mp4')  # Replace with the path to your video file

# Variables for video properties
fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Desired start time
desired_start_time = 7222  # Replace this with the timestamp from which you want to start processing

# Calculate the target frame number based on the desired start time
target_frame_number = int(desired_start_time * fps)

# Set the video capture object to the target frame
video.set(cv2.CAP_PROP_POS_FRAMES, target_frame_number)

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('minimap_seen_video.mp4', fourcc, fps, (width, height))

# Create background subtractor using KNN method
background_subtractor = cv2.createBackgroundSubtractorKNN()
cv2.imshow("template", background_subtractor.apply(minimap_template))
# Iterate through the video frames
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = background_subtractor.apply(frame)

    # Match the template in the foreground mask
    result = cv2.matchTemplate(fg_mask, minimap_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Set a threshold for template matching
    threshold = 0.8
    if max_val >= threshold:
        # Highlight the detected region with a green bounding box
        top_left = max_loc
        bottom_right = (top_left[0] + minimap_template.shape[1], top_left[1] + minimap_template.shape[0])
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        out.write(frame)

    # Show the processed frames in different windows
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Background Subtraction', fg_mask)
    cv2.imshow('edges', cv2.Canny(frame, 100, 250, apertureSize=3))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
