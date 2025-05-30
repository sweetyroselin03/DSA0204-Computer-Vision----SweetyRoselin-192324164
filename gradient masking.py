import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg", cv2.IMREAD_GRAYSCALE)

# Define Prewitt-like gradient masks
gx_kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

gy_kernel = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

# Compute gradients
grad_x = cv2.filter2D(image, -1, gx_kernel)
grad_y = cv2.filter2D(image, -1, gy_kernel)

# Combine gradients to get edge map
edges = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

# Sharpen the image by adding edges to the original
sharpened = cv2.add(image, edges)

# Display results
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Edge Map (Gradient)')
plt.imshow(edges, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Sharpened Image')
plt.imshow(sharpened, cmap='gray')

plt.tight_layout()
plt.show()
