import requests
import math
import cv2
import numpy as np
import time
import os

frameCount = 1
peakFPS = 0
minFPS = 10000
averageFPS =0
FPS = []
startTime = time.time()
video = cv2.VideoCapture("./road-traffic.mp4")

def getNextServer():
	#file = open("../NextServer.txt", "r")
	#return file.read()[:]
	#print(os.environ['server'])
	return os.environ['server']

uri_init = "http://" + getNextServer() + "/init"
uri = "http://" + getNextServer() + "/frameProcessing"
#force 640x480 webcam resolution
video.set(3,640)
video.set(4,480)
response = requests.post(uri_init, json = {})

for i in range(0,20):
    (grabbed, frame) = video.read()

while True:
	frameStartTime = time.time()
	frameCount+=1
	(grabbed, frame) = video.read()
	height = np.size(frame,0)
	width = np.size(frame,1)

    #if cannot grab a frame, this program ends here.
	if not grabbed:
		break
	#cv2.imwrite("Frame.jpg", frame)
	#print(frame.shape)
	data = {"Frame":frame.tolist()}
	r = requests.post(uri, json = data)
	currentFPS = 1.0/(time.time() - frameStartTime)
	FPS.append(currentFPS)
	print("response = {}, frame = {}, fps = {} ".format(r, frameCount, round(currentFPS, 3)))
        file2 = open("../output/client/result.txt", "a")
        file2.write("response = {}, frame = {}, fps = {} ".format(r, frameCount, round(currentFPS, 3)))
        file2.close
	if r == "<Response [500]>":
		break
print("Average FPS = {}".format(round(np.mean(FPS), 3)))
print("RunTimeInSeconds = {}".format(round(frameStartTime - startTime, 3)))