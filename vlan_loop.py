#!/usr/bin/env python2.7

import getpass
import sys
import telnetlib

HOST = "Remote host IP add"
user = raw_input("Enter Telnet user: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

# This section can be avoided by granting privilege permissions to user in SW/R
tn.write(b"enable\n")
tn.write(b"Enable passw\n")
tn.write(b"\conf t\n")

#variable n needs to be treated as a string as well, otherwise there will be a mismatch

for n in range (2,10):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name VLAN_ " + str(n) + "\n")


tn.write(b"end\n")
tn.write(b"exit\n")



print tn.read_all()
