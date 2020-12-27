document.addEventListener('DOMContentLoaded', function () {
  var form = document.querySelector('#upload_features'),
      btn = document.querySelector('.button'),
      loader = document.querySelector('.loader'),
      check = document.querySelector('.check');
  
  form.addEventListener('submit', function () {
    loader.classList.add('computing');    
  });
 
  loader.addEventListener('animationend', function() {
    check.classList.add('computing'); 
  });
});

function initMap() {
  const myLatlng = { lat: 51.5423, lng: -0.1285 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: myLatlng,
  });
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click the map to get Lat/Lng!",
    position: myLatlng,
  });
  infoWindow.open(map);
  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    var lat = mapsMouseEvent.latLng.lat();
    var lng = mapsMouseEvent.latLng.lng();
    if (lat < 51.45 || lat > 51.60 || lng < -0.28 || lng > 0.12) {
      alert("Wrong coordinates, please use some coordinates inside London");
      return;
    }
    document.getElementById("latitude").value = lat;
    document.getElementById("longitude").value = lng;
    // Close the current InfoWindow.
    infoWindow.close();
    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
      JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    );
    infoWindow.open(map);
  });
}
