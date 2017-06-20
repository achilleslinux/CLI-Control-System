#!usr/bin/python

import os
import time

print("\t\t\n\n\n\n")
os.system("tput setaf 3")
print "\t\t\t Partition task related Terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!"
print " \t\t\t\t\t\t"
os.system("tput setaf 0")
print"""
Press 1 : To Check The List Of Current Partition
Press 2 : To Create A Partition
Press 3 : To Show The Partition List
Press 4 : To Be Mount The Partition
Press 5 : To Be Take  a Backup Of File System
Press 6 : To Reboot The System
Press 7 : To Check The List of Part For Delete
Press 8 : To Delete The Partition
Press 9 : To save a done Process
Press 10: To Go To Main Menu
Press 11: To Exit
"""
p=raw_input("Follow This To be di it")
if int(p)==1:
   print"Enter C to Check The Current Partiton in Disk"
   os.system("fdisk -l")
elif int(p)==2:
   print"Enter P for Partition : "
   os.system("fdisk /dev/sda")
   time.sleep(2)
elif int(p)==3:
   os.system("fdisk -l")
elif int(p)==4:
   print"Enter M for Mounting "
   os.system("mkdir /test | mount /dev/sda3 /test | ls -a /test")
elif int(p)==5:
   os.system("cp /etc/fstab /etc/fstab.bk | vi /etc/fstab")
elif int(p)==6:
   os.system("reboot")
elif int(p)==7:
   print"Press Enter to Start The Delete Partition"
   os.system("fdisk /dev/sda")
elif  int(p)==8:
   os.system("fdisk /dev/sda")
   time.sleep(2)
elif int(p)==9:
   os.system("w")
elif int(p)==10:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')     
elif int(p)==11:
	print"Thanks For Using The Service."
	time.sleep(2)
	exit()
else :
	 print"Enter The Valid key"
