# Static GBFS Feeds

A couple of sharing providers currently have no online booking system. To integrate them nevertheless in stadtnavi we mock such a system by static GBFS feeds provided by this project.

## gueltstein-mobil
Gültstein mobil is a local initiative offering a cargobike ("Gülf") for rental in the locality Herrenberg-Gültstein. They provide an online booking system based on commons-booking, which will hopefully in near- to mid-term future will provide a proper GBFS feed on it's own.

## car-sharing
The carsharing feed currently provides all car-sharing stations of stadtmobil Stuttgart.
To update the feed, proceed as follows:

```
$ wget https://stuttgart.stadtmobil.de/media/user_upload/downloads_privatkunden/stuttgart/stadtmobil_Stuttgart_Stationsdaten.csv
$ python3 scripts/csvToStationInfo.py
```
