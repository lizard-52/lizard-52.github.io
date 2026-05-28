# /bin/sh

# shut down the server while things are being changed
service apache2 stop

cd /var/www/html

#rm -rf ./*
chmod -R 777 ./*

cp -ru /home/pi/lizard-52.github.io .
ln -s ./lizard-52.github.io/* .
rm -rf ./lizard-52.github.io/.git

find /var/www/html -type f -exec chmod 644 {} \;
find /var/www/html -type d -exec chmod 755 {} \;

service apache2 start