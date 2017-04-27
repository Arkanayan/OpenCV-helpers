import numpy as np
import argparse
import cv2
from imutils import paths
import os

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


ap = argparse.ArgumentParser()
ap.add_argument('-imdir', '--images-dir', required=True, help='Path to the images directory')
ap.add_argument('-sigma', '--sigma', type=float, required=False, help='Kernal is calculated from sigma')
ap.add_argument('-o', '--output-dir', required=True, help='Name of the output images directory')
args = vars(ap.parse_args())

if args.get('images_dir', None) is None:
    print('Please specify the images directory')
    exit()

if not os.path.exists(args.get('output_dir')):
    print('Please specify the proper output images directory')
    exit()

imdir = args.get('images_dir')
sigma = args.get('threshold', None) or 3
output_dir = args.get('output_dir', None)

for imagePath in paths.list_images(imdir):

    image = cv2.imread(imagePath)
    blur = cv2.GaussianBlur(image ,(0,0), sigma)
    sharpened_image = cv2.addWeighted(image, 1.5, blur, -0.5, 0)

    image_path, image_name = os.path.split(imagePath)
    
    extension = os.path.splitext(imagePath)[1]
    output_image_name = '{}_sharp{}'.format(os.path.splitext(image_name)[0], extension)

    print('Writing sharpened image: {}'.format(output_image_name))
    cv2.imwrite(os.path.join(output_dir, output_image_name), sharpened_image)