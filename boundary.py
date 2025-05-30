import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Tiger.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel for erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Extract boundary by subtracting eroded image from the original
boundary = cv2.subtract(image, eroded)

# Display results
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')


plt.subplot(1, 3, 2)
plt.title('Boundary')
plt.imshow(boundary, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
