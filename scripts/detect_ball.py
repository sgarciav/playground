#!/usr/bin/env python3

import sys
import cv2
import argparse
import numpy as np

def main(args=None):
    parser = argparse.ArgumentParser(description = 'Main file to test the CSV class and argparser.')
    parser.add_argument('-f', '--filename',
                        type=str,
                        default=None,
                        help='Absolute or relative path to the input image.')

    args = parser.parse_args()

    # Read the image
    image = cv2.imread(args.filename, cv2.IMREAD_GRAYSCALE)
    og_image = cv2.imread(args.filename)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (11, 11), 0)

    # Apply Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=50)

    if circles is not None:
        # Convert the circles parameters to integers
        circles = np.round(circles[0, :]).astype("int")

        # Overlay the circle on the original image and output the center coordinates
        for (x, y, r) in circles:
            cv2.circle(og_image, (x, y), r, (0, 0, 255), 4)
            cv2.circle(og_image, (x, y), 1, (0, 0, 255), 4)  # Center of the circle
            print("Center coordinates ({}, {}) | radius: {}".format(x, y, r))

        # Display the image
        cv2.imshow("Detected ball", og_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("No circle detected in the image.")

if __name__ == '__main__':
    sys.exit(main())
