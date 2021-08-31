import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('Tracking')
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)

cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    frame = cv.imread('smarties2.jpg')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos('LS', 'Tracking')
    l_s = cv.getTrackbarPos('LV', 'Tracking')
    l_v = cv.getTrackbarPos('LH', 'Tracking')
    
    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')
    
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('result', res)
    
    key = cv.waitKey(1)
    if key == 27:
        break
    
cv.destroyAllWindows()