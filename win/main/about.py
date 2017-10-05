from tkinter import *

def about():
    status = Tk()

    screen_width = status.winfo_screenwidth()
    screen_height = status.winfo_screenheight()

    w = (screen_width/4)+30
    h = screen_height/4
    
    status.geometry("%sx%s+0+0"%(int(w),int(h)))

    # titel
    status.title("نرم افزار کنترل گلخانه هوشمند - درباره ما")

    #sensor
    Label(status, text="""
نرم افزار کنترل گلخانه هوشمند - نسخه 1.0

گلخانه به وسيله يک ميني رايانه هوشمند مدل رزبري پاي نسخه 3
و سيستم عامل رزبين و کد نويسي پايتون انجام گرديده است.

ايده و سازنده طرح : مهندس عليرضا اميني
طراحي و پياده سازي نرم افزار : علي دهقان

www.alidehqan.com
en.alidehghan@gmail.com
+98 912 088 3990

""").grid(row=0, column=0)

    #btn
    Button(status, text="Exit", width=10, fg="red", command=status.destroy).grid(row=10, column=0)



    mainloop()

if __name__ == "__main__":
    about()

    
