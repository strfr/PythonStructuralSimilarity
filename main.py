# import the necessary packages
from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
cap = cv2.VideoCapture("birds.mp4")
frame = None
while True:
    if frame is None:
        ret, frame = cap.read()
    ret, frame2 = cap.read()
    # convert the images to grayscale
    grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    #                         cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    cv2.imshow("Diff", diff)
    frame=frame2
    cv2.waitKey(1)

