import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in color
img = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Tiger.jpg")

# Convert to grayscale for erosion/dilation
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion and dilation
img_erosion = cv2.erode(gray, kernel, iterations=1)
img_dilation = cv2.dilate(gray, kernel, iterations=1)

# Convert original image to RGB for matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show images side by side
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Erosion")
plt.imshow(img_erosion, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Dilation")
plt.imshow(img_dilation, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
