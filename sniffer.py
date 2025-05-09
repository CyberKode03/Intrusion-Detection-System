import pyshark
import threading

sniffing = True

# Define packet handler
def packet_callback(packet):
    # You can write packets to a file or forward to Snort via PCAP log
    with open("packets.log", "a") as f:
        f.write(str(packet) + "\n")

# Sniffing function
def start_sniffing():
    global sniffing
    sniffing = True
    # Use Pyshark for sniffing
    capture = pyshark.LiveCapture(interface='eth0')  # Adjust interface as needed
    capture.sniff(timeout=50)  # Capture packets for 50 seconds or adjust as needed
    for packet in capture:
        packet_callback(packet)

def stop_sniffing():
    global sniffing
    sniffing = False
