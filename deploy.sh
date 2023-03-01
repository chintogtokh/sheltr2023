cd /srv/sheltr
git checkout master
git pull
cd /srv/sheltr/frontend
npm run build
cd /srv/sheltr/backend
npm run build
chown -R ubuntu:ubuntu /srv/sheltr
service node-6000 restart
service nginx restart

