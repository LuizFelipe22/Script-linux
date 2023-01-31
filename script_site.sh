#!bin/bash

sudo apt install apache2 -y
sudo apt install unzip -y

sudo cd /tmp
sudo wget https://github.com/LuizFelipe22/site-barbearia-com-HTML-e-CSS/archive/refs/heads/main.zip 
sudo unzip main.zip
sudo cd site-barbearia-com-HTML-e-CSS-main
sudo cp -R * /var/www/html

echo "Site já estar em execução no servidor"


