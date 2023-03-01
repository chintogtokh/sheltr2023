set -e

mongoimport --drop --legacy --db sheltr --collection suburbs --type json --file /docker-entrypoint-initdb.d/suburbs.json

mongoimport --drop --legacy --db sheltr --collection universities --type json --file /docker-entrypoint-initdb.d/uni_for_mongo.txt