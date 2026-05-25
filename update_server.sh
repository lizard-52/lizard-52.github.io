# /bin/sh

# shut down the server while things are being changed
service apache2 stop

cd /var/www/html

rm -rf ./*

sudo cp -r /home/pi/lizard-52.github.io .
ln -s ./lizard-52.github.io/* .
rm -rf ./lizard-52.github.io/.git

sudo find /var/www/html -type f -exec chmod 644 {} \;
sudo find /var/www/html -type d -exec chmod 755 {} \;

service apache2 start