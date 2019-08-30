import requests
import json
import time

def wakingup(self, duration):

    url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"
    
    counter = 1

    #calculate the time steps by given duration to fully light up
    time_per_step = duration / 254

    for i in range(1, 254):
        # creating command for hue bridge
        data = {"on":True, "bri":counter}
        #data_off = {"on":False}

        # sending command via hue bridge to bulb
        r = requests.put(url, json.dumps(data), timeout=5)

        # wait for the next brightness step
        time.sleep(time_per_step)
        counter = counter + 1
        
    pass

