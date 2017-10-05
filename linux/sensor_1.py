import time

while 1:
    t = open("/sys/bus/w1/devices/28-000008eecbdc/w1_slave")
    data = t.read()
    t.close()
    t_data = data.split('\n')[1].split(' ')[9]
    temp = float(t_data[2:])
    temp = temp / 1000
        
    print (temp)

    with open("ex_s.txt", "w") as file :
        file.write (str(temp))
        file.close()
    time.sleep(1)
