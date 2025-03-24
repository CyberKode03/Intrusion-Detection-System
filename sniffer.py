# intrusion_detection_system/sniffer.py

from scapy.all import sniff
import threading
import time

sniffing = True

# Define packet handler
def packet_callback(packet):
    # You can write packets to a file or forward to Snort via PCAP log
    with open("packets.log", "a") as f:
        f.write(str(packet.summary()) + "\n")

# Sniffing function
def start_sniffing():
    global sniffing
    sniffing = True
    sniff(prn=packet_callback, store=0, stop_filter=lambda x: not sniffing)

def stop_sniffing():
    global sniffing
    sniffing = False
