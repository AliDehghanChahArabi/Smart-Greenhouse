import time

while 1:
    t1 = open("/sys/bus/w1/devices/28-000008ee69e8/w1_slave")
    data1 = t1.read()
    t1.close()
    t_data1 = data1.split('\n')[1].split(' ')[9]
    temp1 = float(t_data1[2:])
    temp1 = temp1 / 1000
	
    print (temp1)

    with open("in_s.txt", "w") as file:
        file.write(str(temp1))
        file.close()
                
    time.sleep(1)
