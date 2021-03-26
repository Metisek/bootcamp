var mymap = L.map('mapid').setView([49.780145, 22.786583], 13);

// Podkład topograficzny

// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
//     maxZoom: 18,
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
//         'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1
// }).addTo(mymap);

var CartoDB_DarkMatter = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
}).addTo(mymap);

// Koniec podkładu

var myIcon = L.icon({
    iconUrl: 'tower.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32],
});


L.marker([49.780145, 22.786583]).addTo(mymap)
    .bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

L.marker([49.781264, 22.835083], {icon: myIcon}).addTo(mymap)
    .bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();
L.circle([49.770622, 22.752686], 30, {
    color: '#cc00cc',
    fillColor: "#FF00FF",
    fillOpacity: 0.5,
}).addTo(mymap)

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

L.geoJSON(przemysl, {
    style: function(feature) {
        return {color: '#99ff99',
        fillColor: '#ffffcc',
        fillOpacity: 0.1};
    }
}).addTo(mymap);

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
}

mymap.on('click', onMapClick);

let myRequest = new XMLHttpRequest();
myRequest.open('GET', 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson')

myRequest.onload = function(){
    let earthquakes = JSON.parse(myRequest.responseText);
    window.earthquakes = L.geoJSON(earthquakes, {
        onEachFeature: function(feature, layer){
            layer.bindPopup('<p><b>Earthquake location: </b>'+ feature.properties.place +
            '</p><p><b> Magnitude: </b>' + feature.properties.mag+'</p>')
        }
    }).addTo(mymap) 
}
myRequest.send()