import os
import save_time
from tkinter import *

def about():
    os.startfile('about.py')
    
def login():
    with open("../Data/User.txt", "r") as user:
        data = user.readlines()
        user = str(data[0])
        password = int(data[1])
        if user == (u.get()+"\n") and password == int(p.get()) :
            os.startfile('home.py')
            st = save_time.Save_Time(user)
            st.ST()
            os._exit(1)
        else :
            Label(labelframe, fg = "red", text=" Error User and Password, try again. ").grid(row=0, column=3)
            Label(labelframe, fg = "red", text="نام کاربري يا پسورد يا وارد شده اشباه مي باشد").grid(row=1, column=3)
            
        
        
def sing_up():
    os.startfile('chang_pass.py')
   
user = Tk()

icon = PhotoImage(file='../Pictures/user.png')
user.tk.call('wm', 'iconphoto', user._w, icon)

screen_width = user.winfo_screenwidth()
screen_height = user.winfo_screenheight()

user.geometry("%sx%s+0+0"%(screen_width,screen_height))

# titel
user.title("ورود کاربر - نرم افزار کنترل گلخانه هوشمند - نسخه 1.0")

# menu bar
menubar = Menu(user)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="خروج", command=user.quit)
filemenu.add_separator()
menubar.add_cascade(label="فايل", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="راهنما نرم افزار", command="Help_p")
helpmenu.add_command(label="درباره ما", command=about)
helpmenu.add_separator()
menubar.add_cascade(label="راهنما", menu=helpmenu)
user.config(menu=menubar)

# lable from
labelframe = LabelFrame(user, text="اطلاعات کاربر")
labelframe.pack(fill="both", expand="yes")

# logo and text
logo = PhotoImage(file="../Pictures/pro_logo.ppm")
w1 = Label(labelframe, image=logo).grid(row=3, column=3)

#
Label(labelframe, text="User :").grid(row=0, column=0)
u = Entry(labelframe)
u.grid(row=0, column=1)

#
Label(labelframe, text="Password :").grid(row=1, column=0)
p = Entry(labelframe)
p.grid(row=1, column=1)

# buttons
Button(labelframe, text="ورود",width=15, command=login).grid(row=2, column=0)
Button(labelframe, text="تعويض پسورد",width=15, command=sing_up).grid(row=2, column=1)

mainloop()
