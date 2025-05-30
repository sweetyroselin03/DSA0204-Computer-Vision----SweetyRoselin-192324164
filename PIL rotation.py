from PIL import Image
image = Image.open(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\LION.jpg")
angle = 45 
rotated_image = image.rotate(angle)
rotated_image.show()
