import os
import connector
from tkinter import *
from datetime import datetime

def run_status_print():
    def magic(numList):         # [1,2,3]
        s = map(str, numList)   # ['1','2','3']
        s = ''.join(s)          # '123'
        s = int(s)              # 123
        return s
    data = connector.Status()
    s_data = data.read_data()
    
    sensorA_data = magic(s_data['in'])
    sensorB_data = magic(s_data['ex'])

    motorA_data = magic(s_data['A'])
    motorB_data = magic(s_data['B'])
    motorC_data = magic(s_data['C'])
    motorL_data = magic(s_data['L'])

    pwmA = magic(s_data['pA'])
    pwmB = magic(s_data['pB'])
    pwmC = magic(s_data['pC'])
    pwmL = magic(s_data['pL'])

    motorA_data_out = ""
    motorB_data_out = ""
    motorC_data_out = ""
    motorL_data_out = ""
    motorL_pwm_data_out = ""
    
   
    if  motorA_data == 0 :
        motorA_data_out = " OFF - خاموش "
        A = "OFF"
    if motorA_data == 1 :
        motorA_data_out = " ON - روشن "
        A = "ON "

    if  motorB_data == 0 :
        motorB_data_out = " OFF - خاموش "
        B = "OFF"
    if motorB_data == 1 :
        motorB_data_out = " ON - روشن "
        B = "ON "

    if  motorC_data == 0 :
        motorC_data_out = " OFF - خاموش "
        C = "OFF"
    if motorC_data == 1 :
        motorC_data_out = " ON - روشن "
        C = "ON "

    if motorL_data == 0 :
        motorL_data_out = " OFF - خاموش "
        L = "OFF"
    if motorL_data == 1 :
        motorL_data_out = " ON - روشن "
        L = "ON "
        

    def print_data():
        with open("../Data/print_data.txt", "w") as file :
            file.write("    *** Data Systam *** \n External Temperature : %s \n Internal Temperature : %s \n Motor A : %s    PWM : %s \n Motor B : %s    PWM : %s \n Motor C : %s    PWM : %s \n Lamp    : %s    PWM : %s \n    *** ___________ ***"%
                       (sensorA_data,sensorB_data,A,pwmA,B,pwmB,C,pwmC,L,pwmL))
            file.close()
        while 1:
            os.chdir("../Data")
            os.startfile("print_data.txt", "print")
            break
        
    status = Tk()

    icon = PhotoImage(file='../Pictures/print.png')
    status.tk.call('wm', 'iconphoto', status._w, icon)

    screen_width = status.winfo_screenwidth()
    screen_height = status.winfo_screenheight()

    w = screen_width
    h = screen_height
    time = str(datetime.now())

    status.geometry("%sx%s+0+0"%(int(w),int(h)))

    # titel
    status.title("نرم افزار کنترل گلخانه هوشمند - پرينت وضعيت")

    #sensor
    Label(status, text="External Temperature").grid(row=0, column=0)
    Label(status, text=" %s C" % (sensorA_data)).grid(row=0, column=1)
    
    Label(status, text="Internal Temperature").grid(row=1, column=0)
    Label(status, text=" %s C" % (sensorB_data)).grid(row=1, column=1)
    
    #
    Label(status, text="  ").grid(row=2, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=2, column=1)
    
    #motor
    Label(status, text="Motor A").grid(row=3, column=0)
    Label(status, text=" %s " % (str(motorA_data_out))).grid(row=3, column=1)
    
    Label(status, text="Motor B").grid(row=4, column=0)
    Label(status, text=" %s " % (str(motorB_data_out))).grid(row=4, column=1)
    
    Label(status, text="Motor C").grid(row=5, column=0)
    Label(status, text=" %s " % (str(motorC_data_out))).grid(row=5, column=1)
    
    #
    Label(status, text="  ").grid(row=6, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=6, column=1)
    
    #lamp
    Label(status, text="Lamp").grid(row=7, column=0)
    Label(status, text=" %s " % (str(motorL_data_out))).grid(row=7, column=1)
    
    Label(status, text="Brightness").grid(row=8, column=0)
    Label(status, text=" %s " % (str(motorL_pwm_data_out))).grid(row=8, column=1)
    
    #
    Label(status, text="  ").grid(row=9, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=9, column=1)
    
    #btn
    Button(status, text="Exit", width=10, fg="red", command=status.destroy).grid(row=10, column=0)

    #time
    Label(status, text=time).grid(row=10, column=1)

    #btn
    Button(status, text="Print", width=10, fg="blue", command=print_data).grid(row=10, column=2)
    

    mainloop()

if __name__ == "__main__":
    run_status_print()

    
