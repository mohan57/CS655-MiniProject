import requests
from datetime import *
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
    PROX = {"http": "http://172.17.2.20:8080","https": "https://172.17.2.20:8080",}
    
    print("================================================")
    print("THE INITIAL TIME BEFORE SENDING ALL THE REQUESTS")
    print("================================================")
    
    t1 = datetime.now();
    time1 = t1
    print(time1)
    
    j = 0
    while j < 50:
        r = requests.get("http://www.umass.edu", proxies=PROX)
        j = j + 1
        
    print("================================================")
    print("THE FINAL TIME AFTER SENDING ALL THE REQUESTS")
    print("================================================")
    
    time2 = datetime.now();
    t2 = time2
    print(t2)
    
    g1 = get_sec(t1)
    g2 = get_sec(t2)
    BW_time = g2 - g1
    
    tot = "TIME TAKEN TO COMPLETE THE REQUESTS " + str(BW_time) + " seconds"
    print("==============================================================")
    print(tot)
    print("==============================================================")







