import cv2
image_path = r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\elephants.jpg"  # Replace with your image file path
image = cv2.imread(image_path)


# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 1.4)
cv2.imshow("blurred Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
