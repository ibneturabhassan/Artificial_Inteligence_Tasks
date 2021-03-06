# You should have the following at this point:
#
# 1.	Bounding box = (left, right, top, bottom)
# 2.	Centroid = (cx, cy)
#
# You now have to divide the image into four segments

from PIL import Image, ImageDraw
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
       color = img.getpixel((x,y))
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

d.rectangle(((right, top), (left, bottom)), outline="black")
d.line([(cx, top), (cx, bottom)], fill="black", width=1)
d.line([(left, cy), (right, cy)], fill="black", width=1)

img.show()