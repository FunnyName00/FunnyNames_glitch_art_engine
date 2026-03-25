# FunnyName's Glitch Art Engine

A Python-based image manipulation software built using Pillow and Tkinter to create glitch art, pixel sorting, and various image effects.

## Features
### Feature	Description
Pixel Sorting : Sorts pixels in segments based on brightness thresholds.<br>
Chromatic Aberration : Simulates lens color fringing by shifting and sorting specific RGB channels.<br>
Edge-Detection Text : Procedurally places text along the high-contrast edges of an image.<br>
Binarization : High-speed black and white conversion based on custom thresholds<<br>
Cross-Brightness : Creates glowing cross artifacts on bright pixels.

## Installation

You need to have Python 3.8+ installed, then install the dependencies using :

```bash
pip install Pillow
pip install Tkinter
```

## Quick Start

The ActionList class allows you to queue multiple effects and execute them in sequence.
Python

# 1. Load your image
```
img = Image.open("input.png")
```
# 2. Initialize the processor
```
processor = ActionList(img)
```
# 3. Add your modifiers (Effect, *Args)
```
processor.add(ImageModifier.binarize, 128) 
processor.add(ImageModifier.pixelSortBrightness, 100, 30)
processor.add(ImageModifier.chromaticAbberation, 150, 10, 0)
```
# 4. Execute and save
```
processor.execute("final_result.png")
```
## Example

<img src="img/Sil80.jpg" alt="Original" width="45%"/> <img src="img/final_result.png" alt="Altered" width="45%"/>

## How It Works

The engine uses Pillow (PIL) to access the image pixels directly. <br> 
Many algorithms in this program utilize a "Threshold + Segment" logic

## Project Structure
```
.
├── main.py                 # Main program with GUI
├── scripts/
│   ├── ImageModifier.py    # Core static methods for image manipulation
│   └── executionList.py    # Pipeline management & sequential processing
└── img/                    # Source images and output directory
```
## Requirements

    Python 3.8+
    Tkinter
    Pillow (PIL)

## What's next ? 
  
  - Better gui to choose the modifiers 
  - MORE FUNCTIONNALITIESSSSS
  - MORE GLITCHEEEESSSSSSSS
  - M̶͔͔̯̆̉̐̑͐͆̌O̶̡͇̫̲͇̖̯͐͌͋͐̍͗͗͗̌R̴͍̀͌͂͂̋̍̅͗̄̕Ȩ̷̡̛̼̩̜̪͕͙͖͈̺̅͂̓́͛̊͊̑̄͋̚ͅͅ ̵̱͙̙̑͌̎̇͠Ģ̵̡͚͍̞͓̭̘͈̩̬̩̪̄ͅL̵̡̢̨̧̻̥̜͎͙͔̦̘̦̔̀̎̌͒͆́̈̈͠͝ͅḬ̷̙̱̮͙̦̜͕̇̍̑͂̀͊͆̅̐̈́̕T̶̙̟̘̟̝͈̖̭̪̺̻͓͈̟̤̆͆̾̈́̈́̇̿̈̂́̆̍͆͘͠Ĉ̸̨̧̲̭͚͎͍̺̘͓̣͓͓̰̾͐̌̌͑̍̓̍̌̿̌̈́ͅH̶̡̤͉̄̑̉̍͊̽̅̍̆͐Ẹ̵̖͔̣͒͗̊̇̓̌̅̀̅̌̌͗̑̾͝S̵̢̧̨̩͈̦̭̰͖͝
## License

Distributed under the MIT License. See LICENSE for more information.
