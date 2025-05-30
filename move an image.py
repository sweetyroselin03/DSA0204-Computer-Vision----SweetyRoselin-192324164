import cv2
import numpy as np

image = cv2.imread(r'C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg')
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

tx, ty = 100, 50  

translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

(height, width) = image.shape[:2]

moved_image = cv2.warpAffine(image, translation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Moved Image', moved_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
