import cv2
import numpy as np

def combine_videos(video_path, output_path):
    # Open videos
    video = cv2.VideoCapture(video_path)

    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    minimap_w = 400
    minimap_h = 400

    scoreboard_w = 751-528
    scoreboard_h = 47-7

    # Find the maximum height of the two videos
    max_height = max(minimap_h, scoreboard_h)

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (minimap_w + scoreboard_w, max_height))

    print("Combining videos Start")

    while True:
        # Read frames from both videos
        ret, frame = video.read()

        if not ret:
            break  # Break the loop if both videos end

        # Create black backgrounds
        black_background1 = np.zeros((max_height, minimap_w, 3), dtype=np.uint8)
        black_background2 = np.zeros((max_height, scoreboard_w, 3), dtype=np.uint8)

        # If there's a frame in video1, place it on the black background1

        cropped_map = frame[0:400, 0:400]
        cropped_score = frame[7:47, 528:751]

        black_background1[:minimap_h, :] = cropped_map

        # If there's a frame in video2, place it on the black background2
        black_background2[:scoreboard_h, :] = cropped_score

        # Concatenate the frames horizontally
        combined_frame = np.concatenate((black_background1, black_background2), axis=1)

        # Write the combined frame to the output video
        out.write(combined_frame)

        cv2.imshow('Combined Video', combined_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and writer objects
    video.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage
video_path = 'Video/Loud vs Drx _ Valorant Champions 2023.mp4'
output_path = 'Video/output_combined.mp4'

combine_videos(video_path, output_path)
