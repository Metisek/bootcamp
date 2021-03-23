import matplotlib.pyplot as plt
import geopandas as gpd

granice = gpd.read_file('przemyslGranice.geojson')
punkty = gpd.read_file('Czujniki_Przemysl.geojson')

plt.figsize = (20, 10)

ax = granice.plot(color='blue')

for idx, row in punkty.iterrows():
    coordinates = row['geometry'].coords.xy
    x, y = coordinates[0][0], coordinates[1][0]
    ax.annotate(row['id'], xy=(x, y), xytext = (x,y), fontsize = 1 )

z = punkty.plot(ax=ax, scheme='quantiles', cmap='OrRd')
ff = z.get_figure()
ff.savefig('miasto.svg')
ff.show()

# Plik powinien się zapisać w katalogu zadania