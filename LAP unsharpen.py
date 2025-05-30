import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\cartoon face", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to get the blurred version
blurred = cv2.GaussianBlur(image, (5, 5), 1.0)

# Subtract blurred from original to get the mask
mask = cv2.subtract(image, blurred)

# Add the mask back to original to get the sharpened image
sharpened = cv2.add(image, mask)

# Display images
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Blurred')
plt.imshow(blurred, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Sharpened (Unsharp Masking)')
plt.imshow(sharpened, cmap='gray')

plt.tight_layout()
plt.show()
