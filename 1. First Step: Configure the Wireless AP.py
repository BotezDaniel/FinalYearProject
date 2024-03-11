#After setting up the OS for the Raspberry Pi, I configured the Wireless AP


iface wlan0 inet static
address 10.0.1.1
network 10.0.1.0
netmask 255.255.255.0
broadcast 10.0.1.255

#reboot the pi at after configuring this, in order to apply the changes
