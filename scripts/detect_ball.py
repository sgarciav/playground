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

    # # Apply Hough Circle Transform to detect circles
    # circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=50)

    # if circles is not None:
    #     # Convert the circles parameters to integers
    #     circles = np.round(circles[0, :]).astype("int")

    #     # Overlay the circle on the original image and output the center coordinates
    #     for (x, y, r) in circles:
    #         cv2.circle(og_image, (x, y), r, (0, 0, 255), 4)
    #         cv2.circle(og_image, (x, y), 1, (0, 0, 255), 4)  # Center of the circle
    #         print("Center coordinates ({}, {}) | radius: {}".format(x, y, r))

    #     # Display the image
    #     cv2.imshow("Detected ball", og_image)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # else:
    #     print("No circle detected in the image.")


    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 30, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize list to store circle centers
    circle_centers = []
    radii = []

    # Loop over the contours
    for contour in contours:
        # Approximate the contour to a closed polygon
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)

        # If the contour is approximately circular
        if len(approx) >= 6:
            # Find the minimum enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(contour)

            # Calculate area and aspect ratio of the enclosing circle
            circle_area = np.pi * (radius ** 2)
            aspect_ratio = cv2.contourArea(contour) / circle_area

            # # debug
            # print("{}: circle area {} | aspect ratio {}".format(radius, circle_area, aspect_ratio))

            # Filter based on area and aspect ratio
            if circle_area > 1000 and aspect_ratio > 0.0 and aspect_ratio <= 0.02:
                center = (int(x), int(y))
                radius = int(radius)

                # Draw the circle
                cv2.circle(og_image, center, radius, (0, 0, 255), 4)
                cv2.circle(og_image, center, 1, (0, 0, 255), 4)  # Center of the circle

                # Store the center coordinates
                circle_centers.append(center)
                radii.append(radius)

    # Display the image
    cv2.imshow("Detected circles (contour detection)", og_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Output the detected circle centers
    i = 0;
    for center in circle_centers:
        print("Center: {} | radius: {}".format(center, radii[i]))
        i = i + 1

if __name__ == '__main__':
    sys.exit(main())
