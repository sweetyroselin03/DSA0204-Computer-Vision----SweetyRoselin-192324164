import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\mountain.jpg")
rows, cols, ch = image.shape

# Define three points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50 , 200]])

# Define where those points should map to in the transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation to the image
transformed_image = cv2.warpAffine(image, M, (cols, rows))

# Save the result
cv2.imshow('transformed_image.jpg', transformed_image)
