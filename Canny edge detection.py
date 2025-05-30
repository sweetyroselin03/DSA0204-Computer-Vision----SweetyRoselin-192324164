import cv2
from matplotlib import pyplot as plt

image_path = r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\elephants.jpg"  # Replace with your image file path
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

# Apply Canny edge detector
edges = cv2.Canny(blurred, threshold1=100, threshold2=200)

# Display results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Canny Edges")
plt.imshow(edges, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()
