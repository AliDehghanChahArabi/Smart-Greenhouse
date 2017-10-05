import connector
from tkinter import *

def manul_control():    
    def magic(numList):         # [1,2,3]
        s = map(str, numList)   # ['1','2','3']
        s = ''.join(s)          # '123'
        s = int(s)              # 123
        return s
    riceive_data = connector.Manual_Control()
    riceive_data = riceive_data.read_data()

    print(riceive_data)
    
    v = riceive_data['A']
    motorA = magic(v)
    v = riceive_data['pA']
    PwmA = magic(v)
    print (motorA, PwmA)

    v = riceive_data['B']
    motorB = magic(v)
    v = riceive_data['pB']
    PwmB = magic(v)
    print (motorB, PwmB)

    v = riceive_data['C']
    motorC = magic(v)
    v = riceive_data['pC']
    PwmC = magic(v)
    print (motorC, PwmC)

    v = riceive_data['L']
    motorL = magic(v)
    v = riceive_data['pL']
    PwmL = magic(v)
    print (motorL, PwmL)

    def set_data():
        print("Timer A = ",A.get())
        print("Timer B = ",B.get())
        print("Timer C = ",C.get())
        print("Timer Lamp = ",L.get())

        print("pwm. A = ",pwmA.get())
        print("pwm. B = ",pwmB.get())
        print("pwm. C = ",pwmC.get())
        print("pwm. Lamp = ",pwmL.get())

       

        data = connector.Manual_Control(
            A.get(),pwmA.get(),
            B.get(),pwmB.get(),
            C.get(),pwmC.get(),
            L.get(),pwmL.get())
        data.set_data()
            
                                       
        

        
    sc = Tk()

    icon = PhotoImage(file='../Pictures/smart.png')
    sc.tk.call('wm', 'iconphoto', sc._w, icon)

    screen_width = sc.winfo_screenwidth()
    screen_height = sc.winfo_screenheight()

    w = screen_width
    h = screen_height
    
    sc.geometry("%sx%s+0+0"%(int(w),int(h)))
    # titel
    sc.title("نرم افزار کنترل گلخانه هوشمند - کنترل دستي")

    #m1/#radio btn
    A = IntVar()
    A.set(motorA)
    #Label(sc, text="""Motor A """,).grid(row=0, column=0)
    
    Label(sc, text="PWM").grid(row=0, column=4)
    pwmA = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmA.set(PwmA)
    pwmA.grid(row=1, column=4)

    Label(sc, text="""Motor A """,).grid(row=2, column=0)
    Radiobutton(sc, text="ON", variable=A, value=1).grid(row=2, column=2)
    Radiobutton(sc, text="OFF", variable=A, value=0).grid(row=2, column=3)

     #m1/#radio btn
    B = IntVar()
    B.set(motorB)
    #Label(sc, text="""Motor B """,).grid(row=0, column=6)
    
    Label(sc, text="PWM").grid(row=0, column=9)
    pwmB = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmB.set(PwmB)
    pwmB.grid(row=1, column=9)

    Label(sc, text="""Motor B """,).grid(row=2, column=6)
    Radiobutton(sc, text="ON", variable=B, value=1).grid(row=2, column=7)
    Radiobutton(sc, text="OFF", variable=B, value=0).grid(row=2, column=8)

    
     #m1/#radio btn
    C = IntVar()
    C.set(motorC)
    #Label(sc, text="""Motor C """,).grid(row=0, column=11)
    
    Label(sc, text="PWM").grid(row=0, column=14)
    pwmC = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmC.set(PwmC)
    pwmC.grid(row=1, column=14)

    Label(sc, text="""Motor C """,).grid(row=2, column=11)
    Radiobutton(sc, text="ON", variable=C, value=1).grid(row=2, column=12)
    Radiobutton(sc, text="OFF", variable=C, value=0).grid(row=2, column=13)

       
     #m1/#radio btn
    L = IntVar()
    L.set(motorL)
    #Label(sc, text="""Lamp """,).grid(row=0, column=16)
    
    Label(sc, text="PWM").grid(row=0, column=19)
    pwmL = Scale(sc, from_=0, to=100, length=500, tickinterval=1)
    pwmL.set(PwmL)
    pwmL.grid(row=1, column=19)

    Label(sc, text="""Lamp """,).grid(row=2, column=16)
    Radiobutton(sc, text="ON", variable=L, value=1).grid(row=2, column=17)
    Radiobutton(sc, text="OFF", variable=L, value=0).grid(row=2, column=18)

    

    
    #btn
    Button(sc, text="Exit", width=10, fg="red", command=sc.destroy).grid(row=10, column=20)


    #btn
    Button(sc, text="Set", width=10, fg="green", command=set_data).grid(row=10, column=21)
    
    mainloop()


    


    

  

if __name__ == "__main__":
    manul_control()
