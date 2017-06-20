#!/bin/usr/python2

import os
import time
import getpass

os.system("tput setaf 1")
print"\t\t\tWelcome To Command Line Terminal "
os.system("tput setaf 0")
print"\t\t\t!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"
os.system("tput setaf 2")
while True:
	print  "Enter  user name : " 
	os.system("tput setf 2") 
	u=raw_input()
	os.system("tput setaf 4")
	print  "Enter  password  :  "
	os.system("tput setaf 4")
	p=getpass.getpass("")

	if  u ==  'root' and  p == 'redhat' :
		os.system('python /root/Desktop/RedhatLinux/success.py')


	else :
		print  "Invalid  user or password"

os.system("tput setaf 0")




