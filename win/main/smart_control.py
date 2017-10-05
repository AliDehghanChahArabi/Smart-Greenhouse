import os
import connector
from tkinter import *

def run_smart_control():
    def magic(numList):         # [1,2,3]
        s = map(str, numList)   # ['1','2','3']
        s = ''.join(s)          # '123'
        s = int(s)              # 123
        return s
    riceive_data = connector.Smart_Control()
    riceive_data = riceive_data.read_data()

    print(riceive_data)
    
    v = riceive_data['A']
    motorA = magic(v)
    v1 = riceive_data['hA']
    hA = magic(v1)
    v2 = riceive_data['mA']
    mA = magic(v2)
    v3 = riceive_data['pA']
    PwmA = magic(v3)
    print (motorA, hA, mA, PwmA)

    v = riceive_data['B']
    motorB = magic(v)
    v = riceive_data['hB']
    hB = magic(v)
    v = riceive_data['mB']
    mB = magic(v)
    v = riceive_data['mB']
    PwmB = magic(v)
    print (motorB, hB, mB, PwmB)

    v = riceive_data['C']
    motorC = magic(v)
    v = riceive_data['hC']
    hC = magic(v)
    v = riceive_data['mC']
    mC = magic(v)
    v = riceive_data['mC']
    PwmC = magic(v)
    print (motorC, hC, mC, PwmC)

    v = riceive_data['L']
    motorL = magic(v)
    v = riceive_data['hL']
    hL = magic(v)
    v = riceive_data['mL']
    mL = magic(v)
    v = riceive_data['mL']
    PwmL = magic(v)
    print (motorL, hL, mL, PwmL)

    v = riceive_data['i1']
    SA1 = magic(v)
    v = riceive_data['i2']
    SA2 = magic(v)
    v = riceive_data['i3']
    SA3 = magic(v) 
    print (SA1, SA2, SA3)

    v = riceive_data['e1']
    SB1 = magic(v)
    v = riceive_data['e2']
    SB2 = magic(v)
    v = riceive_data['e3']
    SB3 = magic(v)
    print (SB1, SB2, SB3)

    v = riceive_data['ex_s']
    ex_s = magic(v)
    v = riceive_data['in_s']
    in_s = magic(v)
    print (ex_s, in_s)

    
    
    def set_data():
        print("Timer A = ",A.get())
        print("Timer B = ",B.get())
        print("Timer C = ",C.get())
        print("Timer Lamp = ",L.get())

        print("H. A = ",HA.get())
        print("H. B = ",HB.get())
        print("H. C = ",HC.get())
        print("H. Lamp = ",HL.get())

        print("M. A = ",MA.get())
        print("M. B = ",MB.get())
        print("M. C = ",MC.get())
        print("M. Lamp = ",ML.get())

        print("pwm. A = ",pwmA.get())
        print("pwm. B = ",pwmB.get())
        print("pwm. C = ",pwmC.get())
        print("pwm. Lamp = ",pwmL.get())

        print("IA1 = ",IA1.get())
        print("IA2 = ",IA2.get())
        print("IA3 = ",IA3.get())
        
        print("E. T.1 = ",EA1.get())
        print("E. T.2 = ",EA2.get())
        print("E. T.3 = ",EA3.get())

        data = connector.Smart_Control(
            A.get(),pwmA.get(),HA.get(),MA.get(),
            B.get(),pwmB.get(),HB.get(),MB.get(),
            C.get(),pwmC.get(),HC.get(),MC.get(),
            L.get(),pwmL.get(),HL.get(),ML.get(),
            IA1.get(),IA2.get(),IA3.get(),
            EA1.get(),EA2.get(),EA3.get())
        data.set_data()

        os.startfile('web.py')
            
                                       
        

        
    sc = Tk()

    icon = PhotoImage(file='../Pictures/smart.png')
    sc.tk.call('wm', 'iconphoto', sc._w, icon)

    screen_width = sc.winfo_screenwidth()
    screen_height = sc.winfo_screenheight()

    w = screen_width
    h = screen_height
    
    sc.geometry("%sx%s+0+0"%(int(w),int(h)))

    # titel
    sc.title("نرم افزار کنترل گلخانه هوشمند - کنترل هوشمند")

    #m1/#radio btn
    A = IntVar()
    A.set(motorA)
    Label(sc, text="""Motor A """,).grid(row=0, column=0)
    
    Label(sc, text="Hour").grid(row=0, column=2)
    HA = Scale(sc, from_=0, to=12, length=500, tickinterval=1)
    HA.set(hA)
    HA.grid(row=1, column=2)
    
    Label(sc, text="Minute").grid(row=0, column=3)
    MA = Scale(sc, from_=0, to=59, length=500, tickinterval=1)
    MA.set(mA)
    MA.grid(row=1, column=3)
    
    Label(sc, text="PWM").grid(row=0, column=4)
    pwmA = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmA.set(PwmA)
    pwmA.grid(row=1, column=4)

    Label(sc, text="""Timer A """,).grid(row=2, column=0)
    Radiobutton(sc, text="ON", variable=A, value=1).grid(row=2, column=2)
    Radiobutton(sc, text="OFF", variable=A, value=0).grid(row=2, column=3)

    Label(sc, text="""Internal Temperature """,).grid(row=3, column=0)
    Label(sc, text="""%s if  < = """%(in_s)).grid(row=3, column=2)
    IA1 = Entry(sc, width = 3)
    IA1.grid(row=3, column=3)
    Label(sc, text="""Motor ON. """,).grid(row=3, column=4)
    Label(sc, text=""" %s """%(SA1)).grid(row=3, column=5)
    
    Label(sc, text="""Internal Temperature """,).grid(row=4, column=0)
    Label(sc, text="""%s if  > = """%(in_s)).grid(row=4, column=2)
    IA2 = Entry(sc, width = 3)
    IA2.grid(row=4, column=3)
    Label(sc, text="""Motor OFF. """,).grid(row=4, column=4)
    Label(sc, text=""" %s """%(SA2)).grid(row=4, column=5)

    Label(sc, text="""Internal Temperature """,).grid(row=5, column=0)
    Label(sc, text="""%s if  = = """%(in_s)).grid(row=5, column=2)
    IA3 = Entry(sc, width = 3)
    IA3.grid(row=5, column=3)
    Label(sc, text="""Normal. """,).grid(row=5, column=4)
    Label(sc, text=""" %s """%(SA3)).grid(row=5, column=5)
    
    Label(sc, text="""External Temperature """,).grid(row=6, column=0)
    Label(sc, text="""%s if  < = """%(ex_s)).grid(row=6, column=2)
    EA1 = Entry(sc, width = 3)
    EA1.grid(row=6, column=3)
    Label(sc, text="""Elemant ON. """,).grid(row=6, column=4)
    Label(sc, text=""" %s """%(SB1)).grid(row=6, column=5)
    
    Label(sc, text="""External Temperature """,).grid(row=7, column=0)
    Label(sc, text="""%s if  == """%(ex_s)).grid(row=7, column=2)
    EA2 = Entry(sc, width = 3)
    EA2.grid(row=7, column=3)
    Label(sc, text="""Elemant, Coler OFF. """,).grid(row=7, column=4)
    Label(sc, text=""" %s """%(SB2)).grid(row=7, column=5)

    Label(sc, text="""External Temperature """,).grid(row=8, column=0)
    Label(sc, text="""%s if  > = """%(ex_s)).grid(row=8, column=2)
    EA3 = Entry(sc, width = 3)
    EA3.grid(row=8, column=3)
    Label(sc, text="""Coler ON. """,).grid(row=8, column=4)
    Label(sc, text=""" %s """%(SB3)).grid(row=8, column=5)

     #m1/#radio btn
    B = IntVar()
    B.set(motorB)
    Label(sc, text="""Motor B """,).grid(row=0, column=6)
    
    Label(sc, text="Hour").grid(row=0, column=7)
    HB = Scale(sc, from_=0, to=12, length=500, tickinterval=1)
    HB.set(hB)
    HB.grid(row=1, column=7)
    
    Label(sc, text="Minute").grid(row=0, column=8)
    MB = Scale(sc, from_=0, to=59, length=500, tickinterval=1)
    MB.set(mB)
    MB.grid(row=1, column=8)
    
    Label(sc, text="PWM").grid(row=0, column=9)
    pwmB = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmB.set(PwmB)
    pwmB.grid(row=1, column=9)

    Label(sc, text="""Timer B """,).grid(row=2, column=6)
    Radiobutton(sc, text="ON", variable=B, value=1).grid(row=2, column=7)
    Radiobutton(sc, text="OFF", variable=B, value=0).grid(row=2, column=8)

    
     #m1/#radio btn
    C = IntVar()
    C.set(motorC)
    Label(sc, text="""Motor C """,).grid(row=0, column=11)
    
    Label(sc, text="Hour").grid(row=0, column=12)
    HC = Scale(sc, from_=0, to=12, length=500, tickinterval=1)
    HC.set(hC)
    HC.grid(row=1, column=12)
    
    Label(sc, text="Minute").grid(row=0, column=13)
    MC = Scale(sc, from_=0, to=59, length=500, tickinterval=1)
    MC.set(mC)
    MC.grid(row=1, column=13)
    
    Label(sc, text="PWM").grid(row=0, column=14)
    pwmC = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmC.set(PwmC)
    pwmC.grid(row=1, column=14)

    Label(sc, text="""Timer C """,).grid(row=2, column=11)
    Radiobutton(sc, text="ON", variable=C, value=1).grid(row=2, column=12)
    Radiobutton(sc, text="OFF", variable=C, value=0).grid(row=2, column=13)

       
     #m1/#radio btn
    L = IntVar()
    L.set(motorL)
    Label(sc, text="""Lamp """,).grid(row=0, column=16)
    
    Label(sc, text="Hour").grid(row=0, column=17)
    HL = Scale(sc, from_=0, to=12, length=500, tickinterval=1)
    HL.set(hL)
    HL.grid(row=1, column=17)
    
    Label(sc, text="Minute").grid(row=0, column=18)
    ML = Scale(sc, from_=0, to=59, length=500, tickinterval=1)
    ML.set(mL)
    ML.grid(row=1, column=18)
    
    Label(sc, text="PWM").grid(row=0, column=19)
    pwmL = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmL.set(PwmL)
    pwmL.grid(row=1, column=19)

    Label(sc, text="""Timer Lamp """,).grid(row=2, column=16)
    Radiobutton(sc, text="ON", variable=L, value=1).grid(row=2, column=17)
    Radiobutton(sc, text="OFF", variable=L, value=0).grid(row=2, column=18)

    

    
    #btn
    Button(sc, text="Exit", width=10, fg="red", command=sc.destroy).grid(row=10, column=20)


    #btn
    Button(sc, text="Set", width=10, fg="green", command=set_data).grid(row=10, column=21)
    
    mainloop()

if __name__=="__main__":
    run_smart_control()


   
  


    
