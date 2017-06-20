#!usr/bin/python
import os
import time

os.system("tput setaf 5")
print "\t\t\tNetwork task related Terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!**"
print " \t\t\t\t\t\t"
os.system("tput setaf 1")
print"""
Press  1 : To Check The Network Card 
Press  2 : To Check IP Addrress And Configuration Network Interface  
Press  3 : To Check The System Host Name
Press  4 : To Get The DNS Information for Domains
Press  5 : To Reverse Look Up
Press  6 : To Download The File
Press  7 : To Continue a Stopped Download
Press  8 : To Review Network Connection and Open Sockets
Press  9 : To Go To The Main Menu
Press 10 : To Exit
"""
n=raw_input("Press the Key To Perform The Task For Network")
if int(n)==1:    
    os.system("arp -l")
elif int(n)==2:
    os.system("ifconfig")
elif int(n)==3:
    os.system("hostname")
elif int(n)==4:
     i=raw_input("Please Wait..!! Your Request Is Processing ")
     time.sleep(1)
     os.system("dig domain ")
elif int(n)==5:
    os.system("dig x host ")
elif int(n)==6:
    os.system("wget file ")
elif int(n)==7: 
    os.system("wget-c file ")
elif int(n)==8:
    os.system("netstat")
elif int(f)==9:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')     
elif int(f)==10:
	print"Thanks For Using The Service."
	time.sleep(2)
	exit()
else:
	print"Enter The Valid Key"
os.system("tput setaf 0")

