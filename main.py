# Hi Code Crafters This is Main file for our project where we are loading mask detector model and displaying the result
# Code Restricted To  Abhishek Gupta,Harsh Modi,Abhishek Sharma,Ishaan Dwivedi & Juet Evalution team till 20 th June 2020
# I have Done Commenting for temp purpose so that we can understand the code and algorithms

# This library is of CNN( convolutional neural network ) which can classify 1000s of Images and more than 50 layers of images
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# This Library Simply Comverts single Image files to a image array
from tensorflow.keras.preprocessing.image import img_to_array

# This is to load aur model which I have already trained i will explan it on phone call 
from tensorflow.keras.models import load_model

# This library contains various utility funtions of image / videos
from imutils.video import VideoStream

# This is to play a mp3 file 
from playsound import playsound

# Numpy -- Numerical Python  is for manipulating mathematic operations
import numpy as np

# used for parsing the arguments 
import argparse

#used for image utility functions
import imutils

#used for time functions
import time

#This is VERY IMP , Its Open Cv which has unlimited features to visualize an image (open source computer vison)
import cv2
import os
import datetime
#**************************************************************************************************************************************#
                                                       #ACTUAL CODE STARTS HERE ! 
#**************************************************************************************************************************************#

## First Of All we need model files (model is something that will tell us the result with mask or without mask ) so to import all these
## Files we have diclared variables to store paths 

# Path to Proto Text File
proto_txt_path = os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
    "deploy.prototxt.txt"])

#Path to caffe model file
model_path = os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
    "res10_300x300_ssd_iter_140000.caffemodel"])


#Path to MAIN MODEL FILE
model=os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
    "mask_detector.model"])


# This line stores the proto path and model path in  face_detector variable
face_detector = cv2.dnn.readNetFromCaffe(proto_txt_path, model_path)

# Now we are loading the model and storing it in mask_detector variable
mask_detector = load_model(model)

# cap is a variable which means capture , and to open camera we use Open Cv library cv2 to capture video from port 0 where 
# 0 is for webcam
cap = cv2.VideoCapture(0)

