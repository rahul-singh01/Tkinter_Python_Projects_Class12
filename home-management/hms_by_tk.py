from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk , Image
import matplotlib.pyplot as plt
import time, smtplib, random, os ,sys 
from fpdf import FPDF
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

localtime=time.asctime(time.localtime(time.time()))

root =  ''

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'
with open('passw.txt','r') as t:
    key = t.read()

def decode(code):
    final = ''
    key_index = 0
    alternate = 0


    for j, i in enumerate(code):

        if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
            key_index += 1
            continue

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue

        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==1):
            change = 'A'
        else:
            if alternate%2==1:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final

def encode(code):
    final = ''
    key_index = 0
    alternate = 0

    for j, i in enumerate(code): # j= indexing of a  i= value of a

        if j != 0 and j%int(key[0]) == 0:
            final += key[key_index%len(key)] # IMPORTANT ALGORITHEM...(it's like looping some range of integer.)
            key_index += 1

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue
        
        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==0):
            change = 'A'
        else:
            if alternate%2==0:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final

user =''

def add_member():
    global root
    root.destroy()
    root = Tk()
    def back():
        root.destroy()
        start()
    def member():
        global root
        root.destroy()
        root = Tk()

        style = Style()
        style.configure('TButton',font = ('calibri',10,'bold'), borderwidth = '2')
        style.map('TButton', foreground= [('active','!disabled','blue')] ,background=[('active','black')])

        def back1(): 
            add_member()
        
        member = str(mem.get())
        if member == '':
            Label(root,text="Username Cannot be Empty!!" ,background ='black',foreground ='red').pack()
        else:
        #checking members in txt file....
            make = True
            with open('members_list.txt', 'r') as t:
                members = t.read().split(',')

            for i in members:
                if member == i:
                    messagebox.showinfo('Display',"Username Already exists!! Try Another Username")
                    root.destroy()
                    start()
                    make = False

            if make:
                root.destroy()
                root = Tk()  
                canvas = Canvas(root, width = 1100, height = 400)  
                canvas.pack()  
                img = ImageTk.PhotoImage(Image.open("pic.jpg"))  
                canvas.create_image(0, 0, anchor=NW, image=img) 
                mail = StringVar()
                Label(root , text = 'Feel free to share your email with us because we keep your data encrypted', font = ('calibri',25,'bold'),justify = 'center', background = 'orange', foreground = 'black').place(x=5,y=20)     
                Label(root, text='Enter your Email to get your personal data',background ='yellow', foreground = 'black' ,font=('Calibri',20,'bold'), justify ='center').place( x=10, y = 100)
                Entry(root, textvariable = mail, width=50, font=('calibri',10,'bold')).place(x=500,y=110)

                def email_verify():
                    def back():
                        global root
                        root.destroy()  
                        member()
                    
                    try:
                        otp = random.randint(100000,999999)
                        server = smtplib.SMTP('smtp.proton.me', 587)
                        server.starttls()
                        server.login('homemanagement_Client@proton.me', "rdjloveshomemanagement")
                        server.sendmail('homemanagement_Client@proton.me', str(mail.get()) ,f' yourhomemanagement01 OTP Verification \n\n We are happy to see you make a best start with us \n hello {user} ! \n thanks for using \n\n\n Your Verification Code is :- { otp}')
                        messagebox.showinfo('MAIL BOT',f'Otp successfully sent to {str(mail.get())}')

                    except:
                        messagebox.showwarning('','Servers are not responding yet or local host web browser problem email cannot be sent to {str(mail.get())} \n  we are sorry for your inconvenince')
                        root.destroy()
                        start()

                    otp_hai = StringVar()
                    Label(root, text="Verify the Otp you have received ",background ='yellow', foreground = 'black' ,font=('Calibri',20,'bold'), justify ='center').place(x=20 , y=250)
                    Entry(root,textvariable= otp_hai ,font=('Calibri',10,'bold')).place(x=420,y=260)
                    def otp_verify():
                        re_otp = int(otp_hai.get())
                        if re_otp == otp:
                            messagebox.showinfo('OTP verification', "Verified SuccessFully")
                            encrypting = encode(str(mail.get()))

                            messagebox.showinfo('Home management','Member created and now ready for being a buyer')
                            with open('members_list.txt', 'a') as t:
                                t.write(f',{member}')
                            path = f'R://Home Management/{member} HM'
                            os.mkdir(path)
                            with open(f'{path}/{member}.txt', 'a') as t:
                                t.write(f'welcome to account directory of {member} created on {localtime} {encrypting}\n')
                                t.close()
                                global user 
                                user += member
                                root.destroy()
                                start()
                        else:
                            messagebox.showwarning('','OTP verification failure') 

                    Button(root, text = 'Verify Otp' , command=otp_verify).place(x=600,y=260) 
                Button(root, text='Submit' , command=email_verify).place(x=500, y= 150)

                Button(root,text="Back",command=back1).place(x=650 ,y=150)
                root.mainloop()
    
    root.geometry('350x200')
    root.resizable(False, False)
    bg1 = ImageTk.PhotoImage(file = 'image.png')

    Label(root, image = bg1).place(x= 0,y=0 ,relwidth =1, relheight =1)
    Label(root, text='Enter Name of the Member',background='#00FFFF' , foreground = 'black' , font=('Calibri',20,'bold'), justify ='center').place(x=10 , y= 20)

    mem = StringVar()
    
    memberentry = Entry(root, textvariable=mem , width = 40 ,font=('Calibri',10,'bold')).place(x = 10, y = 80)
   
    Button(root, text='submit', command=member).place(x=50, y=120)
    
    Button(root, text='back', command=back).place(x=150 , y=120)

    root.mainloop()  

