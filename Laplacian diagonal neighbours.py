import cv2
import numpy as np

# Load image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\cartoon face", cv2.IMREAD_GRAYSCALE)

# Define Laplacian kernel including diagonal neighbors (8-connected)
laplacian_diag_kernel = np.array([[1, 1, 1],
                                  [1, -8, 1],
                                  [1, 1, 1]], dtype=np.float32)

# Apply the filter
laplacian_diag = cv2.filter2D(image, cv2.CV_64F, laplacian_diag_kernel)
laplacian_diag = cv2.convertScaleAbs(laplacian_diag)

# Display result
cv2.imshow('Laplacian with Diagonal Neighbors (8-connected)', laplacian_diag)
cv2.waitKey(0)
cv2.destroyAllWindows()
