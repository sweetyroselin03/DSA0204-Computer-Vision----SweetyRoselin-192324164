from PIL import Image, ImageOps
img1=Image.open(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg")
img2=ImageOps.grayscale(img1)
img2.show()
