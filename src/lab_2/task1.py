from PIL import Image, ImageDraw
img = Image.open("image.jpg")
img = img.convert('1')
width, height = img.size
left = width
right = 0
top = height
bottom = 0

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

print("Top:"+str(top))
print("Bottom:"+str(bottom))
print("Left:"+str(left))
print("Right:"+str(right))
d = ImageDraw.Draw(img)
d.rectangle(((right, top), (left, bottom)), outline="black")
img.show()