#!/usr/bin/env python2.7

import getpass
import sys
import telnetlib

#If credentials were different for each switch, then they would go inside the loop
user = raw_input("Enter Telnet user: ")
password = getpass.getpass()

#IP addresses need to be contiguous and the range manually specified. In this example it goes from 192.169.122.100 to 192.1>

for n in range (100,150):
        HOST = "192.168.122." + str(n)
        tn = telnetlib.Telnet(HOST)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"\conf t\n")


        for n in range (2,10):
                tn.write("vlan " + str(n) + "\n")
                tn.write("name Python_VLAN_ " + str(n) + "\n")


tn.write(b"end\n")
tn.write(b"exit\n")
