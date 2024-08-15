#!/usr/bin/env python

import getpass
import sys
import telnetlib

HOST = "Insert IP remote device"
user = raw_input("Enter Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

##Commands to be executed

#Example to create a loopback interface 

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"\conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")



print tn.read_all()
