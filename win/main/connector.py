class Smart_Control():
    def __init__ (self, motorA = "0",pwmA = "0",hA = "0",mA = "0", motorB = "0",pwmB = "0",hB = "0",mB = "0", motorC = "0",pwmC = "0",hC = "0",mC = "0", motorL = "0",pwmL = "0",hL = "0",mL = "0", I1 = "0", I2 = "0", I3 = "0", E1 = "0",E2 = "0",E3 = "0"):
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

        self.I1 = str(I1)
        self.I2 = str(I2)
        self.I3 = str(I3)

        self.E1 = str(E1)
        self.E2 = str(E2)
        self.E3 = str(E3)
        
    def set_data(self):
        with open("../Data/MotorA.txt", "w") as file:
            file.write(self.motorA)
            file.close()
        with open("../Data/MotorB.txt", "w") as file:
            file.write(self.motorB)
            file.close()
        with open("../Data/MotorC.txt", "w") as file:
            file.write(self.motorC)
            file.close()
        with open("../Data/MotorL.txt", "w") as file:
            file.write(self.motorL)
            file.close()
        with open("../Data/pwmA.txt", "w") as file:
            file.write(self.pwmA)
            file.close()
        with open("../Data/pwmB.txt", "w") as file:
            file.write(self.pwmB)
            file.close()
        with open("../Data/pwmC.txt", "w") as file:
            file.write(self.pwmC)
            file.close()
        with open("../Data/pwmL.txt", "w") as file:
            file.write(self.pwmL)
            file.close()
        with open("../Data/hA.txt", "w") as file:
            file.write(self.hA)
            file.close()
        with open("../Data/hB.txt", "w") as file:
            file.write(self.hB)
            file.close()
        with open("../Data/hC.txt", "w") as file:
            file.write(self.hC)
            file.close()
        with open("../Data/hL.txt", "w") as file:
            file.write(self.hL)
            file.close()
        with open("../Data/mA.txt", "w") as file:
            file.write(self.mA)
            file.close()
        with open("../Data/mB.txt", "w") as file:
            file.write(self.mB)
            file.close()
        with open("../Data/mC.txt", "w") as file:
            file.write(self.mC)
            file.close()
        with open("../Data/mL.txt", "w") as file:
            file.write(self.mL)
            file.close()
        with open("../Data/I1.txt", "w") as file:
            file.write(self.I1)
            file.close()
        with open("../Data/I2.txt", "w") as file:
            file.write(self.I2)
            file.close()
        with open("../Data/I3.txt", "w") as file:
            file.write(self.I3)
            file.close()
        with open("../Data/E1.txt", "w") as file:
            file.write(self.E1)
            file.close()
        with open("../Data/E2.txt", "w") as file:
            file.write(self.E2)
            file.close()
        with open("../Data/E3.txt", "w") as file:
            file.write(self.E3)
            file.close()
            
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("../Data/hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("../Data/hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("../Data/hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("../Data/hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("../Data/mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("../Data/mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("../Data/mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("../Data/mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("../Data/I1.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("../Data/I2.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("../Data/I3.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("../Data/E1.txt", "r") as file:
            E1 = list(file.read())
            file.close()
        with open("../Data/E2.txt", "r") as file:
            E2 = list(file.read())
            file.close()
        with open("../Data/E3.txt", "r") as file:
            E3 = list(file.read())
            file.close()
        with open("../Data/ex_sensor.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("../Data/in_sensor.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL,
                     'hA' : hA, 'hB' : hB, 'hC' : hC, 'hL' : hL, 'mA' : mA, 'mB' : mB, 'mC' : mC, 'mL' : mL,
                     'i1' : I1 ,'i2' : I2, 'i3' : I3, 'e1' : E1, 'e2' : E2, 'e3' : E3,
                     'ex_s' : ex_s, 'in_s' : in_s}
        return list_data

class Manual_Control():
    def __init__ (self, motorA = "0",pwmA = "0", motorB = "0",pwmB = "0", motorC = "0",pwmC = "0", motorL = "0",pwmL = "0"):
        self.motorA = str(motorA)
        self.motorB = str(motorB)
        self.motorC = str(motorC)
        self.motorL = str(motorL)

        self.pwmA = str(pwmA)
        self.pwmB = str(pwmB)
        self.pwmC = str(pwmC)
        self.pwmL = str(pwmL)
        
    def set_data(self):
        with open("../Data/MotorA.txt", "w") as file:
            file.write(self.motorA)
            file.close()
        with open("../Data/MotorB.txt", "w") as file:
            file.write(self.motorB)
            file.close()
        with open("../Data/MotorC.txt", "w") as file:
            file.write(self.motorC)
            file.close()
        with open("../Data/MotorL.txt", "w") as file:
            file.write(self.motorL)
            file.close()
        with open("../Data/pwmA.txt", "w") as file:
            file.write(self.pwmA)
            file.close()
        with open("../Data/pwmB.txt", "w") as file:
            file.write(self.pwmB)
            file.close()
        with open("../Data/pwmC.txt", "w") as file:
            file.write(self.pwmC)
            file.close()
        with open("../Data/pwmL.txt", "w") as file:
            file.write(self.pwmL)
            file.close()
            
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL,}
        return list_data

class Status():
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("../Data/ex_sensor.txt", "r") as file:
            ex_sensor = list(file.read())
            file.close()
        with open("../Data/in_sensor.txt", "r") as file:
            in_sensor = list(file.read())
            file.close()
        
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL, 'ex' : ex_sensor, 'in' : in_sensor}
        return list_data

class Status_Print():
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("../Data/ex_sensor.txt", "r") as file:
            ex_sensor = list(file.read())
            file.close()
        with open("../Data/in_sensor.txt", "r") as file:
            in_sensor = list(file.read())
            file.close()
        
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL, 'ex' : ex_sensor, 'in' : in_sensor}
        return list_data

class Action():
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("../Data/ex_sensor.txt", "r") as file:
            ex_sensor = list(file.read())
            file.close()
        with open("../Data/in_sensor.txt", "r") as file:
            in_sensor = list(file.read())
            file.close()
        with open("../Data/I1.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("../Data/I2.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("../Data/I3.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("../Data/E1.txt", "r") as file:
            E1 = list(file.read())
            file.close()
        with open("../Data/E2.txt", "r") as file:
            E2 = list(file.read())
            file.close()
        with open("../Data/E3.txt", "r") as file:
            E3 = list(file.read())
            file.close()
        with open("../Data/hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("../Data/mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL, 'ex' : ex_sensor, 'in' : in_sensor,
                     'i1' : I1, 'i2' : I2, 'i3' : I3,
                     'e1' : E1, 'e2' : E2, 'e3' : E3,
                     'hL' : hL, 'mL' : mL}
        return list_data
        

class WEB():
    def read_data(self):
        with open("../Data/MotorA.txt", "r") as file:
            motorA = list(file.read())
            file.close()
        with open("../Data/MotorB.txt", "r") as file:
            motorB = list(file.read())
            file.close()
        with open("../Data/MotorC.txt", "r") as file:
            motorC = list(file.read())
            file.close()
        with open("../Data/MotorL.txt", "r") as file:
            motorL = list(file.read())
            file.close()
        with open("../Data/pwmA.txt", "r") as file:
            pwmA = list(file.read())
            file.close()
        with open("../Data/pwmB.txt", "r") as file:
            pwmB = list(file.read())
            file.close()
        with open("../Data/pwmC.txt", "r") as file:
            pwmC = list(file.read())
            file.close()
        with open("../Data/pwmL.txt", "r") as file:
            pwmL = list(file.read())
            file.close()
        with open("../Data/hA.txt", "r") as file:
            hA = list(file.read())
            file.close()
        with open("../Data/hB.txt", "r") as file:
            hB = list(file.read())
            file.close()
        with open("../Data/hC.txt", "r") as file:
            hC = list(file.read())
            file.close()
        with open("../Data/hL.txt", "r") as file:
            hL = list(file.read())
            file.close()
        with open("../Data/mA.txt", "r") as file:
            mA = list(file.read())
            file.close()
        with open("../Data/mB.txt", "r") as file:
            mB = list(file.read())
            file.close()
        with open("../Data/mC.txt", "r") as file:
            mC = list(file.read())
            file.close()
        with open("../Data/mL.txt", "r") as file:
            mL = list(file.read())
            file.close()
        with open("../Data/I1.txt", "r") as file:
            I1 = list(file.read())
            file.close()
        with open("../Data/I2.txt", "r") as file:
            I2 = list(file.read())
            file.close()
        with open("../Data/I3.txt", "r") as file:
            I3 = list(file.read())
            file.close()
        with open("../Data/E1.txt", "r") as file:
            E1 = list(file.read())
            file.close()
        with open("../Data/E2.txt", "r") as file:
            E2 = list(file.read())
            file.close()
        with open("../Data/E3.txt", "r") as file:
            E3 = list(file.read())
            file.close()
        with open("../Data/ex_sensor.txt", "r") as file:
            ex_s = list(file.read())
            file.close()
        with open("../Data/in_sensor.txt", "r") as file:
            in_s = list(file.read())
            file.close()
        list_data = {'A' : motorA, 'B' : motorB, 'C' : motorC, 'L' : motorL,
                     'pA' : pwmA, 'pB' : pwmB, 'pC' : pwmC, 'pL' : pwmL,
                     'hA' : hA, 'hB' : hB, 'hC' : hC, 'hL' : hL, 'mA' : mA, 'mB' : mB, 'mC' : mC, 'mL' : mL,
                     'i1' : I1 ,'i2' : I2, 'i3' : I3, 'e1' : E1, 'e2' : E2, 'e3' : E3,
                     'ex_s' : ex_s, 'in_s' : in_s}
        return list_data
        
if __name__ == "__main__":
    s = Smart_Control()
    s.set_data()
