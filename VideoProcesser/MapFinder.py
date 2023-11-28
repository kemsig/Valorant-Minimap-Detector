import cv2
import numpy as np
import ImageEffects as ie

# Load the minimap templates and Video
canny_template = cv2.imread('MapTemplates/LOTUS_CANNY.png', cv2.IMREAD_GRAYSCALE)
KNN_template = cv2.imread('MapTemplates/LOTUS_KNN.png', cv2.IMREAD_GRAYSCALE)
color_template = cv2.imread('MapTemplates/LOTUS_COLOR.png', cv2.IMREAD_COLOR)

video = cv2.VideoCapture('Video/fullraw_minimap.mp4')

# Variables for video properties
fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Desired start time
desired_start_time = 0  # Replace this with the timestamp from which you want to start processing

# Calculate the target frame number based on the desired start time
target_frame_number = int(desired_start_time * fps)
#end_frame_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Set the video capture object to the target frame
video.set(cv2.CAP_PROP_POS_FRAMES, target_frame_number)
# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('minimap_seen_video.mp4', fourcc, fps, (width, height))
def template_matcher(write_frame, compare_frame, threshold, template, match_type, color):
    # Match the template in the foreground mask
    result = cv2.matchTemplate(compare_frame, template, cv2.TM_CCOEFF_NORMED) #type
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Highlight the detected region with a green bounding box
        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        cv2.rectangle(write_frame, top_left, bottom_right, color, 2) # draw a green box
        out.write(write_frame)
        return True
    return False


#Get the stats of the video being played
detect_count = 0
total_frame_count = 0
canny_count = 0
KNN_count = 0
color_count = 0
failed_count = 0
end_frame = target_frame_number
# Create background subtractor using KNN method
background_subtractor = cv2.createBackgroundSubtractorKNN(550, 200, False)

#implementation for frame correcting
false_negative_frame = []
saved_frames = []
smoothing_frame_threshold = 45 # change according to taste
def smooth_frame(frame):
    global saved_frames,false_negative_frame
    if len(saved_frames) <= smoothing_frame_threshold:
        false_negative_frame += saved_frames
    saved_frames = []
    false_negative_frame.append(frame)
    for output_frame in false_negative_frame:
        cv2.imshow('Original Frame', output_frame)
        out.write(output_frame)
    false_negative_frame = []

# Iterate through the video frames
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    #Aapply the masks
    canny_mask = ie.apply_canny(frame)

    color_frame = ie.apply_color(frame)

    fg_mask = ie.apply_KNN(frame, background_subtractor)

    if template_matcher(frame, canny_mask, 0.2, canny_template, cv2.TM_CCOEFF_NORMED, (0, 255, 0)):
        smooth_frame(frame)
        detect_count += 1
        canny_count += 1
        failed_frames = 0
    elif template_matcher(frame, fg_mask, 0.4, KNN_template, cv2.TM_CCOEFF_NORMED, (0,0,255)):
        smooth_frame(frame)
        detect_count += 1
        KNN_count += 1
        failed_frames = 0
    elif template_matcher(frame, color_frame, 0.4, color_template, cv2.TM_CCOEFF_NORMED, (255,0,0)):
        smooth_frame(frame)
        detect_count += 1
        color_count += 1
        failed_frames = 0
    else:
        failed_count+=1
        saved_frames.append(frame)
        print(f'frames unsaved: {len(saved_frames)}')

    target_frame_number +=1

    # Show the processed frames in different windows

    cv2.imshow('Color Frame', color_frame)
    cv2.imshow('Background Subtraction', fg_mask)
    cv2.imshow('edges', canny_mask)

    total_frame_count += 1
    end_frame += 1

   # if target_frame_number + total_frame_count == int(7213 * fps): break
    if cv2.waitKey(1) & 0xFF == ord('q'): break


video.release()
cv2.destroyAllWindows()
out.release()



print('VIDEO STATS')
print(f'Percent Accuracy: {detect_count/total_frame_count * 100}%')
print(f'Smoothing Percent Accuracy: {(detect_count +len(false_negative_frame))/total_frame_count * 100}%')
print(f'Frames Failed: {failed_count}')
print(f'Canny Count+%: {canny_count} | {canny_count/total_frame_count * 100}%')
print(f'KNN Count+%: {KNN_count} | {KNN_count/total_frame_count * 100}%')
print(f'Color Count+%: {color_count} | {color_count/total_frame_count * 100}%')
print(f'From frame: {target_frame_number}---{end_frame}')