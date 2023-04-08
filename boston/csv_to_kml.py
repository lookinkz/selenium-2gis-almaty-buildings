import simplekml
import re
import pandas as pd

df = pd.read_excel('csv_to_kml.xlsx', sheet_name='csv_to_kml')
kml = simplekml.Kml()
for index, row in df.iterrows():
    address = row[0]
    coordinates = row[1]
    longitude = coordinates.split(',')[0]
    longitude = longitude.replace(" ", "")
    latitude = coordinates.split(',')[1]
    latitude = latitude.replace(" ", "")
    description = row[2]
    point = kml.newpoint(name=address, coords=[(latitude, longitude)])
    point.description = description
    print(address, '\n', coordinates, '\n', description)
    print('\n\n')

kml.save("import.kml")
