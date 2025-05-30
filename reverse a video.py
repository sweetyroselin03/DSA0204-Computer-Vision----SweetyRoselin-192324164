import cv2

cap = cv2.VideoCapture(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\1860079-uhd_2560_1440_25fps.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for i in reversed(range(frame_count)):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if not ret:
        continue
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