list_product= []
list_price = []
graph_price =[]

def list_refresh():
    global list_price
    list_price = []

exit_cond = ' '

def buyer_account():

    global root
    root.destroy()
    root = Tk()

    def back():
        global root
        root.destroy()
        start()

    if user == '':
        messagebox.showinfo('home Management','Firstly logged in\n we are redirecting you to the login page')
        login()
        
    else:
        
        def back():
            global root
            root.destroy()
            start()

        def product_price():
            path = f'R:/Home Management/{user} HM'
            with open(f'{path}/{user}.txt','a') as t:
                t.write(f'Product = {str(product.get())} || Price = {int(price.get())} || date and time of buying = {localtime} \n')
                t.close()
            list_product.append(str(product.get()))
            list_price.append(int(price.get()))
            graph_price.append(int(price.get()))

            global exit_cond
            exit_cond += '1'

            msg = messagebox.askquestion('Adder','Add more items?')
            if msg == 'yes':
                buyer_account()
               
            else:
                
                path = f'R:/Home Management/{user} HM'
                add = sum(list_price)
                with open(f'{path}/{user}.txt','a') as t:
                    t.write(f'your total expenditure = INR {add} on {localtime} \n')
                    t.close()
                list_refresh()
                
                Label(root, text=f'You have spend {add} till now!!',font=('calibri',20,'bold'),foreground='green',background='black').place(x=10 ,y= 200)

                def expense():
                    a=0
                    path = f'R:/Home Management/{user} HM'
                    file = open(f'{path}/{user}.txt','r')
                    read = file.readlines()
                    for i in read:
                        if i.startswith("your total expenditure"):
                            total = i.split(' ')[5]
                            a += int(total)
                    for j in read:
                        if j.startswith("welcome to account directory"):
                            catch = j.split(' ')[-2]
                            year = str(catch)
                    Label(root, text=f'You have spend INR {a} from {year} ',font=('calibri',15,'bold'),foreground='white',background='black').place(x=30 ,y= 300)

                
                Label(root, text='know your all time Expenses?',font=('calibri',15,'bold'),foreground='yellow',background='black').place(x=10 ,y= 250)
                Button(root, text='View',command= expense).place(x=300,y=250)

                def show():
                    plt.bar(list_product,graph_price)
                    plt.ylabel('Price')
                    plt.xlabel('Products')
                    plt.title(f'{user} , your transactions on {localtime}')
                    plt.show()

                def save():
                    temp = ''
                    for i in localtime:
                        if i== ":" :
                            i = '-'
                        temp += i
                    plt.bar(list_product,graph_price)
                    plt.ylabel('Price')
                    plt.xlabel('Products')
                    plt.title(f'{user} , your transactions on {localtime}')
                    plt.savefig(f'{path}/{user} {temp}.png',dpi=300)
                    messagebox.showinfo('Home management','Saved Successfully')

                def back():
                    global root
                    root.destroy()
                    start()
                
                Label(root, text ='Show my graph of Expenses ',font=('calibri',15,'bold'),foreground='green',background='black').place(x=10 ,y= 350)
                Button(root, text ='View',command = show).place(x=300, y=350)
                Label(root, text = 'Save my graph of Expenses ',font=('calibri',15,'bold'),foreground='green',background='black').place(x=10,y= 400)
                Button(root, text ='Save',command = save).place(x=300, y=400)
                Button(root, text ='Back to main menu',command = back).place(x=200, y=450)

        root.resizable(False, False)       
        canvas = Canvas(root, width = 400, height = 500)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("pic.jpg"))  
        canvas.create_image(0, 0, anchor=NW, image=img)      

        product = StringVar()
        price = StringVar()
        with open('members_list.txt', 'r') as t:
            members = t.read().split(',')
        if user in members:
            Label(root, text=f'  Hello! {user}   ',font = ('calibri',10,'bold'), foreground='yellow',background='blue').place(x=40,y=10)      
                
        Label(root, text = "Product name" ,font = ('calibri',15,'bold'), foreground='yellow',background='black' ).place(x=20 ,y =30)
        Entry(root, textvariable = product).place(x=150,y=35)
        Label(root, text = "Product price",font = ('calibri',15 ,'bold'), foreground='yellow',background='black' ).place(x=20 ,y =70)         
        Entry(root, textvariable = price).place(x=150,y=75)

        Button(root, text="Submit", command = product_price).place(x=150, y=120) 
        Button(root, text="Back", command = back).place(x=50, y=120)
        
    root.mainloop()

