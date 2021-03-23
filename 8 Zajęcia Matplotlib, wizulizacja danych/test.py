import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import urllib
import json

url = 'http://api.luftdaten.info/static/v1/data.json'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read()
data = json.loads(content)

g = open('przemyslGranice.geojson', 'r')
granice = g.read()
granice = json.loads(granice)

lista = granice['features'][0]['geometry']['coordinates'][0]
polyg = []
for i in range(0, len(lista)):
    polyg.append(tuple(lista[i]))

polyg = Polygon(polyg)

file = open('Czujniki_Przemysl.geojson', 'w')
geolista = []

for i in data:
    lat = i['location']['latitude']
    lon = i['location']['longitude']
    point = Point(float(lon), float(lat))
    if point.within(polyg) == True:
        geolista.append('a')
        geolista.append(str({"type":"Feature","geometry":{"type":"Point","coordinates":[lat, lon]}, "properties":{"id":123 }))    

wyjscie = '{"type": "FeatureCollection","features":{}}'.format(geolista)
file.write(wyjscie)