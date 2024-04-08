#histogram equalization
#image enhancement
from  PIL import Image
import cv2

#read the image
img = cv2.imread('download.jpeg')

#preparation for CLAHE
clahe = cv2.createCLAHE()

#to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#applying enhancement
enh_img = clahe.apply(gray_img)

#save to file
cv2.imwrite('enhanced.jpeg',enh_img)

print("done enhancing")