import cv2
img = cv2.imread(r"C:\Users\trasr\OneDrive\Pictures\Screenshots\Screenshot 2025-04-30 140834.png")
resized = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.imshow("original image",img)
cv2.imshow("resized image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
                    
