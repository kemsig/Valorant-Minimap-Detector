import cv2

# Load the minimap template
minimap_template = cv2.imread('ASCENT.png')  # Replace with the path to your cropped minimap template

# Load your video file
video = cv2.VideoCapture('fullrawcropped.mp4')  # Replace with the path to your video file

# Define a threshold for matching
threshold = 0.65  # Adjust as needed, represents the minimum threshold for a match

# Function to check if the minimap is present in a frame
def is_minimap_present(frame):
    # convert to gray scale for improved acc
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(frame, minimap_template, cv2.TM_CCOEFF_NORMED)
    loc = cv2.minMaxLoc(res)[1]
    return loc >= threshold

# Variables for video properties
fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Desired start time
desired_start_time = 7202  # Replace this with the timestamp from which you want to start processing

# Calculate the target frame number based on the desired start time
target_frame_number = int(desired_start_time * fps)

# Set the video capture object to the target frame
video.set(cv2.CAP_PROP_POS_FRAMES, target_frame_number)

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('minimap_seen_video.mp4', fourcc, fps, (width, height))

x = 45
y = 34
height = 233
width = 222

# Iterate through the video frames
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Check if the minimap is present in the current frame
    if is_minimap_present(frame):
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)  # Add a green bounding box around the detected minimap
        out.write(frame)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

