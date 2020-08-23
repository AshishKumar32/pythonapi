from urllib.request import urlopen
import json
import requests

a=1
api_url = 'https://api.weatherbit.io/v2.0/forecast/daily?city='
city = 'Ranchi'
key = '&key=265e271bcfdb4aa9a8691cd749e204f7'


def search():
    api_key = key
    url = api_url + api_key
    city=input("Enter City : ")
    url = api_url + city + api_key
    j = requests.get(url)
    data = j.json()
    print("The Temperature in " + city + " is " , data['data'][0]['temp'] , " degree Celcius")
    return
    
    

while (a==1):
    search()
    a=int(input("Enter 0 to exit or 1 to continue : "))



