import tkinter as tk
import socket

from socket import socket


class RaspiFrame(tk.Frame):

    ip_entry = None
    port_entry = None
    message = None
    socket = None

    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):

        # Server Address
        net_frame = tk.LabelFrame(self, text='Server Address')
        net_frame.pack(fill='x')
        ip_label = tk.Label(net_frame, text='IP : ')
        ip_label.pack(side='left')
        self.ip_entry = tk.Entry(net_frame)
        self.ip_entry.pack(side='left', expand=True, fill='x')
        self.ip_entry.insert(tk.END, '127.0.0.1')
        port_label = tk.Label(net_frame, text='PORT : ')
        port_label.pack(side='left')
        self.port_entry = tk.Entry(net_frame, text='4000')
        self.port_entry.pack(side='left', expand=True, fill='x')
        self.port_entry.insert(tk.END, '4000')

        # LED
        led_frame = tk.LabelFrame(self, text='LED')
        led_frame.pack()
        led_on_button = tk.Button(led_frame, text='LED ON')
        led_on_button.pack(side='left')
        led_on_button.bind('<Button-1>', self.on_click)
        led_off_button = tk.Button(led_frame, text='LED OFF')
        led_off_button.pack(side='left')
        led_off_button.bind('<Button-1>', self.on_click)

        # Buzzer
        buzzer_frame = tk.LabelFrame(self, text='Buzzer')
        buzzer_frame.pack()
        buzzer_on_button = tk.Button(buzzer_frame, text='Buzzer ON')
        buzzer_on_button.pack(side='left')
        buzzer_on_button.bind('<Button-1>', self.on_click)
        buzzer_off_button = tk.Button(buzzer_frame, text='Buzzer OFF')
        buzzer_off_button.pack(side='left')
        buzzer_off_button.bind('<Button-1>', self.on_click)

        # Servo Motor
        servo_frame = tk.LabelFrame(self, text='Servo Motor')
        servo_frame.pack()
        servo_top_boutton = tk.Button(servo_frame, text='TOP')
        servo_top_boutton.pack(side='left')
        servo_top_boutton.bind('<Button-1>', self.on_click)
        servo_bottom_boutton = tk.Button(servo_frame, text='BOTTOM')
        servo_bottom_boutton.pack(side='left')
        servo_bottom_boutton.bind('<Button-1>', self.on_click)
        servo_left_boutton = tk.Button(servo_frame, text='LEFT')
        servo_left_boutton.pack(side='left')
        servo_left_boutton.bind('<Button-1>', self.on_click)
        servo_right_boutton = tk.Button(servo_frame, text='RIGHT')
        servo_right_boutton.pack(side='left')
        servo_right_boutton.bind('<Button-1>', self.on_click)

        self.message = tk.Message(self, text='No Message...', relief='solid', width='400')
        self.message.pack(expand=True, fill='both')

    def on_click(self, event):
        widget = event.widget
        widget_text = widget.cget('text')
        self.send_raspi(widget_text)

    def send_raspi(self, send_msg):
        ip = self.ip_entry.get()
        port = self.port_entry.get()

        with socket() as self.socket:
            self.socket.connect((ip, int(port)))
            self.socket.sendall(send_msg.encode())
            recv_msg = self.socket.recv(1024)
            self.message.configure(text='Recived Message : ' + recv_msg.decode())
            # print(f'>{resp.decode()}')
