import cv2
img=cv2.imread('/home/innominds/Downloads/index1.jpeg',0)
print(img.shape)
print(img.ndim)
cv2.circle(img,(115,52),30,(255,0,0),3)
#cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()