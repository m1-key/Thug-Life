# THUG LIFE

This project basically involves the use of OPEN CV.  
In this masking is done live , i.e you are infront of your webcam , at that time masking will be done.

---
## Process / Concept
First detect the face using haarcascade frontal face classifier and then resize the thug mask according the face size and then  
paste it over the face detected. Do the necessary conversions like converting array to image and vice versa as explained in the Thug Life.py file.  

---
### How to run this on your system ?
1. Download open cv by typing this ``` pip install opencv-python ``` in command prompt if you are using python ide.
2. If you are using Anaconda then install opencv by typing this ``` conda install -c conda-forge opencv ``` in Anaconda Prompt.
3. You also need to install pillow for placing mask over the image. You can download that by running ```pip install pillow``` command in command prompt.
4. After this download the mask image and haarcascade file from this repository .
5. Keep the code file , mask image and haarcascade file in the same folder and run the code .  

---
* An output image is there , basically output is not an image, I have just taken a frame from the output to show you what kind of result you will get.

### Important Links
1 - Opencv - ```https://github.com/opencv/opencv ```  
2 - Anaconda - ``` https://anaconda.org/ ```
