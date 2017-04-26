import numpy as np
import argparse
import cv2
from imutils import paths
import csv
import os

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


ap = argparse.ArgumentParser()
ap.add_argument('-imdir', '--images-dir', required=True, help='Path to the images directory')
ap.add_argument('-sigma', '--sigma', type=float, required=True, help='Kernal is calculated from sigma')
ap.add_argument('-o', '--output-dir', required=True, help='Name of the output images directory')
args = vars(ap.parse_args())

if args.get('images_dir', None) is None:
    print('Please specify the images directory')
    exit()

imdir = args.get('images_dir')
threshold = args.get('threshold', None) or 100
output_csv = args.get('output_csv', None) or 'outputBlur.csv'

with open(output_csv, 'w', ) as csvfile:
    blurwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for imagePath in paths.list_images(imdir):

        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        fm = variance_of_laplacian(gray)
        image_path, image_name = os.path.split(imagePath)
        is_blurred = 'N'
        if fm < threshold:
            is_blurred = 'Y'
        else:
            is_blurred = 'N'
        blurwriter.writerow([str(image_name), is_blurred])
        print('{} -> {} -> {}'.format(str(image_name), str(fm), is_blurred))