amount = []
username = []
def compare_buyer():
    global root
    root.destroy()
    root = Tk()

    def back():
        global root
        root.destroy()
        start()
        

    def verify_user():
        condition = True
        make = False
        user1 = str(u.get()) 
        path = f'Home Management/{user1} HM'
        with open(f'members_list.txt','r') as f:
            v = f.read().split(',')
        for i in v:
            if user1 in i:
                condition = False
                make = True
                # username.append(user1.capitalize())
                a=0
                path = f'R:/Home Management/{user1} HM'
                file = open(f'{path}/{user1}.txt','r')
                read = file.readlines()
                for i in read:
                    if i.startswith("your total expenditure"):
                        total = i.split(' ')[5]
                        a += int(total)
        if make:
            amount.append(a)
            username.append(user1.capitalize())

        if condition:
            messagebox.showinfo('Home Management','Member not verified we are redirecting you to the startup menu')
            compare_buyer()

        if len(username)== 1:
            messagebox.showinfo('','Atleast two member should be added to compare!!')
            compare_buyer()
        else:
            que5 = messagebox.askquestion('','Add more members?')

            if que5 == 'yes':
                compare_buyer()
            else:
                def show_graph():
                    plt.bar(username, amount)
                    plt.xlabel('username')
                    plt.ylabel('Amount spend till now')
                    plt.title("who spends the most?")
                    plt.show()
                def save_graph():
                    plt.bar(username, amount)
                    plt.xlabel('username')
                    plt.ylabel('Amount spend till now')
                    plt.title("who spends the most?")
                    path1 = f'R:/Home Management/compared graphs'
                    plt.savefig(f'{path1}/{username}.png',dpi=300)
                    messagebox.showinfo('Home management','Saved Successfully')
                def back():
                    global root
                    root.destroy()
                    start()

                Label(root, text='\nView My Expenses Graph ').pack()

                Button(root, text ='Show',command= show_graph).pack()

                Label(root, text='\nSave My Expenses Graph ').pack()

                Button(root, text ='Save',command= save_graph).pack()
                Label(root, text ='\n')
                Button(root, text ='Back to Main menu',command=back ).pack()

                root.mainloop()

    canvas = Canvas(root, width = 800, height = 150)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("pic.jpg"))  
    canvas.create_image(0, 0, anchor=NW, image=img)      

   
    u = StringVar()
    Label(root, text='Name of Members', background='black',foreground='yellow', font=('calibri',20,'bold')).place(x=20 , y=40)
    Entry(root, textvariable=u ,font=('calibri',15,'bold')).place(x= 250 , y=40)
                    
    Button(root, text='Add',command = verify_user).place(x= 550 , y=45)
    Button(root, text='back',command = back).place(x= 650 , y=45)
    root.mainloop()

