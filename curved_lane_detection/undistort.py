import numpy as np
import pandas as pd
import cv2
import os
import glob
import matplotlib.pyplot as plt
import pickle
import time

def undistort_img():

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # Prepare object points 0,0,0...8,5,0
    obj_pts = np.zeros((6*9,3), np.float32) 
    obj_pts[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    objpoints = []
    imgpoints = []
    cap = cv2.VideoCapture(0)

    captured = 0
    while captured < 50:
        ret, frame = cap.read()
        img = frame
        cv2.imwrite('input_images\photo'+str(captured)+'.jpg', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (9,6), None)

        if ret == True:
            print("\n Ret is true")
            objpoints.append(obj_pts)
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)
            imgpoints.append(corners)
       
            img2 = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
            captured+=1

        if ret == False:
            cv2.imshow('img', img)
        else:
            cv2.imshow('img', img2)
        cv2.waitKey(10)
        time.sleep(1)

    img_size = (img.shape[1], img.shape[0])
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)
    dst = cv2.undistort(img, mtx, dist, None, mtx)

    dist_pickle = {}
    dist_pickle['mtx'] = mtx
    dist_pickle['dist'] = dist
    pickle.dump(dist_pickle, open('camera_cal/cal_pickle.p', 'wb'))
    cap.release()
    cv2.destroyAllWindows()
    pass

def undistort(img, cal_dir='camera_cal/cal_pickle_2.p'):
    with open(cal_dir, mode='rb') as f:
        file = pickle.load(f)
    mtx = file['mtx']
    dist = file['dist']
    dst = cv2.undistort(img, mtx, dist, None, mtx)

    return dst

if __name__ == "__main__":
    undistort_img()
