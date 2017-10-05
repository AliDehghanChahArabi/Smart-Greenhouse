import connector
import time

while 1:
      def magic(numList):         # [1,2,3]
        s = map(str, numList)   # ['1','2','3']
        s = ''.join(s)          # '123'
        s = int(s)              # 123
        return s
      
      data = connector.Action()
      s_data = data.read_data()

      sensorA = magic(s_data['in'])
      sensorB = magic(s_data['ex'])

      i1 = magic(s_data['i1'])
      i2 = magic(s_data['i2'])
      i3 = magic(s_data['i3'])

      e1 = magic(s_data['e1'])
      e2 = magic(s_data['e2'])
      e3 = magic(s_data['e3'])

      a = magic(s_data['A'])
      b = magic(s_data['B'])
      c = magic(s_data['C'])
      l = magic(s_data['L'])

      hL = magic(s_data['hL'])
      mL = magic(s_data['mL'])

      pwmA = magic(s_data['pA'])
      pwmB = magic(s_data['pB'])
      pwmC = magic(s_data['pC'])
      pwmL = magic(s_data['pL'])

      print (i1,i2,i3,e1,e2,e3,a,b,c,l,pwmA,pwmB,pwmC,pwmL)
      
      if sensorB == i3  :
            print ("m1 - on")

      if sensorB < i3 :
            print ("m1,2,3 and elemt - on")

      if sensorB > i3 :
            print ("m1,2,3 and coler - on")

      if l == 1:
            print ("Lamp On." + str(pwmL), str(hL), str(mL)) 
      time.sleep (5)
