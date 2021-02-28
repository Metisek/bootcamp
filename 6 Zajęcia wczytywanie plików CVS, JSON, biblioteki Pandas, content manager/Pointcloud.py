import geopandas as gp

warszawa = gp.read_file(r'C:\Users\User\Projekty\bootcamp\6 Zajęcia wczytywanie plików CVS, JSON, biblioteki Pandas, content manager\Pliki\graniceWarszawyWGS84.shp')
warszawa.plot(figsize=(12, 12), color='#c5d4c9')

import matplotlib.pyplot as plt

plt.savefig('zdjęcie.svg')

import numpy as np
x = np.random.rand(100, 3)
import pptk
v = pptk.viewer(x)
v.set(point_size=0.01)
