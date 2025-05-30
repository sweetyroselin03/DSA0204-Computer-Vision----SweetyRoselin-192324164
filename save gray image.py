import cv2
image_path = r"C:\Users\trasr\OneDrive\Pictures\Screenshots\Screenshot 2025-04-30 140834.png"  # Replace with your image file path
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_fruits.jpg",gray)
