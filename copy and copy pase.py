import cv2

# Load the main image (destination)
main_image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Tiger.jpg")

# Load the image to crop from (source)
source_image = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\Tiger crop.jpg")

# Crop a region from the source image (adjust coordinates as needed)
cropped = source_image[50:200, 100:250]  # [y1:y2, x1:x2]

# Define top-left corner where you want to paste in the main image
x_offset, y_offset = 50, 50
x_end = x_offset + cropped.shape[1]
y_end = y_offset + cropped.shape[0]

# Paste the cropped image into the main image
main_image[y_offset:y_end, x_offset:x_end] = cropped

# Display the result
cv2.imshow('Pasted Image', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
