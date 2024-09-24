import cv2
import numpy as np
import os
from pathlib import Path



def Color_Equalize(img):


    img[:,:,1] = cv2.equalizeHist(img[:,:,1])
    img[:,:,2] = cv2.equalizeHist(img[:,:,2])
    img[:,:,0] = cv2.equalizeHist(img[:,:,0])

    return img

def Auto_Equalize(img):

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:,:,0])
    # convert the YUV image back to RGB format
    img_yuv[:, :, 0] = clahe.apply(img)
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return img_output


def New_Image_File_Name(filename, suffix):
    return '/'+filename.strip('.jpg')+suffix+'.jpg'


if __name__ == '__main__':

    source_dir = Path()
    gray_equal_dir = Path('./gray_equalized')
    col_equal_dir = Path('./color_equalized')

    #list_of_dirs = [gray_equal_dir, col_equal_dir]
    list_of_dirs = [col_equal_dir]

    for d in list_of_dirs:
        if not d.exists():
            os.makedirs(str(d))


    for file in source_dir.iterdir():
        
        filename = str(file)
        if filename.endswith('.jpg'):
            
            img = cv2.imread(filename)
            
            '''
            img_ae = Auto_Equalize(img)
            img_name = New_Image_File_Name(filename, '-ae')
            cv2.imwrite(str(auto_equal_dir)+img_name, img_ae)
            '''


            img_ce = Color_Equalize(img)
            img_name = New_Image_File_Name(filename, '-ce')
            cv2.imwrite(str(col_equal_dir)+img_name, img_ce)


    print('done')