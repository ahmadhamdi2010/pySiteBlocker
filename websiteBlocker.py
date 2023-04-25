import time
from datetime import datetime as dt

tempHostPath = "hosts"
hostsPath = "C:\Windows\System32\drivers\etc\hosts"
redirectIp = "127.0.0.1"
blockedSites = ["www.facebook.com","facebook.com"]

startHour = 15
endHour = 16

while True :
    time.sleep(5)
    print(1)
    if dt.now().hour in range(startHour,endHour,1):
        print("Working hours...")
        with open(tempHostPath, 'r+' ) as file:
            content = file.read()
            #print(content)
            for address in blockedSites:
                if address in content :
                    pass
                else:
                    file.write(redirectIp + " " + address + "\n")


    else:

        with open(tempHostPath, 'r+' ) as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blockedSites):
                    file.write(line)
            
            file.truncate()


        print("Fun Hour...")

    
     