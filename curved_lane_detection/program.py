import sys
import cv2
from video_pipeline import vid_pipeline

def main():
    cap = cv2.VideoCapture('videos/' + str(sys.argv[1]))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        ret_frame = vid_pipeline(frame)
        ret_cv_frame = ret_frame[:,:,::-1]

        cv2.imshow('img',ret_frame)
        
    
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
