# Task 4: Finding black to white transitions
# In this lab task, you have to find black to white transitions for each of the four segments/ blocks of the signature you made in Task3. That is, you have to calculate the number of white pixels in the neighborhood (use 8-connectivity) of each black pixel in the image.

from PIL import Image, ImageDraw


def b2wtrans(img, x1, y1, x2, y2):
    prev = img.getpixel((x1, y1))
    n = 0
    for p in range(x1, x2):
        for q in range(y1, y2):
            curr = img.getpixel((p, q))
            if ((curr == 255) and (prev == 0)):
                n += 1
            prev = curr
    return n


img = Image.open("image.jpg")
img = img.convert('1')
width, height = img.size
left = width
right = 0
top = height
bottom = 0

cx = 0
cy = 0
n = 0

for x in range(width):
    for y in range(height):
       color = img.getpixel((x, y))
       if color == 0:
           if x > right:
               right = x
           if x < left:
               left = x
           if y > bottom:
               bottom = y
           if y < top:
               top = y


for x in range(width):
    for y in range(height):
        if img.getpixel((x,y)) == 0:
            cx += x
            cy += y
            n += 1
cx = int(cx/n)
cy = int(cy/n)

print("Top:"+str(top))
print("Bottom:"+str(bottom))
print("Left:"+str(left))
print("Right:"+str(right))
print("cx: "+str(cx))
print("cy: "+str(cy))

d = ImageDraw.Draw(img)



d.rectangle(((left, top), (cx, cy)), outline="black")
d.rectangle(((cx, top), (right, cy)), outline="black")
d.rectangle(((left, cy), (cx, bottom)), outline="black")
d.rectangle(((cx, cy), (right, bottom)), outline="black")

TL = b2wtrans(img, left, top, cx, cy)
TR = b2wtrans(img, cx, top, right, cy)
BL = b2wtrans(img, cx, top, right, cy)
BR = b2wtrans(img, cx, top, right, cy)

print("TL: "+str(TL))
print("TR: "+str(TR))
print("BL: "+str(BL))
print("BR: "+str(BR))

img.show()