import tkinter as tk
import cv2

from PIL import Image
from PIL import ImageTk


class VideoFrame(tk.Frame):
    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        label = tk.Label(self)
        label.pack()

        vc = cv2.VideoCapture('opencv/solidWhiteRight.mp4')
        self.start_loop(label, vc)

    def start_loop(self, label, vc):
        _, image = vc.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.imshow(label, image)
        label.after(10, self.start_loop, label, vc)

    def imshow(self, label, image):
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        label.configure(image=image)
        label.image = image
