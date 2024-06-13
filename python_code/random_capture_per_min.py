import cv2
import os
import random

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)

    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Number of intervals (900 frames each)
    num_intervals = total_frames // 900

    os.makedirs(output_folder, exist_ok=True)

    # Save the selected frames as images
    for interval in range(num_intervals):
        
        
        # Generate frame indices within the current interval and excluding excluded_frames
        frame_indices = random.sample(
            [frame_idx for frame_idx in range(interval * 900, (interval + 1) * 900)],
            90
        )

        for idx, frame_idx in enumerate(frame_indices):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if ret:
                output_path = os.path.join(output_folder, f"frame_{interval * 90 + idx + 1}.jpg")
                cv2.imwrite(output_path, frame)
                print(f"Saved frame {interval * 90 + idx + 1}/{num_intervals * 90}")
            else:
                print(f"Error reading frame {interval * 900 + frame_idx + 1}/{num_intervals * 90}")

    cap.release()

    print("Extraction complete.")

video_path = r"C:\intern_codes\python\val1(pro_split)\val1_2.avi"
output_folder = input('Enter the folder name to save images (use alphanumeric characters only): ')

extract_frames(video_path, output_folder)  # Will extract 900 frames in total (90 frames from each 900-frame interval)
