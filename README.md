# Anaerobic-Digester-Pi
Anaerobic Digester Raspberry Pi Code - Used to control 18 tanks 

## Config
### Raspberry Pi config
Install virtualenv
```bash
# Update Packages and install python
sudo apt-get update
sudo apt-get install python-dev
# Get the pip package manager
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
# Setup and configure a virtual environment to install all packages for our scripts
sudo pip install virtualenv
mkdir ~/venv
cd ~/venv
virtualenv anaeropi
```
