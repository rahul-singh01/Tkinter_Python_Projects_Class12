import socket
from vidstream import *
from tkinter import *
import threading


ip = socket.gethostbyname(socket.gethostname())

server = StreamingServer(ip , 7777)
reciever = AudioReceiver(ip , 6666)

def listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciever.start_server)
    t1.start()
    t2.start()

def camera():
    cam = CameraClient(text_ip.get(1.0,'end-1c'),9999)
    t3 = threading.Thread(target=cam.start_stream)
    t3.start()

def screen():
    sc = ScreenShareClient(text_ip.get(1.0,'end-1c'),9999)
    t4 = threading.Thread(target=sc.start_stream)
    t4.start()

def audio():
    au = AudioSender(text_ip.get(1.0,'end-1c'),8888)
    t5 = threading.Thread(target=au.start_stream)
    t5.start()


root = Tk()
root.title("video client")
root.geometry('800x400')

label_ip = Label(root , text = 'target ip ')
label_ip.pack()

text_ip = Text(root , height = 1)
text_ip.pack()

btn_listen  = Button(root , text = 'Start Listening' , width = 50 , command = listening)
btn_listen.pack(anchor = CENTER , expand = True)

btn_camera  = Button(root , text = 'Start Camera' , width = 50 ,command = camera)
btn_camera.pack(anchor = CENTER , expand = True)

btn_screen  = Button(root , text = 'Start Screen' , width = 50 ,command = screen)
btn_screen.pack(anchor = CENTER , expand = True)

btn_audio  = Button(root , text = 'Start Audio' , width = 50 , command = audio)
btn_audio.pack(anchor = CENTER , expand = True)


root.mainloop()
