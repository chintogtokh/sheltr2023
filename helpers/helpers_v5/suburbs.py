import csv
import json
import random
import re
import os

with open('./victoria_simplified.json', 'r') as json_file:
    json_data = json.loads(json_file.read())
    for sub in json_data['features']:
        name = sub['properties']['vic_loca_2']
        if name == "EAST BAIRNSDALE":
            name = "BAIRNSDALE EAST"
        if name == "BALLARAT CENTRAL":
            name = "BALLARAT"
        f = open('data/geojson/' + name + "_xaaaa.geojson", "w+")
        f.write(json.dumps(sub))
        f.close()
    