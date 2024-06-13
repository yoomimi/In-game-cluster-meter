import cv2

video_path = r"C:\intern_codes\python\val1\val1_1.avi"

cap = cv2.VideoCapture(video_path)

total_frames = 0

# Check if video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Read frames and increment frame count
while True:
    # Read the next frame
    ret, frame = cap.read()

    # If frame reading is successful, increment the frame count
    if ret:
        total_frames += 1
    else:
        # If frame reading fails or end of video, break the loop
        break

# Release the video capture object
cap.release()

# Print the total frame count
print("Total frames:", total_frames)
