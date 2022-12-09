import os
import matplotlib
matplotlib.use("Agg")
from datetime import *
import requests
import matplotlib.pyplot as plt


#convert a datetime object into a total of seconds for use in plotting
def get_sec(t):
    i = 0
    temp = 3600
    list_f = []
    while i < 3:
       list_f.append(temp)
       temp = temp//60
       i = i + 1
    return sum([num1 * num2 for num1, num2 in zip(list_f, map(int, t.strftime("%H:%M:%S").split(':')))])

if __name__ == '__main__':
    z = 0
    j = 0
    de = []
    while j < 6:
        de.append(z)
        z = z + 100
        j = j + 1

    sec = []
    y = 0
    while y < 6:
        temp3 = 10*10
        delay = y * temp3
        d = delay
        Sd = "delay is: " + str(d)
        print("===================")
        print(Sd)
        print("===================")
        while y != 0:
            while y != 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
                break
            s = "sudo tc qdisc add dev eth0 root netem delay " + str(d) + "ms"
            print("==============================================================")
            print(s)
            print("==============================================================")
            os.system(s)
            break
        
        print("================================================")
        print("THE INITIAL TIME BEFORE SENDING ALL THE REQUESTS")
        print("================================================")
        
        t1 = datetime.now();
        time1 = t1
        print(time1)
        
        ii = 0
        while ii < 50:
            r = requests.get("http://www.umass.edu")
            ii = ii + 1
        
        print("================================================")
        print("THE FINAL TIME AFTER SENDING ALL THE REQUESTS")
        print("================================================")
        
        t2 = datetime.now();
        time2 = t2
        print(time2)
        
        g1 = get_sec(t1)
        g2 = get_sec(t2)
        BW_time = g2 - g1
        
        sec.append(BW_time)
        Sb = "to finish the requests it takes " + str(BW_time) + " seconds"
        
        print("==============================================================")
        print(Sb)
        print("==============================================================")
        print("\n")
        y = y + 1
    os.system("sudo tc qdisc del dev eth0 root netem")



    fig = plt.figure()
    plt.plot(de, sec, 'r+')
    plt.savefig("withoutCache_timeCost_vs_delay_umass50.png")




