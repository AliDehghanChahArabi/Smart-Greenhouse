import os
import time
from tkinter import *

def about():
    os.startfile('about.py')
    
def chang():
    with open("../Data/User.txt", "r") as user:
        data = user.readlines()
        password = int(data[1])
        print (data)
        print(password)
        user.close()
        if password == int(p.get()) and int(p1.get()) == int(p2.get()) :
            with open("../Data/User.txt", "w") as user:
                user_name = "alidehghan"
                new_password = str(p1.get())
                data_new = """%s
%s"""%(user_name,new_password)
                user.write(data_new)
            Label(labelframe, fg = "blue", text=" *** OK *** ").grid(row=0, column=3)
            Label(labelframe, fg = "blue", text="پسورد با موفقيعت تعويض گرديد").grid(row=1, column=3)
            time.sleep (5)    
            os._exit(1)
        if int(p1.get()) != int(p2.get()) :
            Label(labelframe, fg = "red", text=" Error, try again. ").grid(row=0, column=3)
            Label(labelframe, fg = "red", text="پسورد جديد با تکرار آن يکسان نمي باشد").grid(row=1, column=3)
            
        if int(p1.get()) != int(p2.get()) and password != int(p.get()) :
            Label(labelframe, fg = "red", text=" Error, try again. ").grid(row=0, column=3)
            Label(labelframe, fg = "red", text="پسورد فعلي اشتباه، پسورد جديد و تکرار آن را اشتباه وارد کرديد").grid(row=1, column=3)
            
        if password != int(p.get()) :
            Label(labelframe, fg = "red", text=" Error Password, try again. ").grid(row=0, column=3)
            Label(labelframe, fg = "red", text="پسور فعلي را اشباه وارد کرده ايد.").grid(row=1, column=3)
            
             
    
chang_pass = Tk()

screen_width = chang_pass.winfo_screenwidth()
screen_height = chang_pass.winfo_screenheight()

chang_pass.geometry("%sx%s+0+0"%(int(screen_width/2),int(screen_height/2)))

# titel
chang_pass.title("تعويض پسورد - نرم افزار کنترل گلخانه هوشمند - نسخه 1.0")

# menu bar
menubar = Menu(chang_pass)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="خروج", command=chang_pass.quit)
filemenu.add_separator()
menubar.add_cascade(label="فايل", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="راهنما نرم افزار", command="Help_p")
helpmenu.add_command(label="درباره ما", command=about)
helpmenu.add_separator()
menubar.add_cascade(label="راهنما", menu=helpmenu)
chang_pass.config(menu=menubar)

# lable from
labelframe = LabelFrame(chang_pass, text="اطلاعات کاربر")
labelframe.pack(fill="both", expand="yes")


#
Label(labelframe, text="Password :").grid(row=0, column=0)
p = Entry(labelframe)
p.grid(row=0, column=1)

#
Label(labelframe, text="New Password :").grid(row=1, column=0)
p1 = Entry(labelframe)
p1.grid(row=1, column=1)

#
Label(labelframe, text="New Password :").grid(row=2, column=0)
p2 = Entry(labelframe)
p2.grid(row=2, column=1)

# buttons
Button(labelframe, text="تعويض پسورد",width=15, command=chang).grid(row=3, column=0)
Button(labelframe, text="خروج",width=15, command=chang_pass.destroy).grid(row=3, column=1)

mainloop()
