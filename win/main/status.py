import connector
from tkinter import *
from datetime import datetime

def run_status():
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

    motorA_data_out = ""
    motorB_data_out = ""
    motorC_data_out = ""
    motorL_data_out = ""

    
    if  motorA_data == 0 :
        motorA_data_out = " OFF - خاموش "
    if motorA_data == 1 :
        motorA_data_out = " ON - روشن "

    if  motorB_data == 0 :
        motorB_data_out = " OFF - خاموش "
    if motorB_data == 1 :
        motorB_data_out = " ON - روشن "

    if  motorC_data == 0 :
        motorC_data_out = " OFF - خاموش "
    if motorC_data == 1 :
        motorC_data_out = " ON - روشن "

    if  motorL_data == 0 :
        motorL_data_out = " OFF - خاموش "
    if motorL_data == 1 :
        motorL_data_out = " ON - روشن "
     
    
    status = Tk()

    icon = PhotoImage(file='../Pictures/s.png')
    status.tk.call('wm', 'iconphoto', status._w, icon)

    screen_width = status.winfo_screenwidth()
    screen_height = status.winfo_screenheight()

    w = screen_width
    h = screen_height
    time = str(datetime.now())

    status.geometry("%sx%s+0+0"%(int(w),int(h)))

    # titel
    status.title("نرم افزار کنترل گلخانه هوشمند - نمايش وضعيت")

    #sensor
    Label(status, text="External Temperature").grid(row=0, column=0)
    Label(status, text=" %s C" % (sensorA_data)).grid(row=0, column=1)
    Label(status, text="دماي خارجي").grid(row=0, column=2)

    Label(status, text="Internal Temperature").grid(row=1, column=0)
    Label(status, text=" %s C" % (sensorB_data)).grid(row=1, column=1)
    Label(status, text="دماي داخلي").grid(row=1, column=2)

    #
    Label(status, text="  ").grid(row=2, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=2, column=1)
    Label(status, text="  ").grid(row=2, column=2)

    #motor
    Label(status, text="Motor A").grid(row=3, column=0)
    Label(status, text=" %s " % (str(motorA_data_out))).grid(row=3, column=1)
    Label(status, text="موتور يک").grid(row=3, column=2)

    Label(status, text="Motor B").grid(row=4, column=0)
    Label(status, text=" %s " % (str(motorB_data_out))).grid(row=4, column=1)
    Label(status, text="موتور دو").grid(row=4, column=2)

    Label(status, text="Motor C").grid(row=5, column=0)
    Label(status, text=" %s " % (str(motorC_data_out))).grid(row=5, column=1)
    Label(status, text="موتور سه").grid(row=5, column=2)

    #
    Label(status, text="  ").grid(row=6, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=6, column=1)
    Label(status, text="  ").grid(row=6, column=2)

    #lamp
    Label(status, text="Lamp").grid(row=7, column=0)
    Label(status, text=" %s " % (str(motorL_data_out))).grid(row=7, column=1)
    Label(status, text="چراغ").grid(row=7, column=2)

     #
    Label(status, text="  ").grid(row=9, column=0)
    Label(status, text=" %s " % ("  ")).grid(row=9, column=1)
    Label(status, text="  ").grid(row=9, column=2)

    #btn
    Button(status, text="Exit", width=10, fg="red", command=status.destroy).grid(row=10, column=0)

    #time
    Label(status, text=time).grid(row=10, column=1)
    Label(status, text=" ").grid(row=10, column=2)


    mainloop()

if __name__ == "__main__":
    run_status()

    
