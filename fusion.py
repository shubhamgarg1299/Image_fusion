#IMAGE FUSION BY SHUBHAM GARG
import cv2

img_fn = ["img1.JPG",
          "img2.JPG",
          "img3.JPG",
          "img4.JPG"]
img_list = [cv2.imread(fn) for fn in img_fn]


mergeMertens = cv2.createMergeMertens()
resFusion = mergeMertens.process(img_list)


cv2.imwrite("fusion.jpg", resFusion*255)
