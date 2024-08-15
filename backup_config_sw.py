import getpass
import telnetlib


#If credentials were different for each switch, then they would go inside the loop
user = raw_input("Enter Telnet user: ")
password = getpass.getpass()

#Opens a file that stores IP add
f = open("myhosts")

for line in myhosts:
        print "Getting running config from device " + (line)
        #strip removes any hidden space
        HOST = line.strip()
        tn = telnetlib.Telnet(HOST)

        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")

        #This command tells the SW to show all the config without having to press space bar
        tn.write(b"terimnal lenght 0\n")
        tn.write("show running config"\n")
        tn.write(b"exit\n")

        #Store config
        readconfig = tn.read_all()
        saveconfig = open("switch" + HOST, "w")
        saveconfig.write(readconfig)
        saveconfig.close
