import numpy as np
import cv2, os

def alphaTMean(im,alpha,n=5):
    img = np.zeros(im.shape,dtype=np.int16)
    
    v = (n-1)//2
    
    # Calculate the trim coefficient
    b = int((n*n)*(alpha))
    
    # Process the image
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            # Extract the window area
            block = im[max(i-v,0):min(i+v+1,im.shape[0]), max(j-v,0):min(j+v+1,im.shape[1])]

            # Reshape the neighborhood into a vector by flattening the 2D block
            wB = block.flatten()
            
            # Sort the vector into ascending order
            wB = np.sort(wB)
            len = wB.size
            
            # Trim b elements from each end of the vector
            if (b != 0):
                nwB = wB[b:len-b]
    
            # Calculate the mean of the trimmed vector
            tMean = nwB.mean()

            # Assign the values
            if (tMean > 0):
                img[i][j] = int(tMean)
    return img

import warnings
warnings.filterwarnings("ignore")

for file in os.listdir(os.getcwd()):
    if file.endswith('tif'):
        img = cv2.imread(file,0)
        file, ext = os.path.splitext(file)
        img = alphaTMean(img,0.5)
        cv2.imwrite(file+'_smoothened.png',img)

        
