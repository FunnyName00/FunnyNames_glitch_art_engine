from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

class ImageModifier:

    @staticmethod 
    def pixelSortBrightness(brightness, pixels, img):
        img = img.convert('RGB')
        width, height = img.size
        img_data = img.load()
        for x in range(width):
            y = 0
            while y < height - pixels:
                pixel = img_data[x, y]
                pixel_brightness = sum(pixel) // 3
                if pixel_brightness >= brightness:
                    segment = []
                    for i in range(pixels):
                        segment.append(img.getpixel((x, y + i)))

                    segment.sort(key=lambda p: p, reverse=True)

                    for i in range(pixels):
                        img.putpixel((x, y + i), segment[i])
                    
                    y += pixels
                else:
                    y += 1 
        return img

    @staticmethod
    def chromaticAbberation(brightness, pixels, rgb_index, img):
        channels = list(img.convert('RGB').split())
        
        target_channel = channels[rgb_index]
        width, height = target_channel.size
        
        target_data = target_channel.load()

        for x in range(width):
            y = 0
            while y < height - pixels:
                val = target_data[x, y]

                if val >= brightness:
                    segment = []
                    for i in range(pixels):
                        segment.append(target_data[x, y + i])

                    segment.sort(reverse=True)

                    for i in range(pixels):
                        target_data[x, y + i] = segment[i]
                    
                    y += pixels
                else:
                    y += 1 

        channels[rgb_index] = target_channel
        img = Image.merge("RGB", channels)
        return img 
        

    @staticmethod
    def binarize(threshold, img):
        img = img.convert("L")
        img_data = img.load()
        for x in range(img.width):
            for y in range(img.height):
                if img_data[x,y] < threshold:
                    img.putpixel( (x,y), 0 )
                else:
                    img.putpixel( (x,y), 255 )
        return img

    @staticmethod
    def exagerateColor(threshold, rgb, factor, img):
        img=img.convert("RGB")
        img_data = img.load()
        for x in range(img.width):
                for y in range(img.height):
                    pixel = img_data[x, y]
                    
                    if pixel[rgb]< threshold:
                        li = list(pixel) 
                        li[rgb] //= factor
                        pixel = tuple(li)
                        img.putpixel( (x,y), pixel )
                    if pixel[rgb] > threshold:
                        li = list(pixel) 
                        li[rgb] *= factor
                        pixel = tuple(li)
                        img.putpixel( (x,y), pixel)
        return img

    @staticmethod
    def noiseGenerator(probability, img):
        img=img.convert("RGB")
        for x in range(img.width):
                for y in range(img.height):
                    
                    threshold = random.randint(0, 100)
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    if threshold <= probability:
                        img.putpixel( (x,y), (r,g,b))
        return img

    @staticmethod
    def edgeDetect(img):
        img = img.convert("L")
        img = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
                                                -1, -1, -1, -1), 1, 0))
        return img


    @staticmethod
    def textAlongEdge(words: list, threshold: int, spacing: int, img):
        edge = ImageModifier.edgeDetect(img)
        edge_data = edge.load()
        img_data = img.load()
        width, height = edge.size
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        except OSError:
            print("Font not found at that path. Try 'fc-list' in terminal to find your paths.")

        for x in range(0, width, spacing):
            for y in range(0, height, spacing):
                if edge_data[x, y] >= threshold:
                    word = random.choice(words)
                    #draw.text((x, y), word, font=font, fill=(img_data[x,y]))
                    draw.text((x, y), word, font=font, fill=((200,0,0)))
        
        return img
    
    @staticmethod
    def crossBrightness(threshold: int, saturation: float, size: int, img: Image):
        img = img.convert('RGB')
        read_img = img.copy()
        read_data = read_img.load()
        write_data = img.load()
        width, height = img.size

        for x in range(size, width - size):
            for y in range(size, height - size):
                r, g, b = read_data[x, y]
                
                if (r + g + b) // 3 >= threshold:
                    new_color = tuple(min(255, int(c * saturation)) for c in (r, g, b))
                    
                    write_data[x, y] = new_color
                    
                    for i in range(1, size + 1):
                        write_data[x + i, y] = new_color # Right
                        write_data[x - i, y] = new_color # Left
                        write_data[x, y + i] = new_color # Bottom
                        write_data[x, y - i] = new_color # Top

        return img





