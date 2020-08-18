import cv2
import numpy as np
import math


# Laplacian Edge Detector

image = cv2.imread('Image.jpg',0)

# Filters for calculating Laplacian(uncomment the one you want)

conv_kernel = np.array([[-1, -1, -1, -1, -1], 
                        [-1, -1, -1, -1, -1], 
                        [-1, -1, 24, -1, -1],
                        [-1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1]])

'''conv_kernel = np.array([[0,1,0],
                        [1,-4,1],
                        [0,1,0]])

conv_kernel = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])'''

#Function to calculate 2D convolution of two matrix

def conv2d(image, kernel):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1 
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) 
    return new_image


cv2.imwrite('Laplacian_Image.jpg',conv2d(image,conv_kernel))


