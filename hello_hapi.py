#!/usr/bin/env python3
from mtcnn import MTCNN
import cv2


img = cv2.imread("datas/src/sample001.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detector = MTCNN()
faces = detector.detect_faces(rgb_img)

if(len(faces)):
    print("face found")
else:
    print("no face")

for face in faces:
    x, y, w, h = face['box']
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 8)

cv2.namedWindow("hapi", cv2.WINDOW_NORMAL)
cv2.imshow("hapi", img)
cv2.waitKey(0)
cv2.imwrite("datas/dst/sample001.jpeg", img)
