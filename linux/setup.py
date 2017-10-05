#!/usr/bin/python
import os
import time
import connector
from Tkinter import *

log = 1
time.sleep (2)
while log == 1:     
    def set_data():
        set_data = connector.Set_Data(a.get(),pwma.get(),ha.get(),ma.get(),
                             b.get(),pwmb.get(),hb.get(),mb.get(),
                             c.get(),pwmc.get(),hc.get(),mc.get(),
                             l.get(),pwml.get(),hl.get(),ml.get(),
                             0,normal.get(),0)
        set_data.set_data()
        print ("set data OK")
        os.system("action.py")
        master.destroy()       
        

    def web():
        web = connector.WEB()
        web.show_page()

    def printer():
        printer = connector.Print()
        printer.printer()

    load_data = connector.Load_Data()
    load_data = load_data.read_data()
    
    def magic(numList):
        s = map(str, numList)
        s = "".join(s)
        s = int(s)
        return s
    def magic1(numList):
        s = map(str, numList)
        s = "".join(s)
        s = float(s)
        return s    
    v = load_data['A']
    MA = magic(v)
    v = load_data['B']
    MB = magic(v)
    v = load_data['C']
    MC = magic(v)
    v = load_data['L']
    ML = magic(v)

    v = load_data['pA']
    PWMA = magic(v)
    v = load_data['pB']
    PWMB = magic(v)
    v = load_data['pC']
    PWMC = magic(v)
    v = load_data['pL']
    PWML = magic(v)

    v = load_data['hA']
    HA = magic(v)
    v = load_data['hB']
    HB = magic(v)
    v = load_data['hC']
    HC = magic(v)
    v = load_data['hL']
    HL = magic(v)

    v = load_data['mA']
    mA = magic(v)
    v = load_data['mB']
    mB = magic(v)
    v = load_data['mC']
    mC = magic(v)
    v = load_data['mL']
    mL = magic(v)

    v = load_data['in_s']
    IN = magic1(v)
    v = load_data['ex_s']
    EX = magic1(v)
    v = load_data['gas']
    GAS = magic(v)

    v = load_data['normal']
    NN = magic(v)

    print ("load OK")
    
    master = Tk()

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    master.geometry("%sx%s+0+0"%(screen_width,screen_height))

    master.title("Application GreenHouse v 1.1")

    smart = Frame(master).grid()
    sensor = Frame(master).grid()
    ref = Frame(master).grid()
    btn = Frame(master).grid()

#________________
    menubar = Menu(master)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label= "WEB", command=web)
    filemenu.add_command(label= "Print", command=printer)
    filemenu.add_separator()
    menubar.add_cascade(label= "File", menu=filemenu)    
    master.config(menu=menubar)

#________________
    Label(smart, text = " Fan A : ").grid(row=0, column=0)
    a = IntVar()
    a.set(MA)
    Radiobutton(smart, text = " ON ", variable = a, value = 1).grid(row=0, column=1)
    Radiobutton(smart, text = " OFF ", variable = a, value = 0).grid(row=0, column=2)

    Label(smart, text = " Hour ").grid(row=1, column=0)
    ha = Scale(smart, from_= 0, to = 12, length = 175, tickinterval = 1)
    ha.set(HA)
    ha.grid(row=2, column=0)

    Label(smart, text = " Minute ").grid(row=1, column=1)
    ma = Scale(smart, from_= 0, to = 60, length = 200, tickinterval = 1)
    ma.set(mA)
    ma.grid(row=2, column=1)

    Label(smart, text = " PWM ").grid(row=1, column=2)
    pwma = Scale(smart, from_= 0, to = 100, length = 250, tickinterval = 1)
    pwma.set(PWMA)
    pwma.grid(row=2, column=2)

#________________
    Label(smart, text = " Fan B : ").grid(row=0, column=3)
    b = IntVar()
    b.set(MB)
    Radiobutton(smart, text = " ON ", variable = b, value = 1).grid(row=0, column=4)
    Radiobutton(smart, text = " OFF ", variable = b, value = 0).grid(row=0, column=5)

    Label(smart, text = " Hour ").grid(row=1, column=3)
    hb = Scale(smart, from_= 0, to = 12, length = 175, tickinterval = 1)
    hb.set(HB)
    hb.grid(row=2, column=3)

    Label(smart, text = " Minute ").grid(row=1, column=4)
    mb = Scale(smart, from_= 0, to = 60, length = 200, tickinterval = 1)
    mb.set(mB)
    mb.grid(row=2, column=4)

    Label(smart, text = " PWM ").grid(row=1, column=5)
    pwmb = Scale(smart, from_= 0, to = 100, length = 250, tickinterval = 1)
    pwmb.set(PWMB)
    pwmb.grid(row=2, column=5)

