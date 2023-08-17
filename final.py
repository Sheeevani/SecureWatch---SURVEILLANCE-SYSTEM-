

import cv2
import time
from datetime import datetime
import argparse
import os
import winsound
import pygame



face_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\Downloads\\home\\haarcascade_frontalface_default.xml')  # properties of human face

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # color to grayscale
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
        for x, y, w, h in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)  # create a rectangle on detection
            exact_time = datetime.now().strftime('%Y-%b-%d-%H-%S-%f')  # date time
            cv2.imwrite("face_detected" + str(exact_time) + ".jpg", img)  # file name

        cv2.imshow("home_surveillance", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):  # window closed on pressing q
            ap = argparse.ArgumentParser()
            ap.add_argument("-ext", "--extension", required=False, default='jpg')
            ap.add_argument("-o", "--output", required=False, default='output.mp4')
            args = vars(ap.parse_args())

            dir_path = '.'  # path of our directory of our output
            ext = args['extension']
            output = args['output']

            images = []
            for f in os.listdir(dir_path):  # to find if there is a jpg file
                if f.endswith(ext):
                    images.append(f)

            image_path = os.path.join(dir_path, images[0])  # to find height and width
            frame = cv2.imread(image_path)
            height, width, channels = frame.shape

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # video encoding format
            out = cv2.VideoWriter(output, fourcc, 5.0, (width, height))

            for image in images:
                image_path = os.path.join(dir_path, image)
                frame = cv2.imread(image_path)
                out.write(frame)

            break


        if len(faces) >= 1:
            pygame.mixer.init()   # Initialize pygame
            pygame.mixer.music.load("C:\\Users\\HP\\Downloads\\home\\Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3") # Load music file
            pygame.mixer.music.set_volume(0.5)  # Setting the volume 
            pygame.mixer.music.play() # Play the music


video.release()
cv2.destroyAllWindows()
