import urllib
import json
import requests

# Praca z API Airly

apikey = '3Im4ALn4pqbRihkybONpv4Ey700CQzxA'

url = 'https://airapi.airly.eu/v2/measurements/nearest?lat=52.241685&lng=20.939932&maxDistanceKM=5'

req = urllib.request.Request(url, headers={'apikey':apikey})
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

currentParameters = data['current']['values']


# ========================== #
apikey = '3Im4ALn4pqbRihkybONpv4Ey700CQzxA'
lat = 49 + 47/60 + 5/3600
lon = 22 + 46/60 + 2/3600
url = 'https://airapi.airly.eu/v2/installations/nearest?lat={}&lng={}&maxDistanceKM=30&maxResults=10'\
    .format(str(lat), str(lon))
    
req = urllib.request.Request(url, headers={'apikey':apikey})
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

for obj in data:
    lat = obj['location']['latitude']
    lon = obj['location']['longitude']
    print(lat, lon)
    url = 'https://airapi.airly.eu/v2/measurements/point?lat={}&lng={}'.format(str(lat), str(lon))
    req = urllib.request.Request(url, headers={'apikey':apikey})
    resp = urllib.request.urlopen(req)
    content = resp.read()
    data = json.loads(content)
    print(data['current']['values'])
    print(30*"=")
    
    
# Praca z API Luftdaten  

url = 'http://api.luftdaten.info/static/v1/data.json'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

# Praca z API USGS    
    
r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')
print(r.status_code)
print(r.encoding)
print(r.text)
data = r.json()
print(data)

import functools

@functools.lru_cache()
def myRequest(url, myheaders=None):
    if myheaders == None:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        content = resp.read()
        return json.loads(content)
    else:
        req = urllib.request.Request(url, headers=myheaders)
        resp = urllib.request.urlopen(req)
        content = resp.read()
        return json.loads(content)
    
data = myRequest('https://api.exchangeratesapi.io/2010-01-12')


# Kurs Bitcoina
        
APIadress = 'https://api.coindesk.com/v1/bpi/currentprice.json'
resp = requests.get(APIadress)
jsonFile = resp.json()
print(jsonFile)

# Wysyłanie maili

MailFrom = "Prowadzacy BootCamp"
MailTo = "antek9797@gmail.com"
MailSubject = "TEST TEST TEST"

MailBody =\
'''Czesc

przesylam tego maila na probe.

Pozdrawiam

Antek'''

message = '''From: {}
Subject: {}

{}'''.format(MailFrom, MailSubject, MailBody)

import smtplib

user = 'antek9797@gmail.com'
password = input("Podaj hasło dla użytkownika {}".format(user))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(user, password)
server.sendmail(user, MailTo, message)
server.close()
print("Pomyślnie wysłano wiadomosć")

# Pobieranie stron internetowych

def pobierzStroneWWW(url, directory, fileName):
    import os
    
    print("Rozpoczęto proces pobierania strony")
    
    r = requests.get(url, stream=True)
    file_path = os.path.join(directory, fileName)
    with open(file_path, "wb") as f:
        f.write(r.content)
        

pobierzStroneWWW(r'https://docs.python.org/3/library/json.html',
                 r'C:\SmartFactor\BootCamp\zajecia7',
                 'dokumentacjaJSON.html')


from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)

coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poligon = Polygon(coords)


print(p1.within(poligon))
print(p2.within(poligon))

x,y = poligon.exterior.xy
print(x)
print(y)

print(poligon.area)

coords2 = [(0, 0), (1, 0), (1, 1), (0, 1)]
kwadrat = Polygon(coords2)

coords3 = [(0, 0), (1, 0), (1, 1)]
trojkat = Polygon(coords3)

print(kwadrat.area)
print(trojkat.area)

print(trojkat.intersects(kwadrat))
print(kwadrat.centroid)

plt.figure()
x,y = kwadrat.exterior.xy
plt.plot(x, y)
x,y = trojkat.exterior.xy
plt.plot(x, y)












    
    
    
    
    
    
    
    
    