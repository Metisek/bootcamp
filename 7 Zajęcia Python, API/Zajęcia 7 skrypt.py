import urllib
import json
import requests

# Praca z Airly

apikey = 'xZTN60Vo93VwbDBtVKq5AmTUSaumkIJm'

# Wyświetlanie danych obed

url = 'https://airapi.airly.eu/v2/measurements/nearest?lat=49.4705&lng=22.4602&maxDistanceKM=50'

req = urllib.request.Request(url, headers={'apikey':apikey})
resp = urllib.request.urlopen(req)
content = resp.read()

data = json.loads(content)

currentParameters = data['current']['values']
print(currentParameters)