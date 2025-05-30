import cv2
import numpy as np
image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\sddefault.jpg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)
cv2.imwrite('log_edges.jpg', laplacian_abs)
cv2.imshow('Laplacian of Gaussian', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
