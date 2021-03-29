
var mymap = L.map('mapid').setView([51.505, -0.09], 13);

var CartoDB_DarkMatter = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
}).addTo(mymap);

var wmsLayer = L.tileLayer.wms('http://ows.mundialis.de/services/service?', {
    layers: 'TOPO-OSM-WMS'
}).addTo(mymap);

var basemaps = {'mapa topograficzna': CartoDB_DarkMatter,
								'mapa hipsometryczna': wmsLayer}

L.control.layers(basemaps).addTo(mymap);

L.marker([51.5, -0.09]).addTo(mymap)
	.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

L.circle([51.508, -0.11], 500, {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5
}).addTo(mymap).bindPopup("I am a circle.");

L.polygon([
	[51.509, -0.08],
	[51.503, -0.06],
	[51.51, -0.047]
]).addTo(mymap).bindPopup("I am a polygon.");

latlangs = [[51.54, -0.07],
            [51.56, -0.04],
            [51.53, -0.03]]

L.polyline(latlangs, {color: 'blue'}).addTo(mymap);

var myIcon = L.icon({
    iconUrl: 'arch-of-triumph.png',
    iconSize: [64, 64],
    iconAnchor: [32, 64],
    popupAnchor: [0, -64]
});

var newMarker = L.marker([51.49, -0.06], {icon:myIcon}).addTo(mymap);

newMarker.bindPopup("<div class='mypopup'> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>");

var popup = L.popup();

function onMapClick(e) {
	popup
		.setLatLng(e.latlng)
		.setContent("You clicked the map at " + e.latlng.toString())
		.openOn(mymap);
};

mymap.on('click', onMapClick);

mymap.on('mousemove', function(e){
	let lat = e.latlng.lat;
	let lon = e.latlng.lng;
	document.getElementById('coords').innerText=lat+', '+lon;
})

L.geoJSON(warszawa, {
    style: function (feature) {
        return {color: '#99ff99',
								fillColor: '#ffffcc',
								fillOpacity: 0.1};
    },
		onEachFeature: function(feature, layer){
			layer.on('mouseover', function(){
	      this.setStyle({fillColor: '#00ffff'})
	    });
	    layer.on('mouseout', function(){
	      this.setStyle({fillColor: '#ffffcc'})
			})
		}
}).addTo(mymap);

if('geolocation' in navigator) {
	navigator.geolocation.getCurrentPosition((position) => {
		L.marker([position.coords.latitude, position.coords.longitude]).bindPopup("<b>Geolokalizacja z przeglądarki</b>").addTo(mymap);
	});
};

var myRequest = new XMLHttpRequest();
myRequest.open('GET', 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson');
myRequest.onload = function(){
  var earthquakes = JSON.parse(myRequest.responseText);
  window.earthquakes = L.geoJSON(earthquakes, {
    onEachFeature: function(feature, layer){
      layer.bindPopup('<p><b>Earthquake location: </b>'+ feature.properties.place +
			'</p><p><b>Magnitude: </b>'+ feature.properties.mag +'</p>')}
  }).addTo(mymap);
};
myRequest.send();

function SearchEarthquakeByLocation(){
  var userInput = document.getElementById('filterByName').value;
  earthquakes.eachLayer(function(layer){
    if (layer.feature.properties.place.toLowerCase().indexOf(userInput.toLowerCase())>=1){
      layer.addTo(mymap)
    } else if(userInput ==''){
      layer.addTo(mymap)
    } else {
      mymap.removeLayer(layer);
    }
  })
};
