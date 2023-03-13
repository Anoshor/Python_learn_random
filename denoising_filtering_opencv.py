import cv2
import numpy as np
from matplotlib import pyplot as plt


# deNOISING

path = r'C:\Users\anosh\OneDrive\Desktop\pygame\python_learn\images\DSimages\BSE_Google_noisy.jpg'

img = cv2.imread(path, 1)



kernel = np.ones((3,3), np.float32)/25 
#pick appropriate size-- reduce blurring
#normalizing-- energy of entire kernel remains 1

filt_2D = cv2.filter2D(img, -1, kernel=kernel)    
blur=cv2.blur(img,(3,3))
gaussian_blur = cv2.GaussianBlur(img,(3,3),0) #gaussian-- imagine bell shaped 2d graph prodruding at center
median_blur = cv2.medianBlur(img,3) #when u wanna retain the edges
bilateral_blur = cv2.bilateralFilter(img,9,75,75) #retains edges.. removes noise better(?) idk tbh

cv2.imshow("original", img)
cv2.imshow("2D custom filter", filt_2D)
cv2.imshow("blurred image",blur)
cv2.imshow("gaussian",gaussian_blur)
cv2.imshow("median blur", median_blur)
cv2.imshow("bilateral blur", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
