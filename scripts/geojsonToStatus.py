# Run as: ENV_SOURCE=<path to source .geojson> ENV_DEST=<path to destination .json> python geojsonToStatus.py

import json
import os
from datetime import datetime

sourceFile = os.getenv('ENV_SOURCE')
destFile = os.getenv('ENV_DEST')

with open(sourceFile) as source:
    source_data = json.load(source)

stations = []

i = 0
for feature in source_data["features"]:
	if 'name_de' in feature['properties']:
		name = feature['properties']['name_de']
	else:
		name = feature['properties']['name']
	stations.append({
		"lat": feature["geometry"]["coordinates"][1],
		"lon": feature["geometry"]["coordinates"][0],
		'name': name,
		'station_id': str(i + 1)
	})
	i += 1

created_data = {
	"data": {
		"stations": stations
	},
	"last_updated": int(datetime.timestamp(datetime.now())),
	"ttl": 60000
}

with open(destFile, "w") as dest:
	json.dump(created_data, dest, indent=2)
