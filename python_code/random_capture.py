import cv2
import os
import random


def extract_frames(video_path, output_folder, num_frames):
    cap = cv2.VideoCapture(video_path)

    # get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Exclude the first 150 frames and the last 75 frames
    excluded_frames = list(range(1, 151)) + list(range(total_frames - 75, total_frames + 1))

    # Generate frame indices within the specified range
    frame_indices = random.sample(
        [frame_idx for frame_idx in range(total_frames) if frame_idx not in excluded_frames],
        num_frames
    )

    os.makedirs(output_folder)

    # save the selected frames as images
    for idx, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            output_path = os.path.join(output_folder, f"frame_{idx}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Saved frame {idx + 1}/{num_frames}")
        else:   
            print(f"Error reading frame {frame_idx + 1}/{total_frames}")

    cap.release()

    print("Extraction complete.")
    print(frame_indices)


video_path = r"C:\intern_codes\python\val1\val1_2.avi"

output_folder = input('images를 저장할 폴더명을 영문 혹은 숫자 조합으로 입력하세요: ')

extract_frames(video_path, output_folder, 100)