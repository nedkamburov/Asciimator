"Created by Keith Weaver at https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57"

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os
import argparse
import time

try:
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists('data'):
        index = time.time()
        os.rename("data", f'data_{index}')
        os.makedirs('data')
except OSError:
        print ('Error: Creating directory of data')


def convertMovieToImages(movieFile):
    # Playing video from file:
    cap = cv2.VideoCapture(f'{movieFile}')

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        if not ret:
            break

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()