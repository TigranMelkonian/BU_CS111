#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from ps7image.hmcpng import *


def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels


def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green


def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100


def bw(pixels, threshold):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns
        a new 2-D list of pixels for an image that is a black-and-white version of the original image.
    """
    bw_image = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if brightness(pixels[r][c]) > threshold:
                bw_image[r][c] = [255, 255, 255]
            else:
                bw_image[r][c] = [0, 0, 0]
    return bw_image


def flip_vert(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns
        a new 2-D list of pixels for an image in which the original image is “flipped” vertically.
    """
    vert_flipped_pic = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            vert_flipped_pic[r][c] = pixels[len(pixels) - r - 1][c]
    return vert_flipped_pic


def reduce(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns
        a new 2-D list that represents an image that is half the size of the original image.
    """
    reduced_image = blank_image(len(pixels)//2, len(pixels[0])//2)
    for r in range(len(reduced_image)):
        for c in range(len(reduced_image[0])):
            reduced_image[r][c] = pixels[r * 2][c * 2]
    return reduced_image


def extract(pixels, rmin, rmax, cmin, cmax):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that
        represents the portion of the original image that is specified by the other four parameters.
    """
    cropped_image = blank_image(len(range(rmin, rmax)), len(range(cmin, cmax)))
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            cropped_image[r - rmin][c - cmin] = pixels[r][c]
    return cropped_image


