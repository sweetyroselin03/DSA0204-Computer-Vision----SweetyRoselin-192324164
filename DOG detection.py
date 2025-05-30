import cv2
import numpy as np

# Read the input image in grayscale
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg", cv2.IMREAD_GRAYSCALE)

# Apply two Gaussian blurs with different sigma (standard deviation) values
blur1 = cv2.GaussianBlur(image, (5, 5), 1)  # First Gaussian blur
blur2 = cv2.GaussianBlur(image, (5, 5), 2)  # Second Gaussian blur (more blur)

# Compute the Difference of Gaussians
dog = cv2.subtract(blur1, blur2)

# Optionally normalize to enhance visibility
dog_normalized = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX)
dog_normalized = dog_normalized.astype(np.uint8)

# Display the result (optional)
cv2.imshow('Difference of Gaussian (DoG)', dog_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
