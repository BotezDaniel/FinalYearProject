#To install both softwares, I issued this command:
sudo apt-get install hostapd dnsmasq


#After the installation, this is how I set up dnsmasq:

interface=wlan0         
listen-address=10.0.1.1 
bind-interfaces         
domain-needed           
bogus-priv               
dhcp-range=10.0.1.2,10.0.1.16,9h 


#And then I enabled dnsmasq service to start at boot using this command:
sudo systemctl enable dnsmasq
