# Usage
# python classify.py --model models/svm.cpickle --image images/cellphone.png

# Import the necessary packages
from __future__ import print_function
import joblib
from utils.hog import HOG
from utils import dataset
import imutils
import argparse
import mahotas
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
                help="Path to where the model will be stored")
ap.add_argument("-i", "--image", required=True, help="Path to the image file")
args = vars(ap.parse_args())

# Load the model
model = joblib.load(args["model"])

# Initialize the HOG descriptor
hog = HOG(orientations=18, pixelsPerCell=(10, 10),
          cellsPerBlock=(1, 1), transform=True, block_norm="L2-Hys")

# Load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image, find edges, and then find contours along the edged regions
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 150)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Sort the contours based on their x-axis position, ensuring that we read the
# numbers from left to right
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key=lambda x: x[1])

# Loop over the contours
for (c, _) in cnts:
    # Compute the bounding box for the rectangle
    (x, y, w, h) = cv2.boundingRect(c)

    # If the width is at least 7 pixels and the height is at least 20 pixels,
    # the contour is likely a digit
    if w >= 7 and h >= 20:
        # Crop the ROI and then threshold the grayscale ROI to reveal the digit
        roi = gray[y:y + h, x:x + w]
        thresh = roi.copy()
        T = mahotas.thresholding.otsu(roi)
        thresh[thresh > T] = 255
        thresh = cv2.bitwise_not(thresh)

        # Deskew the image center its extent
        thresh = dataset.deskew(thresh, 20)
        thresh = dataset.center_extent(thresh, (20, 20))

        # Show the thresholded image and the deskewed image
        cv2.imshow("thresh", thresh)

        # Describe the image and classify it
        hist = hog.describe(thresh)
        digit = model.predict([hist])[0]
        print("I think that number is: {}".format(digit))

        # Draw a rectangle around the digit, the show what the digit was classified as
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(image, str(digit), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

        # Show the image and wait for a keypress
        cv2.imshow("image", image)
        cv2.waitKey(0)
