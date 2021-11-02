import cv2

img_path= r"./Pics/test.jpg"
img = cv2.imread(img_path)

canny_edge1 = cv2.Canny(img, threshold1=60, threshold2=180)
canny_edge2 = cv2.Canny(img, threshold1=180, threshold2=230)
canny_edge3 = cv2.Canny(img, threshold1=180, threshold2=230, apertureSize=5, L2gradient=True)

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original", 360, 480)

cv2.namedWindow("canny_edge1", 0)
cv2.resizeWindow("canny_edge1", 360, 480)

cv2.namedWindow("canny_edge2", 0)
cv2.resizeWindow("canny_edge2", 360, 480)

cv2.namedWindow("canny_edge3", 0)
cv2.resizeWindow("canny_edge3", 360, 480)

cv2.imshow("Original", img)
cv2.imshow("canny_edge1", canny_edge1)
cv2.imshow("canny_edge2", canny_edge2)
cv2.imshow("canny_edge3", canny_edge3)
cv2.waitKey(0)
cv2.destroyAllWindows()