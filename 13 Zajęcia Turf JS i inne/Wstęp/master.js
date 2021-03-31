var map = L.map('mapid').setView([52.25, 21], 12);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox/streets-v11',
	tileSize: 512,
	zoomOffset: -1
}).addTo(map);

// var points = turf.randomPoint(30, {bbox: [20.92950381,52.195038,21.094045,52.295152]});

// turf.featureEach(points, function(point) {
//     point.properties.solRad = Math.random() * 10;
// });

// L.geoJSON(points, {
//     onEachFeature: function(feature, layer){
//         layer.bindPopup('<p>'+feature.properties.solRad+'</p>');
//     }
// }).addTo(map);



// var options = {gridType: 'hex', property: 'solRad', units:'kilometers'};
// var grid = turf.interpolate(points, 1, options);
// console.log(grid);

// L.geoJSON(grid, {
//     style: function (feature) {
//         return {color: '#1a53'+Math.round(feature.properties.solRad*10),
//                 weight: 1,
//                 fillColor: '#0fff'+Math.round(feature.properties.solRad*10)};
//     },
//     onEachFeature: function(feature, layer){
//         layer.bindPopup('<p>'+(feature.properties.solRad)+'</p>');
//     }
// }).addTo(map);



// L.geoJSON(ptwp, {
//     style: function(feature){
//         return {color: '#05c9f5', weight: 1}
//     }
// }).addTo(map);

// var buffered = turf.buffer(ptwp, 0.2, {units: 'kilometers'});

// L.geoJSON(buffered, {
//     style: function(feature){
//         return {color: '#f58d05', weight: 1}
//     }
// }).addTo(map);



// L.geoJSON(rezerwat, {
//     style: function(feature){
//         return {color: '#046e1d', weight: 1}
//     }
// }).addTo(map);

// L.geoJSON(teren, {
//     style: function(feature){
//         return {color: '#c95cff', weight: 1}
//     }
// }).addTo(map);
    
// var intersection = turf.intersect(rezerwat, teren);
    
// L.geoJSON(intersection, {
//     style: function(feature){
//         return {color: 'red', weight: 3, fillOPacity:0.8}
//     }
// }).addTo(map);



// L.geoJSON(rezerwat, {
//     style: function(feature){
//         return {color: '#046e1d', weight: 1}
//     }
// }).addTo(map);
   
// var centroid = turf.centroid(rezerwat);
    


// L.marker([centroid.geometry.coordinates[1], centroid.geometry.coordinates[0]]).addTo(map);

// var lotniskoChopina = turf.point([20.96637725830078, 52.167720082876045]);
// var longIslandAirport = turf.point([-73.10062408447266, 40.79899672300568]);
    
// L.marker([lotniskoChopina.geometry.coordinates[1],
//     lotniskoChopina.geometry.coordinates[0]]).addTo(map);
// L.marker([longIslandAirport.geometry.coordinates[1],
//     longIslandAirport.geometry.coordinates[0]]).addTo(map);

// var greatCircle = turf.greatCircle(lotniskoChopina, longIslandAirport);
// L.geoJSON(greatCircle).addTo(map);



// L.geoJSON(rezerwat, {
//     style: function(feature){
//         return {color: '#046e1d', weight: 1}
//     }
// }).addTo(map);
    
// var options = {tolerance: 0.001, highQuality: true};
// var simplified = turf.simplify(rezerwat, options);
    
// L.geoJSON(simplified, {
//     style: function(feature){
//         return {color: '#26d902', weight: 1}
//     }
// }).addTo(map);


// var points = turf.randomPoint(30, {bbox: [20.5,52,21,52.5]});
// var ptsWithin = turf.pointsWithinPolygon(points, warszawa);
// L.geoJSON(warszawa).addTo(map);
// L.geoJSON(ptsWithin).addTo(map);


 
// var bbox = [20.92950381,52.195038,21.094045,52.295152];
// var cellSide = 0.5;
// var options = {units: 'kilometers'};

// var squareGrid = turf.squareGrid(bbox, cellSide, options);
// L.geoJSON(squareGrid).addTo(map);



var points = turf.randomPoint(45, {bbox: [20.92950381,52.195038,21.094045,52.295152]});
var options = {numberOfClusters: 4};
var clustered = turf.clustersKmeans(points, options);
var clusterColors = {0:'red', 1:'blue', 2:'green', 3:'yellow'};
L.geoJSON(clustered, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 8,
            fillColor: clusterColors[feature.properties.cluster],
            color: 'black',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });
    }  
}).addTo(map);
