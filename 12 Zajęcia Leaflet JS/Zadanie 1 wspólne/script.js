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

var myIcon1 = L.icon({
    iconUrl: 'gardening.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32],
});

var myIcon2 = L.icon({
    iconUrl: 'tree.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32],
});

function toggleLayer(){
    if (mymap.hasLayer(mark1)){
        mymap.removeLayer(mark1);
    }
    else{
        mymap.addLayer(mark1);
    };
};
const mark1 = L.marker([49.780145, 22.786583],{icon: myIcon1}).addTo(mymap)
    .bindPopup("Drzewo 1").openPopup();

mark1.on("mouseover", function(e){
    mark1.setIcon(myIcon2)
}).addTo(mymap)

mark1.on("mouseout", function(e){
    mark1.setIcon(myIcon1)
}).addTo(mymap)

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

