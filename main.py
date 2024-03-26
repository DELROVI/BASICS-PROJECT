import requests
import json
import win32com.client 
try:

    #ENTER YOUR API KEY(WEATHER)
    API_KEY=1234                  #ENTER HERE replacing 1234
    while True:
        city=input("ENter the name of the city")
        url=f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        r=requests.get(url)
        print(r.text)
        # print(type(r.text))
        wdic=json.loads(r.text)
        w= wdic["current"]["temp_f"]
        speaker=win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"The current temperature of {city} is {w} Fahrenheit")
except:
    print("Invalid input")
