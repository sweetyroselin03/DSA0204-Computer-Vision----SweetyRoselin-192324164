# Python code to read image
import cv2
img = cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\elephants.jpg", cv2.IMREAD_COLOR)
cv2.imshow("fruits", img)

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_scale",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
