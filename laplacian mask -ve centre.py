import cv2
import numpy as np

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\CUTE PANDA.webp", cv2.IMREAD_GRAYSCALE)

# Define Laplacian kernel (4-connected, negative center)
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]], dtype=np.float32)

# Apply filter using cv2.filter2D
laplacian_image = cv2.filter2D(image, cv2.CV_64F, laplacian_kernel)
laplacian_image = cv2.convertScaleAbs(laplacian_image)  # Convert to 8-bit image

# Show result
cv2.imshow('Laplacian (Negative Center)', laplacian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
