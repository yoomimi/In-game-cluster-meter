import cv2

def exclude_frames(video_path, excluded_frames, output_path):
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec for the output video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    # Create VideoWriter object to save the output video
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()

        # Break the loop if there are no more frames
        if not ret:
            break

        frame_idx = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # Exclude specific frames
        if frame_idx not in excluded_frames:
            out.write(frame)

    # Release VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    print(f"Excluded frames {excluded_frames} and saved the rest to {output_path}")

# Input video path
video_path = r"C:\intern_codes\python\val1\val1_1.avi"

# Output video path
output_path = r"C:\intern_codes\python\val1\val1_2.avi"

# Frames to exclude
excluded_frames = list(range(1, 35))  # This will exclude frames 1 to 460
excluded_frames.extend([1,90,267])  # This will exclude frames 10 and 85
excluded_frames.extend(list(range(236,267)))


# Exclude frames and save the output video
exclude_frames(video_path, excluded_frames, output_path)
