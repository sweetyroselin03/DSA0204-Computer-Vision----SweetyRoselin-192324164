import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\animated face.jpg", cv2.IMREAD_GRAYSCALE)

# Set A value (amplification factor)
A = 2  # Try 1, 1.5, 2...

# Define High-Boost kernel (8-neighbor version)
high_boost_kernel = np.array([
    [-1, -1, -1],
    [-1, A + 8, -1],
    [-1, -1, -1]
])

# Apply high-boost filtering
sharpened = cv2.filter2D(image, -1, high_boost_kernel)

# Display results
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title(f'High-Boost Sharpened (A={A})')
plt.imshow(sharpened, cmap='gray')

plt.tight_layout()
plt.show()
