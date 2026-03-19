from PIL import Image



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


#img = binarize(img, 100)
img = pixelSortBrightness(100, 200, img, 0)

img.save("result.jpg")




