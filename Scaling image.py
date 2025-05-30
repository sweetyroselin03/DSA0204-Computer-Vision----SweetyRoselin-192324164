import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\CUTE PANDA.webp')

bigger = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Display the original, bigger, and smaller images


cv2.imshow('Bigger Image (2x)', bigger)
cv2.imshow('Smaller Image (0.5x)', smaller)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
