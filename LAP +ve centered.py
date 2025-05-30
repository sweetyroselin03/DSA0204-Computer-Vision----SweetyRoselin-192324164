import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\wall image.jpg", cv2.IMREAD_GRAYSCALE)

# Define Laplacian sharpening kernel with positive center coefficient
sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

# Apply the kernel to the image
sharpened = cv2.filter2D(image, -1, sharpen_kernel)

# Display results
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Sharpened')
plt.imshow(sharpened, cmap='gray')

plt.tight_layout()
plt.show()
