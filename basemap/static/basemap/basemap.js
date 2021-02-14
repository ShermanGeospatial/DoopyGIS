function parseLocation(pt){

  PointField = pt.value;
  console.log(PointField);
  var index1 = PointField.indexOf("(");
  var index2 = PointField.lastIndexOf(")");

  var cordString = PointField.substring(index1+1,index2);
  console.log(cordString);

  var index3 = cordString.indexOf(" ");

  var long = cordString.substring(0,index3);
  var lat = cordString.substring(index3+1);

  return [long,lat];
}

//YOUR TURN: add your Mapbox access token 
mapboxgl.accessToken = 'pk.eyJ1Ijoic2hlcm1hbmdlb3NwYXRpYWwiLCJhIjoiY2toZHUxa2M3MGcyaTJ6cGNlbTZrMXh6dSJ9.WfocGcVqEoUkeM79FIqHCA';

var mapstyle = document.getElementById("id_style");
var zoomLevel = document.getElementById("id_zoom");
var mapCenter = document.getElementById("id_location");

var map = new mapboxgl.Map({
  container: 'map', // container id
  style: "mapbox://styles/mapbox/" + mapstyle.value, //YOUR TURN: choose a style: https://docs.mapbox.com/api/maps/#styles
  center: parseLocation(mapCenter), // starting position [lng, lat]
  zoom: zoomLevel.value, // starting zoom
});

var geocodeWidget = new MapboxGeocoder({
  accessToken: mapboxgl.accessToken,
  mapboxgl: mapboxgl,
  });

map.on("load", function() {
  map.addControl(new mapboxgl.NavigationControl(),'bottom-right');
  map.addControl(new mapboxgl.FullscreenControl(),'bottom-right');
});


document.getElementById('geocoder').appendChild(geocodeWidget.onAdd(map));

mapstyle.addEventListener("change", function(){
    
  map.setStyle('mapbox://styles/mapbox/' + mapstyle.value);

});


console.log(typeof(geocodeWidget));

map.on("zoom", function(){

  zoomLevel.value = map.getZoom();
  
});

function setLocation(){

  var centre = map.getCenter();

  PointField = mapCenter.value;

  var index1 = PointField.indexOf("(");

  var pointString = PointField.substring(0,index1+1);
  
  pointString = pointString + centre.lng + " " + centre.lat + ")";
  
  return pointString;
}

map.on('move', function(){
  mapCenter.value = setLocation();
});

var sidebarOpen = false;
    
function openNav() {

  if (!sidebarOpen){
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("sidebar-btn").innerHTML = "close";
    sidebarOpen = true;
  }
  else{
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("sidebar-btn").innerHTML = "open";
    sidebarOpen = false;
  }
}

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */

function loginDropdown() {
  document.getElementById("loginDropdown").classList.toggle("show");
  console.log('bamn1');
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.loginBtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      if (dropdowns.classList.contains('show')) {
              dropdowns.classList.remove('show');
      }
  }
  console.log('bamn2');
}

function openPanel(evt, panelName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("side-panel-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("side-panel-links");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(panelName).style.display = "block";
  evt.currentTarget.className += " active";
}

function addPoints(pointset, randomColor) {

  var index = pointset.indexOf(",");

  var lat = pointset.substring(1,index);
  var lon = pointset.substring(index+2,pointset.length-1);

  var popup = new mapboxgl.Popup({ offset: 25 }).setHTML(
    '<p><b>Latitude = </b>' + lat + '</p><p><b>Longitude = </b>' + lon + '</p>'
    );

  var marker = new mapboxgl.Marker(
    {color:randomColor}
  ).setLngLat([lon,lat]).setPopup(popup).addTo(map);
  
}

