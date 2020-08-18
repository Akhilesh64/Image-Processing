import cv2
import numpy as np

img1 = cv2.imread('Image_1.jpg',0)
img2 = cv2.imread('Image_2.jpg',0)
img3 = cv2.imread('Image_3.jpg',0)


def padding(img,a):
    padded_img = np.zeros((img.shape[0]+a*2,img.shape[1]+a*2))
    padded_img[a:-a,a:-a] = img
    return padded_img


def MedianFilter(img,b):
    d,c = img.shape
    a = b//2
    f_img = padding(img,a)
    filter_img = np.zeros(f_img.shape)
    for i in range(a,d+a+1):
        for j in range(a,c+a+1):
            filter_img[i,j] = np.median(f_img[i-a:i+a+1,j-a:j+a+1])
    return filter_img[a:-a,a:-a]

b = 7

cv2.imwrite('Median_Image_1.jpg',MedianFilter(img1,b))
cv2.imwrite('Median_Image_2.jpg',MedianFilter(img2,b))
cv2.imwrite('Median_Image_3.jpg',MedianFilter(img3,b))



