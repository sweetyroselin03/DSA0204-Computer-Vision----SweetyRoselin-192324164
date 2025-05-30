import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Aeroplane.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel along Y (dx=0, dy=1)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit and display
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imshow('Sobel Y - Horizontal Edges', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
