from PIL import Image
img=Image.open(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\elephants.jpg")
width,height=img.size
left=5
top=height/4
right=164
bottom = 3*height/4
img1=img.crop((left,top,right,bottom))
img1.show()
