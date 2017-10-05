import os
from Tkinter import *

def read_user():
    with open("../Data/User.txt", "r") as file:
        data_file = file.readlines()
        return data_file[0]
    
user_name = read_user()

def smart_control():
    os.startfile('smart_control.py')
    
def status():
    os.startfile('status.py')
    
def print_status():
    os.startfile('print_status.py')
    
def manul_control():
    os.startfile('manul_control.py')

def about():
    os.startfile('about.py')

def play_app():
    #os.startfile('about.py')
    print ("play")
    
def stop_app():
    #os.startfile('about.py')
    print("stop")

home = Tk()

#icon = PhotoImage(file='../Pictures/home.png')
#home.tk.call('wm', 'iconphoto', home._w, icon)

screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()

home.geometry("%sx%s+0+0"%(screen_width,screen_height))

# titel
home.title("نرم افزار کنترل گلخانه هوشمند - نسخه 1.0")

# menu bar
menubar = Menu(home)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="خروج", command=home.quit)
filemenu.add_separator()
menubar.add_cascade(label="فايل", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="راهنما نرم افزار", command="Help_p")
helpmenu.add_command(label="درباره ما", command=about)
helpmenu.add_separator()
menubar.add_cascade(label="راهنما", menu=helpmenu)
home.config(menu=menubar)

# lable from
labelframe = LabelFrame(home, text="تنظيمات")
labelframe.pack(fill="both", expand="yes")

labelframe1 = LabelFrame(home, text="", bg = "white")
labelframe1.pack(fill="both", expand="yes")

# logo and text
logo = PhotoImage(file="../Pictures/pro_logo.ppm")
w1 = Label(labelframe1, image=logo).pack(side="right", padx=10)

explanation = """
"""
w2 = Label(labelframe1, justify=LEFT, bg = "white",padx = 5, text=explanation).pack(side="left")

# buttons
sc = Button(labelframe, text="کنترل هوشمند", height=10, width=10, command=smart_control)
mc = Button(labelframe, text="کنترل دستي", height=10, width=10, command=manul_control)
s = Button(labelframe, text="وضعيت", height=10, width=10, command=status)
ps = Button(labelframe, text="پرينت وضعيت", height=10, width=10, command=print_status)

#photo1 = PhotoImage(file="../Pictures/stop.png")
#photo2 = PhotoImage(file="../Pictures/play.png")
#play = Button(labelframe, command=play_app, image=photo2)
#stop = Button(labelframe, command=stop_app, image=photo1)

# lable
Label(home, text="Application Status: Login System User %s"%(user_name), fg="black",font="Helvetica 10 bold").pack(side="left", anchor="w", expand="yes")

sc.pack(side="left", anchor="ne")
mc.pack(side="left", anchor="ne")
s.pack(side="left", anchor="ne")
ps.pack(side="left", anchor="ne")
#play.pack(side="left", anchor="ne")
#stop.pack(side="left", anchor="ne")

home.mainloop()
