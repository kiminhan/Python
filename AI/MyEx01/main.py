import tkinter as tk
import tkinter.ttk as ttk

from OpencvFrame import OpencvFrame
from AniFrame import AniFrame
from RaspiFrame import RaspiFrame

def main():
    window = tk.Tk()
    window.title('Main Window')
    window.geometry('320x240+200+200')

    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill='both')

    tabs = ttk.Notebook(main_frame)
    tabs.pack(expand=True, fill='both')

    opencv_frame = OpencvFrame(tabs)
    tabs.add(opencv_frame, text='OpenCV')

    ani_frame = AniFrame(tabs)
    tabs.add(ani_frame, text='Animation')

    raspi_frame = RaspiFrame(tabs)
    tabs.add(raspi_frame, text='Raspberry Pi')

    main_frame.mainloop()


main()