#________________
    Label(smart, text = " Fan C : ").grid(row=0, column=6)
    c = IntVar()
    c.set(MC)
    Radiobutton(smart, text = " ON ", variable = c, value = 1).grid(row=0, column=7)
    Radiobutton(smart, text = " OFF ", variable = c, value = 0).grid(row=0, column=8)

    Label(smart, text = " Hour ").grid(row=1, column=6)
    hc = Scale(smart, from_= 0, to = 12, length = 175, tickinterval = 1)
    hc.set(HC)
    hc.grid(row=2, column=6)

    Label(smart, text = " Minute ").grid(row=1, column=7)
    mc = Scale(smart, from_= 0, to = 60, length = 200, tickinterval = 1)
    mc.set(mC)
    mc.grid(row=2, column=7)

    Label(smart, text = " PWM ").grid(row=1, column=8)
    pwmc = Scale(smart, from_= 0, to = 100, length = 250, tickinterval = 1)
    pwmc.set(PWMC)
    pwmc.grid(row=2, column=8)

#________________
    Label(smart, text = " Lamp : ").grid(row=0, column=9)
    l = IntVar()
    l.set(ML)
    Radiobutton(smart, text = " ON ",  variable = l, value = 1).grid(row=0, column=10)
    Radiobutton(smart, text = " OFF ",  variable = l, value = 0).grid(row=0, column=11)

    Label(smart, text = " Hour ").grid(row=1, column=9)
    hl = Scale(smart, from_= 0, to = 12, length = 175, tickinterval = 1)
    hl.set(HL)
    hl.grid(row=2, column=9)

    Label(smart, text = " Minute ").grid(row=1, column=10)
    ml = Scale(smart, from_= 0, to = 60, length = 200, tickinterval = 1)
    ml.set(mL)
    ml.grid(row=2, column=10)

    Label(smart, text = " PWM ").grid(row=1, column=11)
    pwml = Scale(smart, from_= 0, to = 100, length = 250, tickinterval = 1)
    pwml.set(PWML)
    pwml.grid(row=2, column=11)

#________
    if MA == 0:
        FA = 'OFF'
    if MA == 1:
        FA = 'ON'

    if MB == 0:
        FB = 'OFF'
    if MB == 1:
        FB = 'ON'

    if MC == 0:
        FC = 'OFF'
    if MC == 1:
        FC = 'ON'

    if ML == 0:
        FL = 'OFF'
    if ML == 1:
        FL = 'ON'

    Label(sensor, text = " Internal Sensor : ").grid(row=0, column=12)
    Label(sensor, text = " %s "%(IN)).grid(row=0, column=13)

    Label(sensor, text = " External Sensor : ").grid(row=1, column=12)
    Label(sensor, text = " %s "%(EX)).grid(row=1, column=13)

    Label(sensor, text = " Gas Sensor : ").grid(row=3, column=12)
    Label(sensor, text = " %s "%(GAS)).grid(row=3, column=13)

    Label(sensor, text = " Fan A : ").grid(row=4, column=12)
    Label(sensor, text = " %s "%(FA)).grid(row=4, column=13)

    Label(sensor, text = " Fan B : ").grid(row=5, column=12)
    Label(sensor, text = " %s "%(FB)).grid(row=5, column=13)

    Label(sensor, text = " Fan C : ").grid(row=6, column=12)
    Label(sensor, text = " %s "%(FC)).grid(row=6, column=13)

    Label(sensor, text = " Lamp : ").grid(row=7, column=12)
    Label(sensor, text = " %s "%(FL)).grid(row=7, column=13)

#_________
    Label(ref, text = " Normal Temp : ").grid(row=4, column=0)
    normal = Entry(ref, width = 4)
    normal.grid(row=4, column=1)

    Label(ref, text = " Normal Temp : %s "%(NN)).grid(row=5, column=0)


#_________
    Button(btn, text = "Set Data", command = set_data).grid(row=5, column=3)
    


    mainloop()
