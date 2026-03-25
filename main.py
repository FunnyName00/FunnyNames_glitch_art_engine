import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from scripts.executionList import *
from scripts.ImageModifier import *
import threading

class GlitchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FunnyName's glitch art engine")
        
        self.original_img = None
        self.display_img = None

        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="gray")
        self.canvas.pack()

        self.btn_glitch = tk.Button(root, text="Apply Glitch", command=self.process_image)
        self.btn_glitch.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=600, mode='indeterminate')
        self.progress_bar.pack(pady=10)

    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.original_img = Image.open(path)
            self.update_canvas(self.original_img)

    def process_image(self):
        if self.original_img:
            self.progress_bar.start(10)
            thread = threading.Thread(target=self.run_glitch_task)
            thread.start()

    def run_glitch_task(self):
        
        img_to_process = self.original_img.copy()
        processor = ActionList(img_to_process)

        processor.add(ImageModifier.noiseGenerator, 2)
        processor.add(ImageModifier.binarize, 150)
        processor.add(ImageModifier.chromaticAbberation, 100, 25, 0) 
        processor.add(ImageModifier.exagerateColor, 150, 0, 2)
        processor.add(ImageModifier.pixelSortBrightness, 100, 15)   
        processor.add(ImageModifier.textAlongEdge, ["Hate", "Life", "Joy"], 100, 20) 
        processor.add(ImageModifier.pixelSortBrightness, 200, 12)  
        processor.add(ImageModifier.crossBrightness, 250, 1.3, 2)
        
        result = processor.execute("img/final_result.png")
        
        self.root.after(0, self.finalize_glitch, result)

    def finalize_glitch(self, result):

        self.update_canvas(result)
        self.progress_bar.stop()

    def update_canvas(self, pil_img):
        pil_img.thumbnail((600, 400))
        
        self.display_img = ImageTk.PhotoImage(pil_img)
        self.canvas.create_image(300, 200, image=self.display_img)

if __name__ == "__main__":
    root = tk.Tk()
    app = GlitchApp(root)
    root.mainloop()