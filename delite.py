import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Tiger.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel for dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Display results
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Dilated Image')
plt.imshow(dilated, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
