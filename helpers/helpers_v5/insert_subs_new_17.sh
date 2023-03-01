python CSV_JSON_PY_17.py > suburbs.json
mongoimport --drop --username admin --password AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA= --db sheltr --collection suburbs < suburbs.json
