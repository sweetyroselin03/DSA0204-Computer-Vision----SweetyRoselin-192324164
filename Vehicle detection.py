# 39. Vehicle Detection (Using Haar Cascade - sample)
import cv2

haar_cascade = r"C:\Users\trasr\Downloads\cars.xml"
video = r"C:\Users\trasr\Downloads\13730805_1080_1920_30fps.mp4"

cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    if not ret:
        break

    # Detects cars of different sizes directly in the BGR image
    cars = car_cascade.detectMultiScale(frames, 1.1, 1)

    # Draw rectangle around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Resize frame to medium size
    medium_frame = cv2.resize(frames, (960, 540))
    cv2.imshow('video', medium_frame)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
