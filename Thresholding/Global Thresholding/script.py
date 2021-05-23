import os, cv2, numpy as np

for file in os.listdir(os.getcwd()):
    if file.endswith('tif'):
        img = cv2.imread(file,0)
        thresh = int(input('Enter threshold value :'))
        name, ext = os.path.splitext(file)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] > thresh:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
        cv2.imwrite(name+'_threshold_'+str(thresh)+'.png',img)
