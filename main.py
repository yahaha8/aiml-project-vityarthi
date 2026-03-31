import requests
from datetime import datetime

API_KEY="d77233f4939c5a7b515b33d023f5d934"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"



while True:
    place=input("enter the place name (or type exit): ")

    if place.lower()=="exit":
        print("program ended")
        break

    url=f"{BASE_URL}?q={place}&appid={API_KEY}&units=metric"


    try:
        response=requests.get(url)
        data=response.json()
    except:
        print("error fetching data")
        continue


    if data["cod"]==200:
        n=data["name"]
        w=data["weather"][0]["description"]
        m1=data["main"]["temp_min"]
        m2=data["main"]['temp_max']
        m3=data["main"]['pressure']
        m4=data["main"]['humidity']
        y=data["wind"]['speed']

      
        feels=data["main"]["feels_like"]
        country=data["sys"]["country"]

        sunr=data["sys"]['sunrise']
        suns=data["sys"]['sunset']

        # converting the UNIX time to normal time
        sunr=datetime.fromtimestamp(sunr)
        suns=datetime.fromtimestamp(suns)

        # formatting the time for better display 
        sunr=sunr.strftime("%H:%M:%S")
        suns=suns.strftime("%H:%M:%S")


        print("\n-----------------------------")

        print(f"name={n}, country={country}")
        print(f"weather={w}")
        print(f"temp_min={m1}degcelcius")
        print(f"temp_max={m2}degcelcius")
        print(f"feels_like={feels}degcelcius")
        print(f"pressure={m3}")
        print(f"humidity={m4}")
        print(f"wind speed={y}")
        print(f"sunrise={sunr}")
        print(f"sunset={suns}")

        print("-----------------------------\n")


    else:
        print("place not found ")