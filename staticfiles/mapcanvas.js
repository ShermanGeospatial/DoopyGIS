      //YOUR TURN: add your Mapbox access token 
      mapboxgl.accessToken = 'pk.eyJ1Ijoic2hlcm1hbmdlb3NwYXRpYWwiLCJhIjoiY2toZHUxa2M3MGcyaTJ6cGNlbTZrMXh6dSJ9.WfocGcVqEoUkeM79FIqHCA';
      
      var mapstyle = document.getElementById("id_style");
      var zoomLevel = document.getElementById("id_zoom");

      var map = new mapboxgl.Map({
        container: 'map', // container id
        style: "mapbox://styles/mapbox/" + mapstyle.value, //YOUR TURN: choose a style: https://docs.mapbox.com/api/maps/#styles
        center: [-122.957093683618, 50.1564046992175], // starting position [lng, lat]
        zoom: zoomLevel.value, // starting zoom
      });

      map.on("load", function() {
        map.addControl(new mapboxgl.NavigationControl(),'bottom-right');
        map.addControl(new mapboxgl.FullscreenControl(),'bottom-right');
        map.addControl(new mapboxgl.GeolocateControl({
          positionOptions: {
            enableHighAccuracy: true
          },
          trackUserLocation: true
        }),'bottom-right');
      });

      var centre = map.getCenter();

      mapstyle.addEventListener("change", function(){
          
        map.setStyle('mapbox://styles/mapbox/' + mapstyle.value);

      });

      zoomLevel.addEventListener("change", function(){

        map.setZoom(zoomLevel.value);
        
      });

      map.on('zoom', function(){
        console.log(map.getZoom());
      });