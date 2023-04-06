import simplekml
import re
import pandas as pd

df = pd.read_excel('csv_to_kml.xlsx', sheet_name='csv_to_kml')
kml = simplekml.Kml()
for index, row in df.iterrows():
    address = row[0]
    address = address[7:]
    coordinates = row[1]
    longitude = coordinates.split(',')[0]
    longitude = longitude.replace(" ", "")
    latitude = coordinates.split(',')[1]
    latitude = latitude.replace(" ", "")
    description = row[2]    
    point = kml.newpoint(name=address, coords=[(latitude, longitude)])
    point.description = description
    point.style.iconstyle.icon.href = 'https://mt.googleapis.com/vt/icon/name=icons/onion/SHARED-mymaps-container-bg_4x.png,icons/onion/SHARED-mymaps-container_4x.png,icons/onion/1603-house_4x.png'

kml.save("import.kml")