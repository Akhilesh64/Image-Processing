import cv2
import numpy as np

img = cv2.imread('Fig0323(a)(mars_moon_phobos).tif')

# Calculating cdf

def cdf(img):
    cdfimg = dict()
    for i in range(256):
        cdfimg[i] = len(img[img==i])  # calculating frequency of each pixel value
    
    for i in range(1,256):
        cdfimg[i] += cdfimg[i-1]   # calculating cdf
    return cdfimg

# Histogram Equalization

def histogramEqualization(img):

    # Treating channels of color image as different images and then restacking them again

    himgf = np.zeros(img.shape,dtype=np.uint8)
    for i in range(3):  # looping through the 3 channels
        cdfimg = cdf(img[:,:,i])
        cdf_vals = cdfimg.values()
        cdf_max = max(cdf_vals)
        cdf_min = min(cdf_vals)
        for j in range(256):
            cdfimg[j] = int(255 * (cdfimg[j]-cdf_min)/(cdf_max-cdf_min))  #  normalizing cdf

        # map
        himg = np.zeros(img[:,:,i].shape,dtype=np.uint8)
        himg[:,:] = img[:,:,i]

        for j in range(256):
            himg[img[:,:,i]==j] = cdfimg[j]    # replacing the old pixel values with the new equalized pixel values obtained
        himgf[:,:,i] = himg   # stacking the histogram equalized channels
    
    return himgf

heqimg = histogramEqualization(img)

cv2.imwrite("Fig0323(a)(mars_moon_phobos)_histequalized.jpg",heqimg)
