import requests
import json
import time
import pprint
import matplotlib.pyplot as plt
from api_key import key


lat, lon = 59.57, 30.19
dt = int(time.time())


def get_weather(lat, lon, key, dt):

    day_month_hour = []
    temp_hour = []
    
    for day in range(5):
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall/timemachine?'
            f'lat={lat}&lon={lon}&dt={dt}&appid={key}&units=metric').json()
           
        for item in req['hourly']:
            day_month_hour.append(f"{time.localtime(item['dt'])[2]}/{time.localtime(item['dt'])[1]}({time.localtime(item['dt'])[3]}) = {item['temp']}")
            temp_hour.append(item['temp'])
            
        dt -= 60 * 60 * 24

    
    sort_day_month_hour = []
    sort_temp_hour = []
    for i in range(5):
        sort_day_month_hour.extend(day_month_hour[-24:])
        day_month_hour = day_month_hour[:len(day_month_hour)-24]
        sort_temp_hour.extend(temp_hour[-24:])
        temp_hour = temp_hour[:len(temp_hour)-24]

    return sort_day_month_hour, sort_temp_hour


date, temp = get_weather(lat, lon, key, dt)


def visualization(date, temp):

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(date, temp)  # Plot some data on the axes.
    plt.show()

visualization(date, temp)