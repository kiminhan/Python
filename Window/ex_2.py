from tkinter import *

def button1_callback():
    child =Tk()
    frame = Frame(child)
    frame.pack()

    label3 = Label(frame, text='label3', width=10, height=5)
    label3.pack()

def button2_callback():
    print('hi')

root = Tk()

frame = Frame(root)
frame.pack()

label1 = Label(frame, text='label1',width=10, height=5)
label1.pack()

label2 = Label(frame, text='label2')
label2.pack()

button = Button(frame,text='button', width=10, height=5, command=button1_callback)
button.pack()

frame2 = Frame(root)
frame2.pack()

button2 = Button(frame2, text='button2', command=button2_callback)
button2.pack()
# command 에서 함수호출시 () 를 쓰면(C언어 스타일) 원하는 동작을 하지않는다.

root.mainloop()