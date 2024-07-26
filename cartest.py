from grovepi import *
import time
import requests
import json

usr = [2,3]
beper = 0

while True:
    try:
        carper = 0
        
        for n in range(len(usr)):
            distance = ultrasonicRead(usr[n])
        
            if distance <= 4:
                carper += 1 / len(usr)
            
            print(distance)
        
        
        per = round(carper,2)
        print(per)
        
        if beper != per:
            
            url = "https://0fae-125-103-133-46.ngrok-free.app"
            jdata = {'parkingId': 'byoin', 'percent': per}
            res = requests.post(url, json = jdata)
            print(res.text)
            
            beper = per
            print(beper)
        
        time.sleep(1.0)
        
    except KeyboardInterrupt:
        break
    
    except IOError:
        print("Error")
        break
