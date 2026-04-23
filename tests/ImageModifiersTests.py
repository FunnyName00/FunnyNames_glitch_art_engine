import sys
import os

# Adds the parent directory (image_processing) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.executionList import *

img = Image.open("img/Sil80.jpg")
processor = ActionList(img)
processor.add(ImageModifier.binarize, 128)

processor.execute("tests/test_result.png")
