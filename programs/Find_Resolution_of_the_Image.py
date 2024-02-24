# solution 1 = Using Pillow module
import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/Hakki/OneDrive/Desktop/Girish.jpg")
width, height = img.size

print(width,"X",height)