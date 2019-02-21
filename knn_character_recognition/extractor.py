import cv2
import sys
import matplotlib.pyplot as plt
from train_and_test import main

def detect_text(filename):
    img  = cv2.imread(filename)
    img_final  = img
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)

    cv2.imshow('thresh_mask', mask)
    cv2.imshow('new_img', new_img)

    imgThresh = cv2.adaptiveThreshold(new_img, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            11,
            2)

    cv2.imshow('imgThresh', imgThresh)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    dilated = cv2.dilate(imgThresh, kernel)

    cv2.imshow('dilated', dilated)
    _, line_contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    line_arry = [[]]
    counter = 0
    for contour in line_contours:
        arr = []
        [x, y, w, h] = cv2.boundingRect(contour)
        
        if w < 35 and h < 35:
            continue

        cv2.rectangle(img, (x-10, y-10), (x+w+10, y+h+10), (255,0,255), 2)
        arr.append(x)
        arr.append(y)
        arr.append(w)
        arr.append(h)

        line_arry.append(arr)

    print(line_arry)

    for i in range(1, len(line_arry)):
        x = line_arry[i][0]
        y = line_arry[i][1]
        w = line_arry[i][2]
        h = line_arry[i][3]
        print(x, y, w, h)

        imgWordThresh = imgThresh[y:y+h, x:x+w]
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
        dilated = cv2.dilate(imgWordThresh, kernel)

        _, word_contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        word_arry = [[]]
        for wordContour in word_contours:
            arry = []
            [wx, wy, ww, wh] = cv2.boundingRect(wordContour)
            wx = x+wx
            wy = y+wy
            cv2.rectangle(img, (wx-5, wy-5), (wx+ww+5, wy+wh+5), (0,0,255), 1)
            word = img[wy:wy+wh, wx:wx+ww]
            string = main(word)
            print(string)

    cv2.imshow('lines', img)
    cv2.waitKey()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_text(str(sys.argv[1]))
