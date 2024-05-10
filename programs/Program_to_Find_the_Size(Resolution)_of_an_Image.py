
from PIL import Image

filepath = sample2.png

img = Image.open (filepath)

width, height = img.size

print(“The dimensions of the image are:”, width, “x”, height)