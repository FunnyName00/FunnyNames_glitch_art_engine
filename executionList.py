from ImageModifier import *
from PIL import Image


class ActionList:
    def __init__(self, image: Image.Image):
        self.image = image
        self.pipeline = []

    def add(self, modifier_func, *args):
        self.pipeline.append((modifier_func, args))
    
    def execute(self):
        current_img = self.image
        
        for index, (func, args) in enumerate(self.pipeline):
            # print("Func : ", func," Args : ", *args)
            current_img = func(*args, current_img)
            
            #current_img.save(f"step_{index}.png")
        
        self.image = current_img
        self.image.save("final_result.png")
        


## Utilisation Example 

img = Image.open("Sil80.jpg")
processor = ActionList(img)

#processor.add(ImageModifier.binarize, 150)
processor.add(ImageModifier.noiseGenerator, 2)
processor.add(ImageModifier.chromaticAbberation, 100, 25, 0) 
processor.add(ImageModifier.exagerateColor, 150, 0, 2)
processor.add(ImageModifier.pixelSortBrightness, 100, 15)   
processor.add(ImageModifier.textAlongEdge, ["Hate", "Life", "Joy"], 100, 20) 
processor.add(ImageModifier.pixelSortBrightness, 200, 12)  
processor.add(ImageModifier.crossBrightness, 250, 1.3, 2) 

processor.execute()
