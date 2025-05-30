from PIL import Image

# Open the image
image = Image.open(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\sddefault.jpg")

# Flip horizontally (left-right)
horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.show()

# Flip vertically (top-bottom)
vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.show()
