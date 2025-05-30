import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread(r"C:\Users\trasr\Downloads\pexels-ferarcosn-190819.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load a valid Haar cascade (example: frontal face)
stop_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Detect
found = stop_cascade.detectMultiScale(img_gray, minSize=(20, 20))

# Draw rectangles
for (x, y, w, h) in found:
    cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 255, 0), 5)

# Show result
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
