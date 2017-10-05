#from flask import Flask
import os

class Set_Data():
    def __init__ (self, motorA = "0",pwmA = "0",hA = "0",mA = "0",
                  motorB = "0",pwmB = "0",hB = "0",mB = "0",
                  motorC = "0",pwmC = "0",hC = "0",mC = "0",
                  motorL = "0",pwmL = "0",hL = "0",mL = "0",
                  element = "0", normal = "0", coler = "0"):
        self.motorA = str(motorA)
        self.motorB = str(motorB)
        self.motorC = str(motorC)
        self.motorL = str(motorL)

        self.pwmA = str(pwmA)
        self.pwmB = str(pwmB)
        self.pwmC = str(pwmC)
        self.pwmL = str(pwmL)

        self.hA = str(hA)
        self.hB = str(hB)
        self.hC = str(hC)
        self.hL = str(hL)

        self.mA = str(mA)
        self.mB = str(mB)
        self.mC = str(mC)
        self.mL = str(mL)

        self.element = str(element)
        self.normal = str(normal)
        self.coler = str(coler)

    def set_data(self):
        with open("MotorA.txt", "w") as file:
            file.write(self.motorA)
            file.close()
        with open("MotorB.txt", "w") as file:
            file.write(self.motorB)
            file.close()
        with open("MotorC.txt", "w") as file:
            file.write(self.motorC)
            file.close()
        with open("MotorL.txt", "w") as file:
            file.write(self.motorL)
            file.close()
        with open("pwmA.txt", "w") as file:
            file.write(self.pwmA)
            file.close()
        with open("pwmB.txt", "w") as file:
            file.write(self.pwmB)
            file.close()
        with open("pwmC.txt", "w") as file:
            file.write(self.pwmC)
            file.close()
        with open("pwmL.txt", "w") as file:
            file.write(self.pwmL)
            file.close()
        with open("hA.txt", "w") as file:
            file.write(self.hA)
            file.close()
        with open("hB.txt", "w") as file:
            file.write(self.hB)
            file.close()
        with open("hC.txt", "w") as file:
            file.write(self.hC)
            file.close()
        with open("hL.txt", "w") as file:
            file.write(self.hL)
            file.close()
        with open("mA.txt", "w") as file:
            file.write(self.mA)
            file.close()
        with open("mB.txt", "w") as file:
            file.write(self.mB)
            file.close()
        with open("mC.txt", "w") as file:
            file.write(self.mC)
            file.close()
        with open("mL.txt", "w") as file:
            file.write(self.mL)
            file.close()
        with open("element.txt", "w") as file:
            file.write(self.element)
            file.close()
        with open("normal.txt", "w") as file:
            file.write(self.normal)
            file.close()
        with open("coler.txt", "w") as file:
            file.write(self.coler)
            file.close()
            
class Load_Data():
    def read_data(self):
        with open("MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("element.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("normal.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("coler.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("ex_s.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("in_s.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        with open("gas.txt", "r") as file:
            g = list(file.read())
            file.close()
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL,
                     'hA' : hA, 'hB' : hB, 'hC' : hC, 'hL' : hL,
                     'mA' : mA, 'mB' : mB, 'mC' : mC, 'mL' : mL,
                     'element' : I1 ,'normal' : I2, 'coler' : I3,
                     'ex_s' : ex_s, 'in_s' : in_s, 'gas' : g}
        return list_data
    
class WEB():
    def show_page(self):
        with open("MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("element.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("normal.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("coler.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("ex_s.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("in_s.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        with open("gas.txt", "r") as file:
            g = list(file.read())
            file.close()
        #app = Flask(__name__)
        #with open ("index.txt", "w") as file:
            #file.write(""" <ul class="nav nav-pills pull-right">
                          #welcome
                          #<li> Motor A = %s </li>
                          #</ul>"""%(motorA))
        #@app.route("/")
        #def data():
            #with open ("index.txt", "r") as file:
                #web = file.read()
                #return web
        #app.run()
        print ("show page OK")
    
class Print():
    def printer(self):
        with open("MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("element.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("normal.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("coler.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("ex_s.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("in_s.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        with open("gas.txt", "r") as file:
            g = list(file.read())
            file.close()
        with open("printer.txt", "w") as file:
            file.write(""" **** Data System ****
                           Fan A : %s"""%(motorA))
            file.close()
        #os.startfile("printer.txt", "print")
        print ("print OK")

class Sensor():
    def read(self):
        with open("ex_s.txt", "r") as file:
            EX = list(file.read())
            file.close()
        with open("in_s.txt", "r") as file:
            IN = list(file.read())
            file.close()
        list_data = {'ex_s' : EX, 'in_s' : IN}
        return list_data

class Action():
    def data(self):
        with open("MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("element.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("normal.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("coler.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("ex_s.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("in_s.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL,
                     'hA' : hA, 'hB' : hB, 'hC' : hC, 'hL' : hL,
                     'mA' : mA, 'mB' : mB, 'mC' : mC, 'mL' : mL,
                     'element' : I1 ,'normal' : I2, 'coler' : I3,
                     'ex_s' : ex_s, 'in_s' : in_s}
        return list_data
        
    
if __name__ == "__main__":
    s = Load_Data()
    s.read_data()
    print(s)
