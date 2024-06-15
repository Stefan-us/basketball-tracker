import cv2

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_list = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_list.append(frame)
    cap.release()
    return frame_list

if __name__ == "__main__":
    video_path = 'path_to_your_video.mp4'
    frames = extract_frames(video_path)
    print(f"Extracted {len(frames)} frames from the video.")