def email_state():
    list_mail = []
    list_str = ''
    global root
    root.destroy()
    root = Tk()

    def back():
        root.destroy()
        start()
    def email_display():
        global root
        root.destroy()
        root = Tk()
        def monthask():
            global root
            root.destroy()
            root = Tk()
            def back():
                root.destroy()
                start()
                
            def month():
                Label(root, text = 'Please wait Sending Email....').pack()
                file = open(f'{path}/{user}.txt','r')
                content = file.readlines()
                list_str = ''
                year_catch = str(y.get())
                month_catch = str(m.get().capitalize()[0:3])
                for i in content:
                    if i.startswith('your total expenditure'):
                        line = i               
                        if year_catch and month_catch in line:
                            list_mail.append(line)
                # print(list_mail)
                for i in list_mail:
                    list_str += i
                print(list_str)

                email_id = decode(catch)
                
                try:    
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login('yourhomemanagement01@gmail.com', decode('sZ2it`m)Xin.ndl_lhbmcbf"flcfmgu'))
                    server.sendmail('yourhomemanagement01@gmail.com ' , email_id ,f'Hi there {user} ! We are happy to see you\n  \n thanks for using your home management\n  \n {list_str}\n')
                    messagebox.showinfo('','Email Successfully Sent!!')
                except:
                    messagebox.showwarning('','Servers are not responding yet or local host web browser problem  \n  we are sorry for your inconvenince')
                    root.destroy()
                    start()

            y = StringVar()
            Label(root, text='Enter the year').pack()
            Entry(root, textvariable = y).pack()
            m = StringVar()
            Label(root, text='Enter the month').pack()
            Entry(root, textvariable = m).pack()         

            Button(root,text = 'Submit',command = month).pack() 
            Button(root,text = 'Back',command = back).pack() 
            root.mainloop()

        def yearask():
            global root
            root.destroy()
            root = Tk()

            def back():
                root.destroy()
                start()

            def  year():
                Label(root, text = 'Please wait Sending Email....').pack()
                file = open(f'{path}/{user}.txt','r')
                content = file.readlines()
                list_str = ''
                year_catch = str(y.get())
                for i in content:
                    if i.startswith('your total expenditure'):
                        line = i
                        if year_catch in line:
                            list_mail.append(line)
                
                email_id = decode(catch)
                for i in list_mail:
                    list_str += i
                
                try:
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login('yourhomemanagement01@gmail.com', decode('sZ2it`m)Xin.ndl_lhbmcbf"flcfmgu'))
                    server.sendmail('yourhomemanagement01@gmail.com ' , email_id ,f'Hi there {user} ! We are happy to see you\n  \n thanks for using your home management\n  \n {list_str}\n')
                    messagebox.showinfo('','Email Successfully Sent!!')
                except:
                    messagebox.showwarning('','Servers are not responding yet or local host web browser problem \n  we are sorry for your inconvenince')
                    root.destroy()
                    start()

            y = StringVar()
            Label(root, text='Enter the year').pack() 
            Entry(root, textvariable = y).pack()
            Button(root, text = 'Submit', command= year).pack()
            Button(root, text = 'Back', command=back ).pack()
            root.mainloop()
        
        def dateask():
            global root
            root.destroy()
            root = Tk()

            def back():
                root.destroy()
                start()

            def date():
                Label(root, text = 'Please wait Sending Email....').pack()
                file = open(f'{path}/{user}.txt','r')
                content = file.readlines()
                list_str = ''
                year_catch = str(y.get())
                month_catch = str(m.get().capitalize()[0:3])
                date_catch = str(d.get())
                for i in content:
                    if i.startswith('your total expenditure'):
                        line = i              
                        if year_catch and month_catch and date_catch in line:
                            list_mail.append(line)
                email_id = decode(catch)
                for i in list_mail:
                    list_str += i

                try:
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login('yourhomemanagement01@gmail.com', decode('sZ2it`m)Xin.ndl_lhbmcbf"flcfmgu'))
                    server.sendmail('yourhomemanagement01@gmail.com ' , email_id ,f'Hi there {user} ! We are happy to see you\n  \n thanks for using your home management\n  \n {list_str}\n')
                    messagebox.showinfo('','Email Successfully Sent!!')
                except:
                    messagebox.showwarning('','Servers are not responding yet or local host web browser problem \n  we are sorry for your inconvenince')
                    root.destroy()
                    start()

            y = StringVar()
            Label(root, text='Enter the year').pack()
            Entry(root, textvariable = y).pack()
            m = StringVar()
            Label(root, text='Enter the month').pack()
            Entry(root, textvariable = m).pack() 
            d = StringVar()
            Label(root, text = 'Enter the date').pack()
            Entry(root, textvariable = d).pack()        

            Button(root,text = 'Submit',command = date).pack() 
            Button(root,text = 'Back',command = back).pack() 
            root.mainloop()

        Label(root, text="Serach Your Expenses by deeply and get it on gmail id").pack()
        Button(root, text = 'Year Search', command = yearask).pack()

        Button(root, text = 'Month Search',command = monthask).pack()

        Button(root, text = 'Date Search',command = dateask).pack()

        Button(root, text = 'Back',command = back).pack()
        
    if user == '':
        messagebox.showinfo('home Management','Firstly logged in\n we are redirecting you to the login page')
        login()
        
    else:   
        make = True      
        path = f'R:/Home Management/{user} HM'
        file = open('members_list.txt','r')
        r = file.read().split(',')
        for i in r:
            if user in i:
                make  = False
                with open(f'{path}/{user}.txt','r') as f:
                    content = f.readlines()
                for j in content:
                    if j.startswith('welcome to account directory'):
                        catch = str(j.split(' ')[-1])
                        if '@gmail.com' in decode(catch):
                            m = True
        
        if m:                    
            msg = messagebox.askquestion('',f'{decode(catch)}\n\n Is that your email id?')
            if msg == 'yes':
                email_display()
            else:
                messagebox.showinfo('','Redirecting to main menu')
                root.destroy()
                start()
        if make:
            messagebox.showwarning('','Username not matched!!\n\n we are redirecting you to the add member feature')
            add_member()

    root.mainloop() 


