# FunnyName's Glitch Art Engine

A Python-based image manipulation library built on Pillow for creating glitch art, pixel sorting, and procedural image effects.
## Features
### Feature	Description
Pixel Sorting	Sorts pixels in segments based on brightness thresholds.<br>
Chromatic Aberration	Simulates lens color fringing by shifting and sorting specific RGB channels.<br>
Edge-Detection Text	Procedurally places text along the high-contrast edges of an image.<br>
Binarization	High-speed black and white conversion based on custom thresholds<<br>
Cross-Brightness	Creates glowing "cross" artifacts on bright pixels.

## Installation

You need to have Python 3.8+ installed, then install the dependencies using :

```bash
pip install Pillow
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
processor.execute()
```
## Example

<img src="/Sil80.jpg" alt="Original" width="45%"/> <img src="/final_result.png" alt="Altered" width="45%"/>

## How It Works

The engine uses Pillow (PIL) to access the pixel buffer directly. Many algorithms in this library utilize a "Threshold + Segment" logic:

## Requirements

    Python 3.8+

    Pillow (PIL)

## What's next ? 
  
  - Add a main file
  - Make a user interface (I still gotta chose between CLI and graphic)
  - MORE FUNCTIONNALITIESSSSS
  - MORE GLITCHEEEESSSSSSSS
  - M̶͔͔̯̆̉̐̑͐͆̌O̶̡͇̫̲͇̖̯͐͌͋͐̍͗͗͗̌R̴͍̀͌͂͂̋̍̅͗̄̕Ȩ̷̡̛̼̩̜̪͕͙͖͈̺̅͂̓́͛̊͊̑̄͋̚ͅͅ ̵̱͙̙̑͌̎̇͠Ģ̵̡͚͍̞͓̭̘͈̩̬̩̪̄ͅL̵̡̢̨̧̻̥̜͎͙͔̦̘̦̔̀̎̌͒͆́̈̈͠͝ͅḬ̷̙̱̮͙̦̜͕̇̍̑͂̀͊͆̅̐̈́̕T̶̙̟̘̟̝͈̖̭̪̺̻͓͈̟̤̆͆̾̈́̈́̇̿̈̂́̆̍͆͘͠Ĉ̸̨̧̲̭͚͎͍̺̘͓̣͓͓̰̾͐̌̌͑̍̓̍̌̿̌̈́ͅH̶̡̤͉̄̑̉̍͊̽̅̍̆͐Ẹ̵̖͔̣͒͗̊̇̓̌̅̀̅̌̌͗̑̾͝S̵̢̧̨̩͈̦̭̰͖͝
## License

Distributed under the MIT License. See LICENSE for more information.
