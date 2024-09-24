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

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # equalize the histogram of the Y channel
    # img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))
    # convert the YUV image back to RGB format
    img_yuv[:, :, 0] = clahe.apply(img)
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_GRAY2BGR)

    #cv2.imshow('Color input image', img)

    return img_output

def White_Balance(img):

    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    avg_a = np.average(img_lab[:, :, 1])
    avg_b = np.average(img_lab[:, :, 2])
    img_lab[:, :, 1] = img_lab[:, :, 1] - ((avg_a - 128) * (img_lab[:, :, 0] / 255.0) * 1.1)
    img_lab[:, :, 2] = img_lab[:, :, 2] - ((avg_b - 128) * (img_lab[:, :, 0] / 255.0) * 1.1)
    img_output = cv2.cvtColor(img_lab, cv2.COLOR_LAB2BGR)

    return img_output


def New_Image_File_Name(filename, suffix):
    return '/'+filename.strip('.jpg')+suffix+'.jpg'


if __name__ == '__main__':

    source_dir = Path()
    white_balanced_dir = Path('./white_balance')
    gray_equal_dir = Path('./gray_equalized')
    both_dir = Path('./both')
    col_equal_dir = Path('./color_equalized')

    #list_of_dirs = [white_balanced_dir, gray_equal_dir, both_dir, col_equal_dir]
    list_of_dirs = [col_equal_dir]

    for d in list_of_dirs:
        if not d.exists():
            os.makedirs(str(d))


    for file in source_dir.iterdir():
        
        filename = str(file)
        if filename.endswith('.jpg'):
            
            img = cv2.imread(filename)
            
            '''
            img_wb = White_Balance(img)
            img_name = New_Image_File_Name(filename, '-wb')
            cv2.imwrite(str(white_balanced_dir)+img_name, img_wb)
            '''

            '''
            img_ae = Auto_Equalize(img)
            img_name = New_Image_File_Name(filename, '-ae')
            cv2.imwrite(str(auto_equal_dir)+img_name, img_ae)
            '''

            '''
            img_both = Auto_Equalize(img_wb)
            img_name = New_Image_File_Name(filename, '-both')
            cv2.imwrite(str(both_dir)+img_name, img_both)
            '''

            img_ce = Color_Equalize(img)
            img_name = New_Image_File_Name(filename, '-ce')
            cv2.imwrite(str(col_equal_dir)+img_name, img_ce)


    print('done')