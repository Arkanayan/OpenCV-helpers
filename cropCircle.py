import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
ap.add_argument('-dp', '--dp', required=False, help='This parameter is the inverse ratio of the accumulator resolution to the image resolution (see Yuen et al. for more details). Essentially, the larger the dp gets, the smaller the accumulator array gets')
ap.add_argument('-md', '--minDist', required=False, help='Minimum distance between the center (x, y) coordinates of detected circles')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
output = image.copy()

dp = args.get('dp', 1.2) or 1.2
minDist = args.get('minDist', 100) or 100

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, float(dp), float(minDist))

if circles is not None:

    circles = np.round(circles[0, :]).astype('int')

    for (i, (x, y, r)) in enumerate(circles):
        rect =  image[y - 5, x - 5]
        top_y, top_x = y - r - 10, x - r - 10
        bottom_y, bottom_x = y + r + 10, x + r + 10 
        rect = image[top_y:bottom_y, top_x:bottom_x]
        cv2.imwrite((args['image'].split('.'))[0] + 'circle_{}.png'.format(i), rect)