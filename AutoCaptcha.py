import cv2
from PIL import Image
import numpy as np
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class AutoCaptcha:
    def __init__(self, imagePath=""):
        try:
            # use the image object for your operations
            self.imageObject = Image.open(imagePath)
        except Exception as e:
            logging.exception("Exception Image constructor", exc_info=True)
            print(e)

    def ImageShow(self):
        try:
            self.imageObject.show()
        except Exception as e:
            logging.exception("Exception Image Show", exc_info=True)
            print(e)

    
    def GrayUpScale(self):
        try:
            pass
            #converting the image to gray scale
            GrayImage= self.imageObject.convert(mode='L')
            #up Scaling the image
            basewidth=256
            wpercent = (basewidth / float(GrayImage.size[0]))
            hsize = int((float(GrayImage.size[1]) * float(wpercent)))
            UpScale = GrayImage.resize((basewidth, hsize), Image.ANTIALIAS)

        except Exception as e:
            logging.exception("Exception GrayUpScale", exc_info=True)
            print(e)
            
            
    def Morphology(self):
        try:
            pass
        
            # load img data
            #img_data = cv2.imread("/Users/nitin/Desktop/download.png")
            
            #to convert PIL to cv2
            pil_img = self.imageObject
            numpy_image=np.array(pil_img)  
            img_data=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 


            
            #cv2.imshow('Original Imgage',img_data)
            #cv2.waitKey(0)

            #defining kernel
            kernel = np.ones((5,5), np.uint8) # datatype is unsigned Int, 5by5 pixel


            # erode operation
            erosion_op = cv2.erode(img_data,kernel,iterations = 1)
            #cv2.imshow('Erosion Operation',erosion_op)
            #cv2.waitKey(0)

            #dialtion Operation

            dilation_op = cv2.dilate(img_data,kernel, iterations=1)
            #cv2.imshow('Dilation Operation', dilation_op)
            #cv2.waitKey(0)

            # opening operation for noisy removal 
            opening_op = cv2.morphologyEx(img_data,cv2.MORPH_OPEN,kernel)
            #cv2.imshow('Opening Operation',opening_op)
            #cv2.waitKey(0)

            # closing operation for noisy removal
            closing_op = cv2.morphologyEx(img_data,cv2.MORPH_CLOSE,kernel)
            #cv2.imshow('Closing Operation',closing_op)
            #cv2.waitKey(0)
            
        except Exception as e:
            logging.exception("Exception Morphology", exc_info=True)
            print(e)
            

