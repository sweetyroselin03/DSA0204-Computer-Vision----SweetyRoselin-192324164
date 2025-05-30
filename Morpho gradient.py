# import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread(r"C:\Users\trasr\OneDrive\Pictures\Screenshots\ABCDEF.png", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255,
                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((3, 3), np.uint8)


# invert the image
invert = cv2.bitwise_not(binr)

# use morph gradient
morph_gradient = cv2.morphologyEx(invert,
                                  cv2.MORPH_GRADIENT, 
                                  kernel)

# display the output
plt.imshow(morph_gradient, cmap='gray')
plt.title("Morphological Gradient")
plt.axis('off')  # Optional: hides the axis
plt.show()
