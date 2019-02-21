import cv2
import sys

def main():
    cap = cv2.VideoCapture('videos/'+ str(sys.argv[1]))

    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imwrite('test_imgs/img'+str(count)+'.jpg', frame)
        
        count += 1
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
