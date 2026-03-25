from scripts.executionList import *
from scripts.ImageModifier import *
from PIL import Image

## Utilisation Example 

img = Image.open("img/Sil80.jpg")
processor = ActionList(img)

processor.add(ImageModifier.noiseGenerator, 2)
processor.add(ImageModifier.binarize, 150)
processor.add(ImageModifier.chromaticAbberation, 100, 25, 0) 
processor.add(ImageModifier.exagerateColor, 150, 0, 2)
processor.add(ImageModifier.pixelSortBrightness, 100, 15)   
processor.add(ImageModifier.textAlongEdge, ["Hate", "Life", "Joy"], 100, 20) 
processor.add(ImageModifier.pixelSortBrightness, 200, 12)  
processor.add(ImageModifier.crossBrightness, 250, 1.3, 2) 

# print(processor)
# print("--------")

# processor.swapPlace(0, 1)

# print(processor)
# print("--------")
# processor.delete(0)

# print(processor)

processor.execute("img/final_result.png")
