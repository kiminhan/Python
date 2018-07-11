import tkinter as tk

class EtcFrame(tk.Frame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        button1 = tk.Button(self, text='button1') # command=self.on_click
        button1.bind('<Button-1>', self.on_click)
        button1.pack()

        button2 = tk.Button(self, text='button2')
        button2.bind('<Button-1>', self.on_click) # '<Button-1>'은 수정 no!
        button2.pack()

        label1 = tk.Label(self) # 생성할 때 text='label1' 가능하다. (1줄 감소)
        label1.configure(text='label1') # label이 label1로 대체 (set)
        label1.bind('<Button-1>', self.on_click)
        label1.pack()

    def on_click(self, event):
        widget = event.widget
        widget_text = widget.cget('text') # (cget = get)

        if widget_text == 'label1':
            label1 = widget
            label1.configure(text='label!!!')

        elif widget_text =='button1':
            window = tk.Toplevel()
            window.title('Sub Window')
            window.geometry('160x120+100+100')
            button = tk.Button(window, text='button')
            button.pack()
        elif widget_text =='button2':
            pass

        print('widget_text : ', widget_text)