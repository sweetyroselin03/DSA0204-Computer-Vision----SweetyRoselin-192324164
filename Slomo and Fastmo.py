import cv2

video_path = r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\2099568-hd_1920_1080_30fps.mp4" # Replace with your actual video file path

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Original FPS: {fps}")

def play_video(delay, title):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to first frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(title, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyWindow(title)

print("Playing video at normal speed...")
play_video(int(1000 / fps), "Normal Speed")

print("Playing video in slow motion...")
play_video(int(1000 / (fps / 2)), "Slow Motion")

print("Playing video in fast motion...")
play_video(int(1000 / (fps * 2)), "Fast Motion")

cap.release()
cv2.destroyAllWindows()
