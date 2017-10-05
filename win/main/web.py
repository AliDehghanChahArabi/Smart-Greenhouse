import connector
from flask import Flask

while 1:
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
    
    app = Flask(__name__)


    with open ("index.txt","w") as file:
    	file.write("""  <ul class="nav nav-pills pull-right">
	                   welcome 
 
                                <li>MOTOR A = %s    PWM = %s    H = %s    M = %s</li>

                                <li>MOTOR B = %s    PWM = %s    H = %s    M = %s</li>

                                <li>MOTOR C = %s    PWM = %s    H = %s    M = %s</li>

                                <li>LAMP       = %s    PWM = %s    H = %s    M = %s</li>

                                <li>External Sensor = %s</li>

                                <li>Internal   Sensor = %s</li>
         
                                </ul>"""  %(motorA,PwmA,hA,mA, motorB,PwmB,hB,mB, motorC,PwmC,hC,mC, motorL,PwmL,hL,mL, ex_s, in_s))
	
    @app.route("/")
    def hello():
        with open ("index.txt","r") as file:
            web = file.read()
            return web    

    app.run()
        
