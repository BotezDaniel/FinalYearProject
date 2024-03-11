#After setting up dnsmasq, I went ahead and configured hostapd:

interface=wlan0
driver=nl80211
ssid=RaspberryPi
hw_mode=g
channel=1
ieee80211n=1
wmm_enabled=1
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_passphrase=dany12345
rsn_pairwise=CCMP 

#And saved the config as /etc/hostapd/hostapd.conf after which I edited the /etc/default/hostapd and deleted the line below and forwarded it to the config file created:
DAEMON_CONF=” /etc/hostapd/hostapd.conf”. 

#When finished, I also set up hostapd to start during boot with this command:
sudo systemctl enable hostapd

