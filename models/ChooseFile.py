#!/usr/bin/python
import cv2
from PIL import Image


def choosefile():
    """Choose a file to convert"""
    # Define the path to the input image
    input_image_path = "../web_static/images/logo2.png"

    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Display basic properties of the image
    print("Image format:", image.format)
    print("Image mode:", image.mode)
    print("Image size:", image.size)


def display_image():
    """Display the image"""
    img = cv2.imread('../web_static/images/logo2.png')
    cv2.imshow('logo2', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


choosefile()
display_image()
