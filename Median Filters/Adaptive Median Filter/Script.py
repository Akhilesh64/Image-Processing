import cv2
import numpy as np

img1 = cv2.imread('Image_1.jpg',0)
img2 = cv2.imread('Image_2.jpg',0)
img3 = cv2.imread('Image_3.jpg',0)


def padding(img,a):
    padded_img = np.zeros((img.shape[0]+a*2,img.shape[1]+a*2))
    padded_img[a:-a,a:-a] = img
    return padded_img


def Level_A(f_img,x,y,s,Smax):
    mini_img = f_img[x-(s//2):x+(s//2)+1,y-(s//2):y+(s//2)+1]
    Zmin = np.min(mini_img)
    Zmed = np.median(mini_img)
    Zmax = np.max(mini_img)
    A1 = Zmed - Zmin
    A2 = Zmed - Zmax
    if A1>0 and A2<0:
        return Level_B(mini_img,s,Smax)
    else:
        s = s + 2
        if s <= Smax:
            return Level_A(f_img,x,y,s,Smax)
        else:
            return Zmed

def Level_B(mini_img,s,Smax):
    h,w = mini_img.shape
    Zmin = np.min(mini_img)
    Zmed = np.median(mini_img)
    Zmax = np.max(mini_img)
    Zxy = mini_img[h//2,w//2]
    B1 = Zxy - Zmin
    B2 = Zxy - Zmax
    if B1>0 and B2<0:
        return Zxy
    else:
        return Zmed

def AdaptiveMedianFilter(img,s,Smax):
    d,c = img.shape
    a = Smax//2
    f_img = padding(img,a)
    filter_img = np.zeros(f_img.shape)
    for i in range(a,d+a+1):
        for j in range(a,c+a+1):
            z = Level_A(f_img,i,j,s,Smax)
            filter_img[i,j] = z
    return filter_img[a:-a,a:-a]

s = 7
Smax = 11

cv2.imwrite('Adaptive_Image_1.jpg',AdaptiveMedianFilter(img1,s,Smax))
cv2.imwrite('Adaptive_Image_2.jpg',AdaptiveMedianFilter(img2,s,Smax))
cv2.imwrite('Adaptive_Image_3.jpg',AdaptiveMedianFilter(img3,s,Smax))

