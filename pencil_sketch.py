import cv2


img=cv2.imread("virat.jpeg")

shape_img=img.shape

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("grayscale image",imgGray)

# inv_img = cv2.bitwise_not(imgGray)
inv_img=255-imgGray
# cv2.imshow("invert image",inv_img)

# blur = cv2.blur(img,(5,5))
gaus_Blur = cv2.GaussianBlur(inv_img, (11,11),0)
# median_blur = cv2.medianBlur(img,5)
# cv2.imshow("blur image",gaus_Blur)

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def burnV2(image, mask):
  return 255-cv2.divide(255-image, 255-mask, scale=256)

img_blend = dodgeV2(imgGray, gaus_Blur)
result=cv2.imshow("pencil sketch", img_blend)


# print(shape_img)
cv2.waitKey(0)