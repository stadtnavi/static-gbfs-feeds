# Run as: ENV_SOURCE=<path to source .geojson> ENV_DEST=<path to destination folder> python geojsonToStatus.py

import json
import os
from datetime import datetime

sourceFile = os.getenv('ENV_SOURCE')
destFolder = os.getenv('ENV_DEST')

with open(sourceFile) as source:
    source_data = json.load(source)

info = []
status = []

i = 0
for feature in source_data["features"]:
	if 'name_de' in feature['properties']:
		name = feature['properties']['name_de']
	else:
		name = feature['properties']['name']
	info.append({
		"lat": feature["geometry"]["coordinates"][1],
		"lon": feature["geometry"]["coordinates"][0],
		'name': name,
		'station_id': str(i + 1)
	})
	status.append({
		"num_cars_available": 0,
		"is_renting": True,
		'station_id': str(i + 1)
	})
	i += 1

created_info = {
	"data": {
		"stations": info
	},
	"last_updated": int(datetime.timestamp(datetime.now())),
	"ttl": 60000
}
with open(destFolder + "/station_information.json", "w") as dest:
	json.dump(created_info, dest, indent=2)

created_status = {
	"data": {
		"stations": status
	},
	"last_updated": int(datetime.timestamp(datetime.now())),
	"ttl": 60000
}
with open(destFolder + "/station_status.json", "w") as dest:
	json.dump(created_status, dest, indent=2)
