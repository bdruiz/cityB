def generateMap(dtst_bicitaxis,polygon,ubicacionAsociacion):

	import system
	
	marker=	""
	popup=""
	i=0	
	
	pds = system.dataset.toPyDataSet(dtst_bicitaxis)
	for row in pds:
		i=i+1	
		marker+=""" var marker"""+str(i)+""" = L.marker([""" + str(row["LATITUD"]) + ""","""+ str(row["LONGITUD"]) + """], {icon: greenIcon}).addTo(mymap);"""
		popup+="""marker"""+str(i)+""".bindPopup(" <b>Bicitaxi """ +  row["Nombre Bicitaxi"] + """ </b><br>""" + row["Asociacion"] +""" <br>""" + str( row["velocidad"]) +""" km/h   ").openPopup(); """
			
		
	
	
		
	html1 = """<html>
		<head>
			<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin=""/>
			<!-- Make sure you put this AFTER Leaflet's CSS -->
			<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"    integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="    crossorigin="">
			
			

			
			</script>
	   
		</head>
		
		
	 
	
		<body>
				<div style="width: 800px; height: 600px;" id="mapid"></div>
				<script>
				
				  
				
					
					var greenIcon = L.icon({
				    iconUrl: 'https://static.wixstatic.com/media/0e0278_f810356ec9aa4f2c8d53a37295f2acc3~mv2.png/v1/fill/w_38,h_39/bicitaxi.png',
				    shadowUrl: 'https://static.wixstatic.com/media/0e0278_24301ee9a130486d9c3ba56535bf1880~mv2.png/v1/fill/w_70,h_46/bicitaxi%20sombra.png',
				
				    iconSize:     [38, 39], // size of the icon
				    shadowSize:   [50, 46], // size of the shadow
				    iconAnchor:   [22, 50], // point of the icon which will correspond to marker's location
				    shadowAnchor: [13, 55],  // the same for the shadow
				    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
				});
					
					
														
					var mymap = L.map('mapid').setView(["""
					
					
	html1a=				"""], 16);
	
					L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', 
						{
							maxZoom: 18,attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
							'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
							'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',id: 'mapbox/streets-v11'
						}
							).addTo(mymap);
							
					
					
					
					"""
					
	
	html2= """
					
					
					
					
					var popup = L.popup();
								
								function onMapClick(e) {
								    popup
								        .setLatLng(e.latlng)
								        .setContent("Esta posición es: " + e.latlng.toString())
								        .openOn(mymap);
								}
					mymap.on('click', onMapClick);
					
					/*var circle = L.circle([4.6405356,-74.1038277], {
							color: 'red',
							fillColor: '#f03',
							fillOpacity: 0.5,
							radius: 500
							}).addTo(mymap);
					*/		
					var polygon = L.polygon(["""
	
	html3= """]).addTo(mymap);
	
	</script>
		</body>
	</html>
		  """
	html=html1+ubicacionAsociacion+html1a+marker+popup+html2+polygon+html3
#	data = system.dataset.toPyDataSet(system.tag.read("[Client]Locations").value)
#	for row in data:
#		html += "addMarker(map, '%s', '%s', '%s', %s, %s);\n" % (row["title"], row["description"], row["location"], row["lat"], row["lon"])
	  
#	html += """}
	
#	google.maps.event.addDomListener(window, 'load', initialize);
	
#		</script>
#	  </head>
#	  <body>
#		<div id="map-canvas"></div>
#	  </body>
#	</html>"""
	
	return html