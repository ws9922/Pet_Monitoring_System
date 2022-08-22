from read_content import read
from object_detect import object_detector
from send_email import send
import object_detect.utils as utils
import cv2
import sys
import time
import os
import requests
import datetime

model = "./object_detect/efficientdet_lite0.tflite"
options = object_detector.ObjectDetectorOptions(
  num_threads=4,
  score_threshold=0.3,
  max_results=3,
  enable_edgetpu=False)
detector = object_detector.ObjectDetector(model_path=model, options=options)

cap = cv2.VideoCapture(-1, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cat_img_id = 0
row_size = 20  # pixels
left_margin = 24  # pixels
text_color = (0, 0, 255)  # black
font_size = 1
font_thickness = 1

mode = ""
ISOTIMEFORMAT = "%H%M%S"
sendTime = 0
lastTime = None

while True:
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    if(theTime == "090000" or theTime == "210000"):
        send.SendEmail(True)
    success, image = cap.read()
    if (not success):
        continue
    image = cv2.flip(image, 1)
    # Run object detection estimation using the model.


    detections = detector.detect(image)
    image = utils.visualize(image, detections)

    text_location = (left_margin, row_size)
    cv2.putText(image, str(time.ctime(int(time.time()))), text_location, cv2.FONT_HERSHEY_PLAIN,
                font_size, text_color, font_thickness)
    
    cv2.imshow('object_detector', image)
    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
      break
    
    for i in detections:
        score = i.categories[0].score
        label = i.categories[0].label
        threshold = 0.5   
        if score > threshold and label == "cat":
            sendTime = int(datetime.datetime.now().strftime(ISOTIMEFORMAT))
            img_path = "/home/pi/final_project/cat_img/img_{}.jpg"
           
            
            cv2.imwrite(img_path.format(cat_img_id), image)
            send.SendEmail(False, img_path.format(cat_img_id))
            cat_img_id = (cat_img_id + 1) % 100
        
            
            read.talkContent("K Bao, Gay Yeah Par")
            break