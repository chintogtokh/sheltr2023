python CSV_TO_JSON_TO_MONGO_PYTHON_13_05_2018.py > suburbs.json
mongoimport --drop --username admin --password AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA= --db sheltr --collection suburbs < suburbs.json
