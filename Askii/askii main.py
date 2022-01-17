from PIL import Image, ImageOps  # Import python processing image library
import PIL.Image
from os import path


image_path = "C:\\Downloads"

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

user_input = input(
    "Enter the name of the image(make sure its in the same directory as this script): \n")

PIL.Image.open(user_input)

image = PIL.Image.open(user_input)

'''try:
        image = PIL.Image.open(path)
except:
        print(path, "unable to find image")'''

width, height = image.size
img = image.resize((width, height), Image. ANTIALIAS), image.save(
    'resized_image.png')
# resize image

'''width, height = image.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = image.resize((new_width, int(new_height)))'''


'''def resize_image(image, new_width=100):
    width, height = image.size
    width2 = width / 2
    ratio = height / width2 / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)'''


'''def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((new_width, new_height))'''

# convert to grayscale
greyscale_image = PIL.ImageOps.grayscale(image)

# convert from grayscale to ascii


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


# convert greyscale image to ascii characters
ascii_str = pixel_to_ascii(greyscale_image)


img_width = greyscale_image.width
ascii_str_len = len(ascii_str)
ascii_img = ("")


# Split the string based on width  of the image
'''for i in range(0, ascii_str_len, img_width):
    ascii_img += ascii_str[i:i+img_width] + "\n"'''


print(ascii_img)
