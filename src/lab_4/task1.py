from PIL import Image, ImageDraw
import glob
import os

def split(image, left, right, top, bottom, depth=0):
    cx, cy = findCentroid(image, left, right, top, bottom)
    if depth < 3:
        split(image, left, cx, top, cy, depth+1)
        split(image, cx, right, top, cy, depth+1)
        split(image, left, cx, cy, bottom, depth+1)
        split(image, cx, right, cy, bottom, depth+1)
    else:
        t = findTransitions(image, left, right, top, bottom)
        r = findRatio(left, right, top, bottom)

        centroid.write(str(cx) + " " + str(cy) )
        transitions.write(str(t))
        ratio.write(str(r))

def findCentroid(image, left, right, top, bottom):
    width = abs(left-right)
    height = abs(top-bottom)
    cx = 0
    cy = 0
    n = 0
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) == 0:
                cx += x
                cy += y
                n += 1
    if(n == 0):
        n = 1
    cx = int(cx / n)
    cy = int(cy / n)
    return cx, cy

def findTransitions(image, left, right, top, bottom):
    prev = image.getpixel((left, top))
    n = 0
    for p in range(left, right):
        for q in range(top, bottom):
            curr = image.getpixel((p, q))
            if ((curr == 255) and (prev == 0)):
                n += 1
            prev = curr
    return n

def findRatio(left, right, top, bottom):
    width = abs(left-right)
    height = abs(top-bottom)
    if(height != 0):
        return width/height
    else:
        return 0


for filename in glob.glob('C:\\Users\\Malik Hassan Raza\\PycharmProjects\\AI_Task\\src\\lab_4\\dataset\\*.png'): #assuming gif
    img = Image.open(filename)
    img = img.convert('1')
    width, height = img.size

    head_tail = os.path.split(filename)
    print()
    centroid = open("C:\\Users\\Malik Hassan Raza\\PycharmProjects\\AI_Task\\src\\lab_4\\\processed\\centroid\\"+head_tail[1].strip(".png")+".txt", "a")
    ratio = open("C:\\Users\\Malik Hassan Raza\\PycharmProjects\\AI_Task\\src\\lab_4\\\processed\\ratio\\" + head_tail[1].strip(".png") + ".txt", "a")
    transitions = open("C:\\Users\\Malik Hassan Raza\\PycharmProjects\\AI_Task\\src\\lab_4\\\processed\\transitions\\" + head_tail[1].strip(".png") + ".txt", "a")

    print(head_tail[1] + " STARTED")
    split(img, 0, width, 0, height)
    print(head_tail[1]+" ENDED")

