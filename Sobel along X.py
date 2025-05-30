import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Aeroplane.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel along X (dx=1, dy=0)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Convert to 8-bit and display
sobel_x = cv2.convertScaleAbs(sobel_x)

cv2.imshow('Sobel X - Vertical Edges', sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