otp1 = random.randint(1000,9999)

def delete():
    global root
    root.destroy()
    root = Tk()

    def back():
        root.destroy()
        start()

    if user =='':
        messagebox.showinfo('','you are not logged in\n We are redirecting you to the main menu')
        root.destroy()
        start()
    else:
        
        path = f'R:/Home Management/{user} HM'
        with open(f'{path}/{user}.txt','r') as f:
            content = f.readlines()
        for j in content:
            if j.startswith('welcome to account directory'):
                catch = str(j.split(' ')[-1])


        email_id = decode(catch)
        messagebox.showinfo('Home management','An Otp will Sent to Verify your gmail id we are doing this for our security purpose')
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('yourhomemanagement01@gmail.com ' ,decode('sZ2it`m)Xin.ndl_lhbmcbf"flcfmgu'))
            server.sendmail('yourhomemanagement01@gmail.com', email_id, f' yourhomemanagement01 OTP Verification \n\n We are happy to see you make a best start with us \n\n hello {user} ! \n\n  thanks for using \n\n\n Your Verification Code is :- { otp1}')
            messagebox.showinfo('MAIL BOT',f'Otp successfully Sent')
        except:
            messagebox.showwarning('','Servers are not responding yet or local host web browser problem \n  We are sorry for your inconvenince')
            root.destroy()
            start()

        def otp():
            global root
            root.destroy()
            root = Tk()
            re_otp = int(otp_hai.get())
            if re_otp == otp1:
                messagebox.showinfo('','Email Verified!! ')
    
                def data_remove():
                    location = f'R:/Home Management/{user} HM'
                    files = os.listdir(location) 
                    path = os.path.join(location)
                    for i in files:
                        os.remove(f'{location}/{i}')
                    os.rmdir(location)
                    messagebox.showinfo('','Account removed Successfully')

                def user_remove():
                    with open('members_list.txt', 'r') as t:
                        t = t.read().split(',')
                        for i in t:
                            if i == user:
                                t.remove(i)
                        final = ''
                        for i in t:
                            final += i
                            final += ' '.join(',')
                            
                    with open('members_list.txt', 'w') as t:
                        t.write(final[:-1])
                    messagebox.showinfo('Home Management','Username Removed Successfully')

                def back():
                    logout()
                        
                Label(root, text='\nRemove your username from database ').pack()  
                Button(root, text = 'Remove Username', command = user_remove ).pack()
                Label(root, text = '\nRemove your all account data forever').pack()
                Button(root, text='Account Data Remove',command = data_remove).pack()
                Label(root, text = '\n').pack()
                Button(root, text='Back',command=back).pack()
                
            else:
                messagebox.showinfo('','Email is wrong')    
                start()

        otp_hai = StringVar()
        Label(root, text="Verify the Otp you have received ").pack()
        Entry(root, textvariable= otp_hai).pack()
        Button(root, text = 'Verify', command = otp).pack()

        root.mainloop


