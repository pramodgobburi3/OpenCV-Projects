import cv2
from perspective_warp import pipeline, perspective_warp, inv_perspective_warp
from sliding_window import sliding_window, get_curve, draw_lanes
import numpy as np
import matplotlib.pyplot as plt

def vid_pipeline(img):
    global running_avg
    global index
    img_ = pipeline(img)
    img_ = perspective_warp(img_)
    out_img, curves, lanes, ploty = sliding_window(img_, draw_windows=False)
    curverad = get_curve(img, curves[0], curves[1])
    lane_curve = np.mean([curverad[0], curverad[1]])
    img = draw_lanes(img, curves[0], curves[1])

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontColor = (0, 0, 0)
    fontSize = 1
    cv2.putText(img, 'Lane Curvature: {:.0f} m'.format(lane_curve), (500, 620), font, fontSize, fontColor, 2)
    cv2.putText(img, 'Vehicle offset: {:.4f} m'.format(curverad[2]), (500, 670), font, fontSize, fontColor, 2)
    return img

if __name__ == "__main__":
    img = cv2.imread('test_imgs/test3.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret_img = vid_pipeline(img)
    plt.imshow(ret_img)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
