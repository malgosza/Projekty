# import the necessary packages
import argparse

import args as args
import cv2

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="Path to the image to be thresholded")
# ap.add_argument("-t", "--threshold", type=int, default=128,
#                 help="Threshold value")
# args = vars(ap.parse_args())


# load the image and convert it to grayscale
image = cv2.imread("C:/Users/User/Downloads/Case-16-U-27-2.jpg")
# cv2.imshow('las',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('las',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# initialize the list of threshold methods

c=10

(T, thresh) = cv2.threshold(gray,c, 255, cv2.THRESH_BINARY)
cv2.imshow("THRESH_BINARY", thresh)


(T, thresh) = cv2.threshold(gray, c, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("THRESH_BINARY_INV", thresh)


(T, thresh) = cv2.threshold(gray, c, 255, cv2.THRESH_TRUNC)
cv2.imshow("THRESH_TRUNC", thresh)

(T, thresh) = cv2.threshold(gray, c, 255, cv2.THRESH_TOZERO)
cv2.imshow("THRESH_TOZERO", thresh)

(T, thresh) = cv2.threshold(gray, c, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("THRESH_TOZERO_INV", thresh)

cv2.waitKey(0)