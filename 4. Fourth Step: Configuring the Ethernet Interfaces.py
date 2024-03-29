#In order to create the bridge and use both interfaces, we need some tools. For that, I installed bridge-utils using this command:
sudo apt-get install bridge-utils

#To combine both interfaces, I had to change the /etc/network/interfaces file a bit. This is the end file with all the modifications:

auto lo
iface lo inet loopback


allow-hotplug wlan0
iface wlan0 inet static
address 10.0.1.1
network 10.0.1.0
netmask 255.255.255.0
broadcast 10.0.1.255

auto br0
iface br0 inet dhcp
bridge_ports eth0 eth1
bridge_stp off
bridge_fd 0
bridge_maxwait 0

#After the configuration, I rebooted the Pi so that all the changes apply.
