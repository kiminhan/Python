import tkinter as tk

from PIL import Image
from PIL import ImageTk


class AniFrame(tk.Frame):

    minute = 0
    clock_label = None
    count_label = None
    start_button = None
    stop_button = None
    reset_button = None
    after_id = None

    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        self.minute = 0

        self.clock_label = tk.Label(self)
        self.clock_label.pack(expand=True, fill='both')

        self.count_label = tk.Label(self.clock_label, text='0')
        self.count_label.pack(expand=True)

        self.start_button = tk.Button(self.clock_label, text='start')
        self.start_button.pack(side='left')
        self.start_button.bind('<Button-1>', self.on_click)

        self.stop_button = tk.Button(self.clock_label, text='stop')
        self.stop_button.pack(side='left')
        self.stop_button.bind('<Button-1>', self.on_click)

        self.reset_button = tk.Button(self.clock_label, text='reset')
        self.reset_button.pack(side='left')
        self.reset_button.bind('<Button-1>', self.on_click)

        self.update_minute()

    def on_click(self, event):
        widget = event.widget
        widget_text = widget.cget('text')

        if widget_text == 'start':
            self.start_loop()
        elif widget_text == 'stop':
            self.stop_loop()
        elif widget_text == 'reset':
            self.reset_minute()

    def start_loop(self):
        self.minute = (self.minute + 1) % 60
        self.update_minute()
        self.after_id = self.after(200, self.start_loop)

    def stop_loop(self):
        self.after_cancel(self.after_id)
        self.after_id = None

    def reset_minute(self):
        self.minute = 0
        self.update()

    def update_minute(self):
        filename = "ani/frame_{:02d}_delay-0.1s.gif".format(self.minute)
        print('filename : ', filename)
        image = ImageTk.PhotoImage(Image.open(filename))
        self.clock_label.configure(image=image)
        self.clock_label.image = image

        self.count_label.configure(font=("Courier", 30))
        self.count_label.configure(bg='white')
        self.count_label.configure(text='{}'.format(self.minute))

        self.start_button.configure(text='start')
        self.stop_button.configure(text='stop')
        self.reset_button.configure(text='reset')

