import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

gray = cv2.imread('Image.jpg',cv2.IMREAD_GRAYSCALE)
color = cv2.imread('Image.jpg')

# Histogram Equalization 

def cdf(img):
    cdf_img = dict()
    for i in range(256):
        cdf_img[i] = len(img[img==i])

    for i in range(1,256):
        cdf_img[i] += cdf_img[i-1]
    return cdf_img


def histeq(img):
    cdf_img = cdf(img)
    for i in range(256):
        cdf_img[i] = int(255 * cdf_img[i]/(img.shape[0]*img.shape[1]))

    # map
    himgf = np.zeros(img.shape)
    himgf[:,:] = img

    for i in range(256):
        himgf[img==i] = cdf_img[i]


    return himgf

cv2.imwrite('new_img_gray.jpg',histeq(gray))

colorf = np.zeros(color.shape)
colorf[:,:,0] = histeq(color[:,:,0])
colorf[:,:,1] = histeq(color[:,:,1])
colorf[:,:,2] = histeq(color[:,:,2])
colorf = colorf.astype(int)

cv2.imwrite('new_img_color.jpg',colorf)

