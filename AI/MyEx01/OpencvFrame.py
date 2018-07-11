import tkinter as tk

from Python.AI.MyEx01.opencv.CameraFrame import CameraFrame
from Python.AI.MyEx01.opencv.ImageFrame import ImageFrame
from Python.AI.MyEx01.opencv.VideoFrame import VideoFrame


class OpencvFrame(tk.Frame):

    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        image_button = tk.Button(self, text="Image")
        image_button.bind('<Button-1>', self.on_click)
        image_button.pack()

        video_button = tk.Button(self, text="Video")
        video_button.bind('<Button-1>', self.on_click)
        video_button.pack()

        camera_button = tk.Button(self, text="Camera")
        camera_button.bind('<Button-1>', self.on_click)
        camera_button.pack()

    def on_click(self, event):
        window = tk.Toplevel()
        window.title('Opencv Window')
        window.geometry('480x320+300+300')

        widget = event.widget
        widget_text = widget.cget('text')

        if widget_text == 'Image':
            frame = ImageFrame(window)
        elif widget_text == 'Video':
            frame = VideoFrame(window)
        elif widget_text == 'Camera':
            frame = CameraFrame(window)

        frame.pack(expand=True, fill='both')


    # def on_click_image(self):
    #     window = tk.Tk()
    #     window.title('Image Window')
    #     window.geometry('320x240+300+300')
    #     image_frame = ImageFrame(window)
    #     image_frame.pack(expand=True, fill='both')
    #     window.mainloop()
    #
    # def on_click_video(self):
    #     window = tk.Tk()
    #     window.title('Video Window')
    #     window.geometry('320x240+300+300')
    #     video_frame = VideoFrame(window)
    #     video_frame.pack(expand=True, fill='both')
    #     window.mainloop()
    #
    # def on_click_camera(self):
    #     window = tk.Tk()
    #     window.title('Camera Window')
    #     window.geometry('320x240+300+300')
    #     camera_frame = CameraFrame(window)
    #     camera_frame.pack(expand=True, fill='both')
    #     window.mainloop()