def login():
    global root
    root.destroy()
    root = Tk()

    def back():
        global root
        root.destroy()
        start()

    def check_user(): 
        condition = True
        login = (str(l.get()))
        with open('members_list.txt','r') as f:
            t = f.read().split(',')
        for i in t:
            if i == login:
                global user
                messagebox.showinfo('','Login Successfully')
                user += i
                condition = False
                back()
        if condition:
            messagebox.showinfo('login','You are not a member of us \n firstly create a account')
            back()

    l = StringVar()
    Label(root, text = 'Enter your Username to login\n').pack()
    Entry(root, textvariable = l ).pack()
    Button(root, text= "Login" ,command= check_user).pack()
    Button(root, text = 'Back', command = back).pack()

def logout():
    global user
    if user == '':
        pass
    else:
        user = ''
        root.destroy()
        start()

    
def exit():
    if cond and exit_cond != ' ' :  #condition to be made after exiting the program: 
        arrange_expense()   
    else:
        pass
    sys.exit()

# def multiuser():
#     os.system('hms_by_tk.py')

pdf_file = ''

def myfile():

    if user == '':
        messagebox.showinfo('','you are not logged in!!')
        
    else:
        arrange_expense()
        path = f'R:/Home Management/{user} HM'
        with open(f'{path}/{user}.txt','r') as f:
            content = f.read().split('\n')

        root = Tk()

        root.geometry('1366x768')

        Label(root , text = f' Account detail of {user} ',font= ('helvetica',25,'bold') , background = 'grey' , foreground = 'white').pack()

        scroll_bar = Scrollbar(root,) 

        scroll_bar.pack(side = 'right' , fill = Y) 

        mylist = Listbox(root, font=('calibri',15,'bold')) 

        for i in content:
            mylist.insert(END, str(i))

        mylist.pack(padx=0,pady=0,fill=BOTH,expand=True) 

        scroll_bar.config( command = mylist.yview ) 

        def print_page():
            pdf = FPDF()    

            pdf.add_page() 

            pdf.set_font("Arial") 
            
            # open the text file in read mode 
            f = open(f'{path}/{user}.txt', "r") 

            pdf.cell(200, 10, txt = f'Account details of {user}', ln = 1, align = 'C')
            # insert the texts in pdf 

            for x in f: 
                pdf.cell(200, 10, txt = x, ln = 2, align = 'L') 
            
            # save the pdf with name .pdf 
            temp = ''
            for i in localtime:
                if i == ":" :
                    i = '-'
                temp += i
            
            save_name = f'{path}/{user}-Scanned-on-{temp}.pdf'

            pdf.output(save_name) 

            global pdf_file
            pdf_file += save_name  
            B2.config(text = 'Successfully print' , state = 'disabled')

        def send_pdf():
            try:

                # global root 
                # root = Tk()
                # root.geometry('100x100')

                # Label(root, text = 'Sending mail please wait... !!' , font = ('calibri',25,'bold'), background = 'black' , foreground = 'white').pack()

                fromaddr = 'yourhomemanagement01@gmail.com'

                with open(f'{path}/{user}.txt','r') as f: 
                    content = f.readline().split(' ')
                
                toaddr = decode(content[-1])
                
                # instance of MIMEMultipart 
                msg = MIMEMultipart() 
                
                # storing the senders email address   
                msg['From'] = fromaddr 
                
                # storing the receivers email address  
                msg['To'] = toaddr 
                
                # storing the subject  
                msg['Subject'] = "PDF file of your account is generated"
                
                # string to store the body of the mail 
                body = f" Thanks {user} ! \n\n for being our member \n\n Here is the pdf file you want"
                
                # attach the body with the msg instance 
                msg.attach(MIMEText(body, 'plain')) 
                
                # open the file to be sent
                
                if pdf_file == '':
                    print_page()
                else:
                    pass
                
                    
                filename = pdf_file
                attachment = open(filename, "rb") 
                
                # instance of MIMEBase and named as p 
                p = MIMEBase('application', 'octet-stream') 
                
                # To change the payload into encoded form 
                p.set_payload((attachment).read()) 
                
                # encode into base64 
                encoders.encode_base64(p) 
                
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
                
                # attach the instance 'p' to instance 'msg' 
                msg.attach(p) 
                
                # creates SMTP session 
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                
                # start TLS for security 
                s.starttls() 
                
                # Authentication 
                s.login(fromaddr, "rahul-home-management") 
                
                # Converts the Multipart msg into a string 
                text = msg.as_string() 
                
                # sending the mail 
                s.sendmail(fromaddr, toaddr, text) 
                
                # terminating the session 
                s.quit()

                # root.destroy()

                messagebox.showinfo('',f'Successfully sent mail to {toaddr}')
                B1.config(text='Already Sent !',state = 'disabled')

            except:
                messagebox.showinfo('',f'Failed to send mail to {toaddr} \n this is because of our server error or incorrect gate bypass')
            
        def back():
            global root
            root.destroy()
            start()

        B1 = Button(root, text = 'Send Me pdf' , command  = send_pdf)
        B1.place(x= 120 , y = 10)
        B2 = Button(root, text = 'Print page', command = print_page)
        B2.place(x = 20 , y = 10)

        Button(root, text = 'Back', command = back).place(x = 1150 , y = 10)

        root.mainloop()

