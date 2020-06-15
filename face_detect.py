from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
# from imutils.video import VideoStream
from playsound import playsound
import numpy as np
import argparse
# import imutils
import time
import cv2
import os
import datetime


proto_txt_path = os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
 "deploy.prototxt.txt"])

welcome = os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
"welcome.mp3"])

        #'deploy.prototxt'
model_path = os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
"res10_300x300_ssd_iter_140000.caffemodel"])
model=os.path.sep.join([r"C:\Users\Ishaan\Desktop\Juet Hacks",
"mask_detector.model"])
        #'res10_300x300_ssd_iter_140000.caffemodel'
face_detector = cv2.dnn.readNetFromCaffe(proto_txt_path, model_path)
mask_detector = load_model(model)

class VideoCamera(object):
    def __init__(self):


        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        while True :
            ret, frame = self.cap.read()
            # frame = imutils.resize(frame, width=1080)
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177, 123))

            face_detector.setInput(blob)
            detections = face_detector.forward()

            faces = []
            bbox = []
            results = []

            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    face = frame[startY:endY, startX:endX]
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                    face = cv2.resize(face, (224, 224))
                    face = img_to_array(face)
                    face = preprocess_input(face)
                    face = np.expand_dims(face, axis=0)

                    faces.append(face)
                    bbox.append((startX, startY, endX, endY))

            if len(faces) > 0:
                results = mask_detector.predict(faces)

            for (face_box, result) in zip(bbox, results):
                (startX, startY, endX, endY) = face_box
                (mask, withoutMask) = result

                label = ""
                if mask > withoutMask:

                    label = "Mask"
                    color = (0, 255, 0)
                    #playsound(welcome)
                else:
                    label = "No Mask"
                    color = (0, 0, 255)
                    #playsound(welcome)

                cv2.putText(frame, label, (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

                # cv2.imshow("Frame", frame)
                # key = cv2.waitKey(1) & 0xFF

            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.

            return frame
