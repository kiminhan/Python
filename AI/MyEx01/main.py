import tkinter as tk
import tkinter.ttk as ttk

from Python.AI.MyEx01.AniFrame import AniFrame
from Python.AI.MyEx01.EtcFrame import EtcFrame  # 상속
from Python.AI.MyEx01.OpencvFrame import OpencvFrame
from Python.AI.MyEx01.RaspiFrame import RaspiFrame


def main():
    window = tk.Tk()
    window.title('Main Window') # 10~11라인, 빈 윈도우 화면 생성
    window.geometry('320x240+200+200')  # 크기

    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill='both', padx=5, pady=5) # padx, pady는 여백 크기

    tabs = ttk.Notebook(main_frame)
    tabs.pack(expand=True, fill='both')

    opencv_frame = OpencvFrame(tabs)
    tabs.add(opencv_frame, text='OpenCV')

    ani_frame = AniFrame(tabs)
    tabs.add(ani_frame, text='Animation')

    raspi_frame = RaspiFrame(tabs)
    tabs.add(raspi_frame, text='Raspberry Pi')

    etc_tab = EtcFrame(tabs)    # 탭 생성
    tabs.add(etc_tab, text = 'ETC') # 탭 추가 및 이름

    main_frame.mainloop()
    # window.mainloop() # 빈 윈도우 생성


main()
