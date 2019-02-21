# Get directory for all callibration images
images = glob.glob('camera_cal/*.jpg')
                                                                   
for indx, fname in enumerate(images):
    img = cv2.imread(fname)
    gray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)
                                                                   
    ret, corners = cv2.findChessboardCorners(gray, (9,6), None)
                                                                   
    if ret == True:
        objpoints.append(obj_pts)
        imgpoints.append(corners)
                                                                   
    #Test undistortion on img
    img_size = (img.shape[1], img.shape[0])
                                                                   
    # Calibrate camera
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, i
                                                                   
    dst = cv2.undistort(img, mtx, dist, None, mtx)
                                                                   
    #Save camera calibration for later use
    dist_pickle = {}
    dist_pickle['mtx'] = mtx
    dist_pickle['dist'] = dist
    pickle.dump(dist_pickle, open('camera_cal/cal_pickle.p', 'wb'))
