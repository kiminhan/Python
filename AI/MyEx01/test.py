import numpy as np
import cv2
import tkinter 
from PIL import Image
from PIL import ImageTk

# Load an color image
img = cv2.imread('airplane.jpg')

#Rearrang the color channel
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# A root window for displaying objects
root = tkinter.Tk()
root.title('Opencv Window')
root.geometry('320x240+300+300')

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(im)

# Put it in the display window
tkinter.Label(root, image=imgtk).pack() 

root.mainloop() # Start the GUI