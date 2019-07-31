# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:26:10 2019

@author: Mithilesh
"""

""" 1 - This is bascially a simple code to detect face and then put the thug mask over it.
    2 - For face detection haarcascade classifier has been used here.
    3 - Pillow is used for pasting the mask over the detected face.
    4 - cv2 has been imported to read the image and to use the cascade.
    5 - numpy and Pillow's purpose is explained below.
"""

import cv2
import numpy as np
from PIL import Image

# using the webcam to read the image.
cap = cv2.VideoCapture(0)

# using Image function of Pillow to open the thug mask.
thug = Image.open("mask.png")

# using cv2 here to open the HaarCascade in order to detect the face.
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_alt.xml")

while True:
    boolean,img = cap.read()
    
    # it is good to convert the image into GrayScale image for detection of any portion in it.
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # here face will be detected and it will be 30% in the size of the original image.
    face=face_cascade.detectMultiScale(gray,1.3,5)
    
    """ Since cv2 read the image as a multidimensional array, so we need to convert this array into 
        an image in order to use the functions of Image function of Pillow. So here fromarray is used to
        convert that array into image format.
    """
    bkg = Image.fromarray(img)
    
    for (x,y,w,h) in face:
        #here we resize the thug mask according to the detected face.
        new_thug = thug.resize((w,h) , Image.ANTIALIAS)
        
        #now the thug mask is being pasted on the detected face .
        bkg.paste(new_thug , (x,y), mask = new_thug)
    
    """ now all the work is done here , so to view this image using cv2 , we again need to convert this
        this image into array so that cv2 can read this. Using numpy we can convert the image into array format.
    """
    cv2.imshow("Live",np.asarray(bkg))
    
    # press q to exit 
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
    
# releasing the frames here
cap.release()
cv2.destroyAllWindows()
        
