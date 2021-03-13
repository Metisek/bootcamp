import urllib
import json
import requests

# Praca z Airly

apikey = 'xZTN60Vo93VwbDBtVKq5AmTUSaumkIJm'

url = 'https://airapi.airly.eu/v2/measurements/nearest?lat=49.4705&lng=22.4602&maxDistanceKM=50'

req = urllib.request.Request(url, headers={'apikey':apikey})
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

currentParameters = data['current']['values']

# ----------------- #

lat = 49 + 47/60 + 5/3600
lon = 22 + 46/60 + 2/3600

url = 'https://airapi.airly.eu/v2/installations/nearest?lat={}&lng={}&maxDistanceKM=30&maxResults=10'\
    .format(str(lat), str(lon))
    
req = urllib.request.Request(url, headers={'apikey':apikey})
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)
print(data)

for obj in data:
    lan = obj['location']['latitude']
    lon = obj['location']['longitude']
    print(lan, lon)
    url = 'https://airapi.airly.eu/v2/measurements/point?lat={}&lng={}'.format(str(lat), str(lon))
    req = urllib.request.Request(url, headers={'apikey':apikey})
    resp = urllib.request.urlopen(req)
    content = resp.read()
    data = json.loads(content)
    print(data['current']['values'])
    print(30*"=")
    
    
# Praca z Luftdafen

url = 'http://api.luftdaten.info/static/v1/data.json'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

sz1 = 50.041229
dl1 = 21.9927
sz2 = 49.8253
dl2 = 22.8065

lista = []

for d in data:
    if sz2 <= float(d['Location']['Latitude']) <= sz2:
        
        
        
        
# GEOJSON trzęsienia ziemi

url  = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

# * do zrobienia *


# Praca z API USGS

import functools


@functools.lru_cache(maxsize=None)
def kurs():
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    content = resp.read()
    data = json.loads(content)
    return None

kurs()
print(data['rates'].keys())

for i in data['rates'].keys():
    print("1 EUR to", data['rates'].get(i), i)


# Wysyłanie maili

import smtplib

MailFrom = 'Uczestnik Bootcampu'
MailTo = 'matboj5@gmail.com'
MailSubject = 'TEST TEST TEST'

MailBody =\
    '''Czesc
    
    przesylam probnego maila.'''
    
message = '''From: {}
    Subject: {}
    
    {}'''.format(MailFrom, MailSubject, MailBody)
    
user = 'matboj10@gmail.com'
password = input("Podaj hasło: ")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(user, password)
server.sendmail(user, MailTo, message)
server.close()

print("Podano maila pomylnie")


# Pobieranie stron internetowych

def pobierzStroneWWW(url, directory, fileName):
    import os
    
    print("Rozpoczęto proces pobierania strony")
    
    r = requests.get(url, stream = True)
    file_path = os.path.join(directory, fileName)
    with open(file_path, 'wb') as f:
        f.write(r.content)
        
pobierzStroneWWW(r'https://www.programcreek.com/python/example/6443/smtplib.SMTP_SSL',
                 r'C:\Users\User\Projekty\bootcamp\7 Zajęcia Python, API\',
                 'index.html')


# Biblioteka shapely

from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

p1 = Point(24, 60)
p2 = Point(25, 65)

coords = [(24,25), (22,21), (20,23)]
Poligon = Polygon(coords)

print(p1.within(Poligon))

x,y = Poligon.exterior.xy
print(x)
print(y)

print(Poligon.area)


cords2 = [(0, 0), (1,0), (1,1), (0,1)]
kwadrat = Polygon(cords2)

print(kwadrat.area)


cords3 = [(-1,0), (0,2), (2,5), (5, -2)]
trojkat = Polygon(cords3)

print(trojkat.area)

print(trojkat.intersects(kwadrat))