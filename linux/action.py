while True:
    import time
    import connector
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)

    F1 = GPIO.PWM(5, 50)
    F2 = GPIO.PWM(6, 50)
    F3 = GPIO.PWM(13, 50)
    F4 = GPIO.PWM(19, 50)

    data = connector.Action()
    load_data = data.data()

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

    v = load_data['normal']
    normal = magic(v)
    
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

    v = load_data['in_s']
    IN = magic1(v)
#____________________
    a = raw_input = int()
    if a ==1:
        

        F1.start (PWMA)
        F2.start (PWMB)
        F3.start (PWMC)
        F4.start (PWML)

        print (MA,MB,MC)

    if a==0:
        F1.start(0)
        F4.start(0)
        F3.start(0)
        F2.start(0)


        
    
        

    
        
