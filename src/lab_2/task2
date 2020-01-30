# Task 2: Locating the centroid
# Centroid is the point where center of mass of the signature image is located. It can be computed using the algorithm given below.

from PIL import Image, ImageDraw
img = Image.open("image.jpg")
img = img.convert('1')
width, height = img.size
cx = 0
cy = 0
n = 0

for x in range(width):
    for y in range(height):
        if img.getpixel((x,y)) == 0:
            cx += x
            cy += y
            n += 1
cx = int(cx/n)
cy = int(cy/n)
print("cx: "+str(cx))
print("cy: "+str(cy))