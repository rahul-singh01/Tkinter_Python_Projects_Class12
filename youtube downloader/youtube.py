from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube  import *
from tkinter import messagebox
from PIL import Image , ImageTk

import requests ,time
import io

root = ''

root = Tk()

root.title("Download youtube videos")
root.geometry('600x600')
root.resizable(False,False)

Label(root, text = "Youtube video Downloader" , font = ('helvatica',15,'bold'),foreground ='white',background = 'red').place(x=50 , y =10)

def search():
    url = link.get()
    yt = YouTube(url)

    title = yt.title
    print(title)

    video_title.config(text = title)

    # video_image.config(image = yt.thumbnail_url)

    desc.delete('1.0' ,END)
    desc.insert(END , yt.description[:400])

    response = requests.get(yt.thumbnail_url) 
    img_byte = io.BytesIO(response.content)
    a = Image.open(img_byte)
    b = a.resize((200,200), Image.ANTIALIAS)
    b.save('temp.png')

    img = Image.open('temp.png')
    img = ImageTk.PhotoImage(img)

    video_image.config(image = img)
    


link = StringVar()
Label(root, text = 'Paste the url :' , font = ('helvatica',10,'bold')).place(x=10,y=80)
Entry(root, textvariable= link , width = 50).place(x= 120, y = 80)

# providing choices
radio = StringVar()
radio.set('Video')
video_radio = Radiobutton(root, text = "Video" , variable = radio ,value = 'Video' , font =('calibri',15)).place(x = 100, y = 110)
audio_radio = Radiobutton(root, text = "Audio" , variable = radio , value = 'Audio' ,font =('calibri',15)).place(x =200 , y = 110)
# creating option menu
choices = ['1080p','720p','480p','360p']
qua = StringVar()
qua.set('720p')

w = OptionMenu(root, qua , *choices)
w.place(x =300 , y = 110)

Button(root, text = "Search" ,command = search).place(x = 400 , y = 110)

# creating file location
folder = ""
def file_location():
    global folder
    folder = filedialog.askdirectory()

    if len(folder) != "":
        show.insert(tk.END , folder)
        show.config(state = DISABLED)
    
    else:
        messagebox.showwarning('Youtube downloader','Please select a location')

        
Button(root , text = "Choose location to save the file " ,font = ('helvatica',10),command = file_location).place(x =20 , y= 150)
show = Text(root , height = 1 ,width = 40)
show.place(x= 250 , y = 150)

# making image cache
frame1 = Frame(root, bd=2 , relief = RIDGE, bg= 'lightyellow' )
frame1.place(x=20 , y = 200, width = 540 , height = 250)

video_title = Label(frame1, text = 'Video Title Here' ,font = ('calibri',10), bg = 'lightblue' , anchor = 'w' )
video_title.place(x=5)
 
video_image  = Label(frame1 , bg = 'lightgrey', bd=2 , relief = RIDGE)
video_image.place(x=10 , y = 40 , height=200 , width = 200 ) 

video_desc = Label(frame1, text = 'Description' ,font = ('calibri',15), bg = 'orange' , anchor = 'w' )
video_desc.place(x= 300 , y = 20)
 
desc = Text(frame1, font = ('calibri',10), bg = 'lightyellow' )
desc.place(x= 230 , y = 60 ,height = 500 , width = 300 ) 

size = Label(root , text = "Total Size :  MB" ,font = ('helvatica',10) , bg = 'lightgrey')
size.place(x = 30 , y = 470)

downloading = Label(root , text = "Downloading : 0%" ,font = ('helvatica',10))
downloading.place(x = 30 , y = 510)



def dwn():
    url = link.get()
    yt = YouTube(url)
    print(qua.get())
    yt.streams.filter(adaptive = True).first().download()

download = Button(root , text = "  Download  " ,command = dwn ,font = ('helvatica',10) ,fg = 'white' , bg= 'blue')
download.place(x=350 , y = 470)

clear = Button(root , text = "  Clear  " ,font = ('helvatica',10) ,fg = 'white' , bg= 'blue')
clear.place(x=450 , y = 470)

#  progress bar

progess = ttk.Progressbar(root , orient = HORIZONTAL , length = 500 , mode = "determinate")
progess.place(x = 30 , y = 540)




root.mainloop()