from scapy.all import *
import sys
import os
from colorama import Fore,Style
import math

def http_callback(Packet):
    if Packet['TCP'].payload:
        if Packet['IP'].dport == 80:
            pack = str(bytes(Packet['TCP'].payload))
            if pack[:4] == 'POST':
                print Packet['TCP'].payload
                
sniff(prn=http_callback, filter="tcp")
