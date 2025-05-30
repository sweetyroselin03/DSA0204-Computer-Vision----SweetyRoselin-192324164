import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Aeroplane.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel in both directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

cv2.imshow('Sobel XY - Gradient Magnitude', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
