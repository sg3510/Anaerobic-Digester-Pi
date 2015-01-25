# Anaerobic-Digester-Pi
Anaerobic Digester Raspberry Pi Code - Used to control 18 tanks 

## Config
### Raspberry Pi config
Install virtualenv
```bash
# Update Packages and install python
sudo apt-get update
sudo apt-get install -y python-dev
# Get the pip package manager
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
# Setup and configure a virtual environment to install all packages for our scripts
sudo pip install virtualenv
mkdir ~/venv
cd ~/venv
virtualenv anaeropi
```

### Server/Master Pi Config
We have opted to use RabbitMQ as messaging service to get all Pis to talk together. For this we need to install it by doing:
```bash
sudo nano /etc/apt/sources.list
```
Once inside the nano editor, add ```deb http://www.rabbitmq.com/debian/ testing main``` as a seperate line. Ctrl+X can be used to exit (press Y to confirm and save changes).

Then install the key and install RabbitMQ

```bash
sudo wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
# File no longer needed so we can delete
rm rabbitmq-signing-key-public.asc
sudo apt-get update
# Install rabbitmq with all its needed dependencies
sudo apt-get install rabbitmq-server
# For debug purposes we enable the web plugin
sudo rabbitmq-plugins enable rabbitmq_management
# Create a user that can access rabbitmq
sudo rabbitmqctl add_user anaeropi D1g3sting!
sudo rabbitmqctl set_user_tags anaeropi administrator
sudo rabbitmqctl set_permissions -p / anaeropi “.*” “.*” “.*”
```
This creates a user with name ```anaeropi``` and password ```D1g3sting!``` capable of identifying itself to the messaging system.

## SD Card setup
To setup an SD card for the pi we just head to

http://www.raspberrypi.org/downloads/

and get the latest version of raspbian.

The official guide however doesn't list the best way to copy the image to the SD card (speedwise), to improve times 10x use this command instead" 
```
sudo dd if=[raspbian image file].img of=/dev/rdisk# bs=1m
```
