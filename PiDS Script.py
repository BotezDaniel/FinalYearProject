#This code represents the initial version of a network monitoring tool created to analyze incoming network traffic for potential threats. 
#It utilizes Python libraries such as Scapy for packet sniffing and Tkinter for GUI-based notifications. 
#The main functionalities are:
#-Loading the Snort community rules and analyzing incoming packets against these rules.
#-Notifying the user via pop-up messages upon detecting a potentially malicious packet.
#-Logging detected events into a log file for future reference.


from csv import Sniffer
from scapy.all import *
import tkinter as tk
from tkinter import messagebox
import threading
import re
import time
import logging
from logging.handlers import RotatingFileHandler

# Defining the path to the log file directory and the log file itself
log_directory = r'C:\Users\danyk\Desktop\community-rules'
log_file_path = os.path.join(log_directory, "network_monitor.log")

#Checking if the directory exists, creating it if not
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "network_monitor.log")

#Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s\n')

# Creating a file handler for the log file
file_handler = RotatingFileHandler(log_file_path, mode='a', maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Configuring logging format for the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s\n')
file_handler.setFormatter(formatter)

# Adding the file handler to the root logger
logging.getLogger().addHandler(file_handler)

# Global variables for notification throttling
last_notification_time = 0
notification_cooldown = 0  # seconds

# Function to analyze packets against Snort rules
def analyze_packet(packet):
    global last_notification_time

    # Loading Snort rules from a file
    snort_rules = load_snort_rules(r"C:\Users\danyk\Desktop\community-rules\community.rules")
    
    # Checking each rule against the packet
    for rule in snort_rules:
        if match_rule(rule, packet):
            # Throttle notifications
            current_time = time.time()
            if current_time - last_notification_time >= notification_cooldown:
                notify_user("Malicious Packet Detected", f"Snort rule match: {rule}")
                last_notification_time = current_time

                #Log the detected event
                logging.info(f"Malicious packet detected: Snort rule match - {rule}")
            break

# Function to load Snort rules from file
def load_snort_rules(file_path):
    rules = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('#') and line:
                rules.append(line)
    return rules

# Function to match packet against a Snort rule
def match_rule(rule, packet):
    # Example rule format: "alert tcp any any -> any any (content:"malware"; msg:"Malware detected";)"
    match = re.search(r'content:"(.*?)";', rule)
    if match:
        content = match.group(1)
        if content.encode() in bytes(packet):
            return True
    return False

# Function to display pop-up notification
def notify_user(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(title, message)

# Function to start packet sniffing
def start_sniffing():
    sniff(prn=analyze_packet, store=0)

# Start packet sniffing in a separate thread
sniff_thread = threading.Thread(target=start_sniffing)
sniff_thread.start()
