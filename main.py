from PIL import Image
import random


#path = input("Enter the path to the image :\n ")

img = Image.open("Sil80.jpg")

def pixelSortBrightness(brightness:int, pixels:int, img:Image, rgb:int):
    img = img.convert('RGB')
    if 0 <= rgb <= 2:
        x = 0

        while x < img.width:
            y = 0
            while y < img.height - pixels:
                pixel = img.getpixel((x, y))
                #print("(", x, ",",y,")",img.width, img.height, pixel)  

                if pixel[rgb] >= brightness:
                    list = []
                    for i in range(pixels):
                        list.append(img.getpixel((x, y+i)))

                    list.sort()
                    list.reverse()
                    for i in range(len(list)):
                        if y + i-1 < img.height:
                            img.putpixel( (x, y + i-1), list[i] )
                    y += pixels - 1
                else:
                    y += 1 
            x += 1

        return img


def binarize(img, threshold):
    output_image=img.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))< threshold:
                output_image.putpixel( (x,y), 0 )
            else:
                output_image.putpixel( (x,y), 255 )
    return output_image

def exagerateColor(img, threshold, rgb, factor):
    output_image=img.convert("RGB")
    for x in range(output_image.width):
            for y in range(output_image.height):
                pixel = output_image.getpixel((x,y))
                
                if pixel[rgb]< threshold:
                    li = list(pixel) 
                    li[rgb] //= factor
                    pixel = tuple(li)
                    output_image.putpixel( (x,y), pixel )
                if pixel[rgb]> threshold:
                    li = list(pixel) 
                    li[rgb] *= factor
                    pixel = tuple(li)
                    output_image.putpixel( (x,y), pixel)
    return output_image


def randomPixel(img, probability):
    output_image=img.convert("RGB")
    for x in range(output_image.width):
            for y in range(output_image.height):
                
                threshold = random.randint(0, 100)
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                if threshold >= probability:
                    output_image.putpixel( (x,y), (r,g,b))
    return output_image


#img = binarize(img, 100)

img = pixelSortBrightness(240, 200, img, 1)
img = randomPixel(img, 99)
img = exagerateColor(img, 50, 2, 100)
img = pixelSortBrightness(240, 200, img, 1)
img.save("result.jpg")




