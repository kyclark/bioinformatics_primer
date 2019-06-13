#!/usr/bin/env python -u

import csv
import json
from shapely.geometry import shape, Point 

# load GeoJSON file containing sectors
with open('longhurst.json', 'r') as f:
    js = json.load(f)

with open('lat-lon.tab', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for sample_id,latitude,longitude in reader:
        if not latitude or not longitude:
            continue

        point = Point(float(longitude), float(latitude))

        # check each polygon to see if it contains the point
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                print sample_id, feature['properties']['ProvCode']
