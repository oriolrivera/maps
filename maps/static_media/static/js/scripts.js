$(function(){
     // alert("ok");
     if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getCoords, getError);
     }else{
     	initialize(13.30272, -87.194107);
     }

     function getCoords(position){
     	var lat = position.coords.latitude;
     	var lng = position.coords.longitude;

     	initialize(lat, lng);
     }

     function getError(err){
     	initialize(13.30272, -87.194107);
     }

     function initialize(lat, lng){

     	var latlng = new google.maps.LatLng(lat, lng);
     	var mapSettings = {
     		center: latlng,
     		zoom: 15,
     		mapTypeId: google.maps.MapTypeId.ROADMAP
     	}

     	map = new google.maps.Map($('#mapa').get(0), mapSettings);

     	var marker = new google.maps.Marker({
   			position: latlng,
   			map: map,
   			draggable: true,
   			title: 'Arrastrame :)'
     	});

     	google.maps.event.addListener(marker, 'position_changed', function(){
     		getMarkerCoords(marker);
     	});

     }//end initialize

     function getMarkerCoords(marker){
     	var markerCoords = marker.getPosition();
     	//console.log(markerCoords.lat()+' '+markerCoords.lng());
     	$('#id_lat').val(markerCoords.lat() );
     	$('#id_lng').val(markerCoords.lng() );
     }

});