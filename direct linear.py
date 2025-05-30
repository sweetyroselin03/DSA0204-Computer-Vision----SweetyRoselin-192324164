import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load source and destination images
src_img = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\elephants.jpg")         # Use your own source image
dst_img = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg")    # Use your own destination image

# Resize for easier visualization
src_img = cv2.resize(src_img, (400, 300))
dst_img = cv2.resize(dst_img, (400, 300))

# Define 4 corresponding points (in real applications, use cv2.selectROI or feature matching)
src_points = np.float32([[50, 50], [300, 50], [50, 250], [300, 250]])       # corners in source
dst_points = np.float32([[60, 70], [310, 60], [80, 260], [330, 250]])       # where they should map in destination

# Compute homography matrix using DLT
H, status = cv2.findHomography(src_points, dst_points, method=0)

# Apply homography to warp the source image onto destination plane
warped_img = cv2.warpPerspective(src_img, H, (dst_img.shape[1], dst_img.shape[0]))

# Visualize everything
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Source Image")
plt.imshow(cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title("Destination Image")
plt.imshow(cv2.cvtColor(dst_img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title("Warped Source (DLT Result)")
plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
