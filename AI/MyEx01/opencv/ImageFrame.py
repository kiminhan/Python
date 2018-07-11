import tkinter as tk
import cv2

from PIL import Image
from PIL import ImageTk


class ImageFrame(tk.Frame):
    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        label = tk.Label(self)
        label.pack()

        image = cv2.imread('opencv/airplane.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.imshow(label, image)

    def imshow(self, label, image):
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        label.configure(image=image)
        label.image = image
