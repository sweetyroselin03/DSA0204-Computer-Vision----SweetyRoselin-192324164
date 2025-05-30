import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Aeroplane.jpg")

# Define homography matrix (example)
H = np.array([
    [1.2, 0.1, 30],
    [0.1, 1.1, 50],
    [0.0005, 0.0003, 1]
])

# Get output image size
height, width = image.shape[:2]

# Apply perspective transformation
warped_image = cv2.warpPerspective(image, H, (width, height))

# Save or display
cv2.imwrite('warped_image.jpg', warped_image)
cv2.imshow('Warped', warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
