import numpy as np
import matplotlib.pyplot as plt
import json

gra = open(r'przemyslGranice.geojson')
gran = gra.read()
granice = json.loads(gran)

lista = granice['features'][0]['geometry']['coordinates'][0]

args = []
vals = []
for i in lista:
    args.append(i[0])
    vals.append(i[1])
    
czuj = open(r'Czujniki_Przemysl.geojson')
czujn = czuj.read()
czujniki = json.loads(czujn)

czujargs = []
czujvals = []
for i in czujniki['features']:
    czujargs.append(i['geometry']['coordinates'][0])
    czujvals.append(i['geometry']['coordinates'][1])

plt.plot(args, vals)
plt.plot(czujargs, czujvals, 'ro')
plt.show()