def arrange_expense():
    local = localtime.split(' ')
    time = []
    expense_sort=[]
    remover = []
    path = f'R:/Home Management/{user} HM'
    with open(f'{path}/{user}.txt','r') as f:
        content = f.read().split('\n')
    for i in content:
        remover.append(i)
        if i.startswith('your total expenditure'):
            for j in local:
                time.append(j)
            time_catch = f'{time[0]} {time[1]} {time[2]}'
            if time_catch in i:
                expense_sort.append(i)
                remover.remove(i)

    same_day_expenses = []
    for i in expense_sort:
        j = i.split(' ')
        values = int(j[5])
        same_day_expenses.append(values)

    temp = ''
    for i in remover:
        temp += i
        temp += '\n'

    f = open(f'{path}/{user}.txt','w')
    f.write(temp)
    f.close()

    f = open(f'{path}/{user}.txt','a')
    f.write(f'your total expenditure = INR {sum(same_day_expenses)} on {localtime} \n')
    f.close()


def start():
    global root

    root = Tk()

    style = Style()

    root.geometry('1366x768')

    bg = ImageTk.PhotoImage(file = 'pic.jpg' , master = root)

    style.configure('TButton',font = ('calibri',20,'bold'), borderwidth = '4')
    style.map('TButton', foreground= [('active','!disabled','green')] ,background=[('active','black')])


    Label(root, image = bg).place(x= 0,y=0 ,relwidth =1, relheight =1)
    Label(root, text='Welcome to Home Management Program this will save your all expenses and keep record of it! \n lets start with us, hope u like it!!', font = ('calibri',25,'bold'),justify = 'center', background = 'black', foreground = 'white').place(x=15 ,y=20)

    Label(root, text = f'Hello! {user} ',background = 'yellow',foreground = 'black', font =('calibri',20,'bold'),justify = 'center').place(x = 650 , y = 130)

    Button(root, text='Sign Up', command=add_member).place(x=60 , y=200)

    Button(root, text = 'Login',command = login).place(x= 300 , y = 200)

    Button(root, text = 'Log Out',command = logout).place(x= 540, y = 200)

    # Button(root, text = 'Multi User' ,command = multiuser).place(x=1200, y=150)

    Button(root, text='Exit', command=exit ).place(x=780 , y=200)

    Button(root, text='ADD VALUE TO THE BUYER ACCOUNT', command=buyer_account).place(x=10 , y=300)


    Button(root, text='COMPARE YOUR EXPENSES WITH OTHER MEMBERS', command=compare_buyer).place(x=10 , y=370)


    Button(root, text='GET YOUR EXPENSES BY EMAIL STATEMENT', command=email_state).place(x=10 ,y=440) 

    Button(root, text='DELETE OR REMOVE', command=delete).place(x=10 , y=510)

    Button(root, text='VIEW MY ACCOUNT', command=myfile ).place(x=10 , y=580)

    root.mainloop()


if __name__ == '__main__':
    cond = True
    start()

if cond and exit_cond != ' ' :  #condition to be made after exiting the program:    
    arrange_expense()
else:
    pass