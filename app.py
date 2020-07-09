# ALL CREDIT GOES TO THECOMEUPCODE: https://github.com/TheComeUpCode/WardrobeApp

import os
import random

import tkinter as tk
from PIL import Image, ImageTk

WINDOW_TITLE = "Clothes"
WINDOW_HEIGHT = 1200
WINDOW_WIDTH = 400
IMG_HEIGHT = 200
IMG_WIDTH = 200
BEIGE_COLOR_HEX = '#E3C396'
ALL_TOPS = [str("tops/") + file for file in os.listdir("tops/") if not file.startswith('.')]
ALL_BOTTOMS = [str("bottoms/") + file for file in os.listdir("bottoms/") if not file.startswith('.')]
ALL_SHOES = [str("shoes/") + file for file in os.listdir("shoes/") if not file.startswith('.')]


class WardrobeApp:
    def __init__(self, root):
        self.root = root

        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS
        self.shoe_images = ALL_SHOES

        self.top_image_path = self.top_images[0]
        self.bottom_image_path = self.bottom_images[0]
        self.shoe_image_path = self.shoe_images[0]

        self.tops_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.bottoms_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.shoes_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)

        self.top_image_label = self.create_photo(self.top_image_path, self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)

        self.bottom_image_label = self.create_photo(self.bottom_image_path, self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.TOP)

        self.shoe_image_label = self.create_photo(self.shoe_image_path, self.shoes_frame)
        self.shoe_image_label.pack(side=tk.TOP)

        self.create_background()

    def create_background(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.shoes_frame.pack(fill=tk.BOTH, expand=tk.YES)

        self.create_buttons()

    def create_buttons(self):

        top_prev_button = tk.Button(self.tops_frame, text="Prev", command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        create_outfit_button = tk.Button(self.tops_frame, text="Create Outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame, text="Next", command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text="Next", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

        shoe_prev_button = tk.Button(self.shoes_frame, text="Prev", command=self.get_prev_shoe)
        shoe_prev_button.pack(side=tk.LEFT)

        shoe_next_button = tk.Button(self.shoes_frame, text="Next", command=self.get_next_shoe)
        shoe_next_button.pack(side=tk.RIGHT)

    def create_photo(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def get_next_item(self, current_item, category, increment=True):
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0
        elif not increment and item_index == 0:
            next_index = final_index
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        if current_item in self.top_images:
            image_label = self.top_image_label
            self.top_image_path = next_image
        elif current_item in self.bottom_images:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image
        elif current_item in self.shoe_images:
            image_label = self.shoe_image_label
            self.shoe_image_path = next_image

        self.update_photo(next_image, image_label)

    def get_next_top(self):
        self.get_next_item(self.top_image_path, self.top_images, increment=True)

    def get_prev_top(self):
        self.get_next_item(self.top_image_path, self.top_images, increment=False)

    def get_next_bottom(self):
        self.get_next_item(self.bottom_image_path, self.bottom_images, increment=True)

    def get_prev_bottom(self):
        self.get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

    def get_next_shoe(self):
        self.get_next_item(self.shoe_image_path, self.shoe_images, increment=True)

    def get_prev_shoe(self):
        self.get_next_item(self.shoe_image_path, self.shoe_images, increment=False)

    def create_outfit(self):
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)
        new_shoe_index = random.randint(0, len(self.shoe_images) - 1)

        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)
        self.update_photo(self.shoe_images[new_shoe_index], self.shoe_image_label)


if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)

    root.mainloop()
