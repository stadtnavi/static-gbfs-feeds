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
	if "address_en" in feature["properties"] and "Capacity" in feature["properties"]["address_en"]:
		capacity = int(feature["properties"]["address_en"].split("Capacity: ")[1].split(",")[0])
	else:
		capacity = 0

	stations.append({
		"is_renting": "true",
		"num_cars_available": capacity,
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
