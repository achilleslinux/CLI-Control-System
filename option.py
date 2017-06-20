#!usr/bin/python

import time
import os
print("\t\t\t\t\n\n\n")
os.system("tput setaf 1")
print"\t\t\tWelcome To  Linux  System Terminal"
print"\t\t\t*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"

print "\t\t\t\t\t\t\t\t"
os.system("tput setaf 0")

print("\t\t\t\n")
print"""
Press  1: To Perform Commands Related To Login User
Press  2: To Perform Commands Related To File
Press  3: To Perform Commands Related To Directory
Press  4: To Perform Commands Related To Process Management
Press  5: To Perform Commands Related To System Information
Press  6: To Perform Commands Related To Networking 
Press  7: To Perform Commands Related To Partition
Press  8: To Perform Commands Related To Usefull command keyword
Press  9: To View Servers
Press 10: Recommended- DEVELOPERS only!!!
Press 11: To exit the system
"""
os.system("tput setaf 5")
f=raw_input("Press any key to perform tasks : ")
if int(f)==1:
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/log.py')
elif int(f)==2:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/file.py')
elif int(f)==3:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/dir.py')
elif int(f)==4:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/process.py')
elif int(f)==5:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/sys.py')

elif int(f)==6:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/network.py')
elif int(f)==7:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/partition.py')
elif int(f)==8:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/uf.py')
elif int(f)==9:
	print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\n")
        time.sleep(2)
        os.system('python //root/Desktop/RedhatLinux/servers/options.py')
elif int(f)==10:
        os.system("gnome-terminal")
elif int(f)==11:
	print("See you soon. Have a nice day!!!")
	time.sleep(3)
	exit()
else:
    
	print "You've entered an invalid key. Please press a valid key"

os.system("tput setaf 0")







