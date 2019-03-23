#!/usr/bin/env python3
import subprocess

interface = input("[+] Enter the interface > \n") #python3:input() python2:raw_input
print("selected interface > "+interface)
mac_addr = input ("[+] Enter the new Mac Address \n")
print("selected Mac Address > "+mac_addr)

subprocess.call("ifconfig "+interface,shell=True)
subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+mac_addr,shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)
subprocess.call("ifconfig",shell=True)
