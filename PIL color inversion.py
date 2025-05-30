from PIL import Image, ImageChops
img=Image.open(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg")
inv_img=ImageChops.invert(img)
inv_img.show()
