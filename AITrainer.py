import cv2
import numpy as np
import time
import PoseModule as pm
cap = cv2.VideoCapture("Pose/curls5.mp4")


detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    #img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("Pose/Test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)

    if len(lmList) != 0:
        # Right Arm
        detector.findAngle(img,12, 14,16)
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))
        #print(angle, per)

        #check for the dumbbell curls

        color = (255,0,255)
        if per == 100:
            color = (255, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
    # Draw Bar
        cv2.rectangle(img, (2250,200), (2300,650),color, 3)
        cv2.rectangle(img, (2250, int(bar)), (2250, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (2255, 170), cv2.FONT_HERSHEY_PLAIN, 3, color, 4)
    # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(count)}', (100, 620), cv2.FONT_HERSHEY_PLAIN, 7, (255,0,0), 5)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (100, 200), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)