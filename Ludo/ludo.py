
from tkinter import *
from PIL import ImageTk , Image
import random, time
from tkinter import messagebox

dice = ''
root = ' '
player_list=[]
list_pick = 0
button_pos = 30
turn = 'red'
forward_list = []
make = ''

def start():
    global root

    root = Tk()
    root.geometry('1366x768')
    root.title('Ludo - Rahul Singh')


    image = Image.open('board.png')
    image = image.resize((800, 700), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)


    red_img = PhotoImage(file="red.png")
    blue_img = ImageTk.PhotoImage(file="violet.png")
    yellow_img = ImageTk.PhotoImage(file = "orange.jpg")
    green_img = ImageTk.PhotoImage(file = "green.jpg")
    white_img = ImageTk.PhotoImage(file = "white.png")
    Label(root, image = my_img).place(x=10, y=10)


    #placement of red buttons
    Button(root , image = red_img , width = 40 , height = 40).place(x = 615 , y=100)    
    Button(root , image = red_img , width = 40 , height = 40).place(x = 615 , y=190)
    Button(root , image = red_img , width = 40 , height = 40).place(x = 565 , y=140)
    Button(root , image = red_img , width = 40 , height = 40).place(x = 665 , y=140)

    #placement of blue buttons
    Button(root , image = blue_img , width = 40 , height = 40).place(x = 615 , y=490)
    Button(root , image = blue_img , width = 40 , height = 40).place(x = 615 , y=580)
    Button(root , image = blue_img , width = 40 , height = 40).place(x = 565 , y=540)
    Button(root , image = blue_img , width = 40 , height = 40).place(x = 665 , y=540)

    #placement of yellow button
    Button(root , image = yellow_img , width = 40 , height = 40).place(x = 165 , y=490)
    Button(root , image = yellow_img , width = 40 , height = 40).place(x = 165 , y=580)
    Button(root , image = yellow_img , width = 40 , height = 40).place(x = 215 , y=540)
    Button(root , image = yellow_img , width = 40 , height = 40).place(x = 110 , y=540)

    #placement of green button
    Button(root , image = green_img , width = 40 , height = 40).place(x = 165 , y=100)
    Button(root , image = green_img , width = 40 , height = 40).place(x = 165 , y=190)
    Button(root , image = green_img , width = 40 , height = 40).place(x = 215 , y=140)
    Button(root , image = green_img , width = 40 , height = 40).place(x = 110 , y=140)

    #placement of x plane buttons
    posx1 = Button(root , image = white_img , width = 40, height = 40)
    posx1.place(x = 38 , y = 295)
    posx2 = Button(root , image = white_img , width = 40, height = 40)
    posx2.place(x = 38 , y = 340)
    posx3 = Button(root , image = white_img,  width = 40, height = 40)
    posx3.place(x = 38 , y = 385)

    posx4 = Button(root , image = white_img , width = 40, height = 40) # green home
    posx4.place(x = 88 , y = 295)
    posx5 = Button(root , image = white_img , width = 40, height = 40)
    posx5.place(x = 88 , y = 340)
    posx6 = Button(root , image = white_img,  width = 40, height = 40)
    posx6.place(x = 88 , y = 385)

    posx7 = Button(root , image = white_img , width = 40, height = 40)
    posx7.place(x = 138 , y = 295)
    posx8 = Button(root , image = white_img , width = 40, height = 40)
    posx8.place(x = 138 , y = 340)
    posx9 = Button(root , image = white_img,  width = 40, height = 40)
    posx9.place(x = 138 , y = 385)

    posx10 = Button(root , image = white_img , width = 40, height = 40)
    posx10.place(x = 188 , y = 295)
    posx11 = Button(root , image = white_img , width = 40, height = 40)
    posx11.place(x = 188 , y = 340)
    posx12 = Button(root , image = white_img,  width = 40, height = 40)
    posx12.place(x = 188 , y = 385)

    posx13 = Button(root , image = white_img , width = 40, height = 40)
    posx13.place(x = 238 , y = 295)
    posx14 = Button(root , image = white_img , width = 40, height = 40)
    posx14.place(x = 238 , y = 340)
    posx15 = Button(root , image = white_img,  width = 40, height = 40)
    posx15.place(x = 238 , y = 385)

    posx16 = Button(root , image = white_img , width = 40, height = 40)
    posx16.place(x = 288 , y = 295)
    posx17 = Button(root , image = white_img , width = 40, height = 40)
    posx17.place(x = 288 , y = 340)
    posx18 = Button(root , image = white_img,  width = 40, height = 40)
    posx18.place(x = 288 , y = 385)

    posx19 = Button(root , image = white_img , width = 40, height = 40)
    posx19.place(x = 490 , y = 295)
    posx20 = Button(root , image = white_img , width = 40, height = 40)
    posx20.place(x = 490 , y = 340)
    posx21 = Button(root , image = white_img,  width = 40, height = 40)
    posx21.place(x = 490 , y = 385)

    posx22 = Button(root , image = white_img , width = 40, height = 40)
    posx22.place(x = 540 , y = 295)
    posx23 = Button(root , image = white_img , width = 40, height = 40)
    posx23.place(x = 540 , y = 340)
    posx24 = Button(root , image = white_img,  width = 40, height = 40)
    posx24.place(x = 540 , y = 385)

    posx25 = Button(root , image = white_img , width = 40, height = 40)
    posx25.place(x = 590 , y = 295)
    posx26 = Button(root , image = white_img , width = 40, height = 40)
    posx26.place(x = 590 , y = 340)
    posx27 = Button(root , image = white_img,  width = 40, height = 40)
    posx27.place(x = 590 , y = 385)

    posx28 = Button(root , image = white_img , width = 40, height = 40)
    posx28.place(x = 640 , y = 295)
    posx29 = Button(root , image = white_img , width = 40, height = 40)
    posx29.place(x = 640 , y = 340)
    posx30 = Button(root , image = white_img,  width = 40, height = 40)
    posx30.place(x = 640 , y = 385)

    posx31 = Button(root , image = white_img , width = 40, height = 40)
    posx31.place(x = 690 , y = 295)
    posx32 = Button(root , image = white_img , width = 40, height = 40)
    posx32.place(x = 690 , y = 340)
    posx33 = Button(root , image = white_img,  width = 40, height = 40) # blue home
    posx33.place(x = 690 , y = 385)

    posx34 = Button(root , image = white_img , width = 40, height = 40)
    posx34.place(x = 740 , y = 295)
    posx35 = Button(root , image = white_img , width = 40, height = 40)
    posx35.place(x = 740 , y = 340)
    posx36 = Button(root , image = white_img,  width = 40, height = 40)
    posx36.place(x = 740 , y = 385)

    # placement of y-axis
    posy1 = Button(root , image = white_img , width = 40, height = 40)
    posy1.place(x = 390 , y = 30)
    posy2 = Button(root , image = white_img , width = 40, height = 40)
    posy2.place(x = 340 , y = 30)
    posy3 = Button(root , image = white_img,  width = 40, height = 40)
    posy3.place(x = 440 , y = 30)

    posy4 = Button(root , image = white_img , width = 40, height = 40)
    posy4.place(x = 340 , y = 75)
    posy5 = Button(root , image = white_img , width = 40, height = 40)
    posy5.place(x = 390 , y = 75)
    posy6 = Button(root , image = white_img,  width = 40, height = 40) # red home
    posy6.place(x = 440 , y = 75)

    posy7 = Button(root , image = white_img , width = 40, height = 40)
    posy7.place(x = 340 , y = 125)
    posy8 = Button(root , image = white_img , width = 40, height = 40)
    posy8.place(x = 390 , y = 125)
    posy9 = Button(root , image = white_img,  width = 40, height = 40)
    posy9.place(x = 440 , y = 125)

    posy10 = Button(root , image = white_img , width = 40, height = 40)
    posy10.place(x = 340 , y = 165)
    posy11 = Button(root , image = white_img , width = 40, height = 40)
    posy11.place(x = 390 , y = 165)
    posy12 = Button(root , image = white_img,  width = 40, height = 40)
    posy12.place(x = 440 , y = 165)

    posy13 = Button(root , image = white_img , width = 40, height = 40)
    posy13.place(x = 340 , y = 210)
    posy14 = Button(root , image = white_img , width = 40, height = 40)
    posy14.place(x = 390 , y = 210)
    posy15 = Button(root , image = white_img,  width = 40, height = 40)
    posy15.place(x = 440 , y = 210)

    posy16 = Button(root , image = white_img , width = 40, height = 40)
    posy16.place(x = 340 , y = 255)
    posy17 = Button(root , image = white_img , width = 40, height = 40)
    posy17.place(x = 390 , y = 255)
    posy18 = Button(root , image = white_img,  width = 40, height = 40)
    posy18.place(x = 440 , y = 255)


    posy19 = Button(root , image = white_img , width = 40, height = 40)
    posy19.place(x = 340 , y = 430)
    posy20 = Button(root , image = white_img , width = 40, height = 40)
    posy20.place(x = 390 , y = 430)
    posy21 = Button(root , image = white_img,  width = 40, height = 40)
    posy21.place(x = 440 , y = 430)

    posy22 = Button(root , image = white_img , width = 40, height = 40)
    posy22.place(x = 340 , y = 475)
    posy23 = Button(root , image = white_img , width = 40, height = 40)
    posy23.place(x = 390 , y = 475)
    posy24 = Button(root , image = white_img,  width = 40, height = 40)
    posy24.place(x = 440 , y = 475)

    posy25 = Button(root , image = white_img , width = 40, height = 40)
    posy25.place(x = 340 , y = 520)
    posy26 = Button(root , image = white_img , width = 40, height = 40)
    posy26.place(x = 390 , y = 520)
    posy27 = Button(root , image = white_img,  width = 40, height = 40)
    posy27.place(x = 440 , y = 520)

    posy28 = Button(root , image = white_img , width = 40, height = 40)
    posy28.place(x = 340 , y = 565)
    posy29 = Button(root , image = white_img , width = 40, height = 40)
    posy29.place(x = 390 , y = 565)
    posy30 = Button(root , image = white_img,  width = 40, height = 40)
    posy30.place(x = 440 , y = 565)

    posy31 = Button(root , image = white_img , width = 40, height = 40) # yellow home
    posy31.place(x = 340 , y = 610)
    posy32 = Button(root , image = white_img , width = 40, height = 40)
    posy32.place(x = 390 , y = 610)
    posy33 = Button(root , image = white_img,  width = 40, height = 40)
    posy33.place(x = 440 , y = 610)

    posy34 = Button(root , image = white_img , width = 40, height = 40)
    posy34.place(x = 340 , y = 650)
    posy35 = Button(root , image = white_img , width = 40, height = 40)
    posy35.place(x = 390 , y = 650)
    posy36 = Button(root , image = white_img,  width = 40, height = 40)
    posy36.place(x = 440 , y = 650)

    def play():

        for i in range(0,len(player_list)):
            Label(root, text=f'{[player_list[i]]} your Turn').place(x=850 , y= 300)





    # user control setup
    
    def register():
        if  a != '':
            if len(player_list) != 4:

                global list_pick , button_pos

                player_list.append(str(a.get()))
                box = ['red','yellow','blue','green']
                
                pick = box[list_pick]
                
                Button(root , text = f'{player_list[list_pick]} Active' ,background = pick, foreground = 'black').place(x = 1200 , y = button_pos )
                print(player_list)

                list_pick = list_pick + 1
                button_pos = button_pos + 40

                print(list_pick)

                if len(player_list) == 2:
                    playing_condition = True
                    Button(root , text = '    Play    ' ,font=('calibri',25,'bold'),background = 'black' , foreground = 'green').place(x = 850 , y = 150)


            else:
                r.config(text = 'not available seat', state = 'disabled')
                print('enough player list for today')

        else:
            messagebox.showwarning('','Player cannot be empty!! ')


    a = StringVar()
    Label(root, text =' Enter the name of the player').place(x= 800 , y= 80)
    Entry(root , textvariable = a).place(x  = 800 , y = 100)
    r = Button(root , text = 'register',command = register )
    r.place( x = 920 , y = 100)


    def roll():
        global dice
        luck = random.randint(1,6)
        
        luck_display.config(text = f' The number comes is {luck}')

        if len(forward_list) < 1:
            forward_list.append(int(luck))
            print('before else',forward_list)

        else:
            forward_list.append(luck)
            x = sum(forward_list)
            forward_list.clear()
            forward_list.append(x)
            print('After else',forward_list)

        if turn == 'red':

            red_path = [posy6, posy9 , posy12, posy15, posy18, posx19, posx22, posx25 , posx28 , posx31 , posx34 , posx35 , posx36 , posx33 , posx30 , posx27 , posx24 , posx21 , posx18 ,  posx15 ,  posx12 , posx9 , posx6 , posx3  , posy21 , posy24 , posy27 , posy30  , posy33 , posy36]
            
            motion = red_path[forward_list[0]]
            motion.config(image = red_img)

    Button(root, text = 'Roll Dice' ,command = roll ,font = ('calibri',25,'bold')).place(x = 850 , y = 350 )   
        
    luck_display = Label(root, text = f' The number come is {dice}' , font = ('calibri',15,'bold'))
    luck_display.place(x = 950 , y = 350)    
        
    

    root.mainloop()

if __name__ == "__main__":
    start()


