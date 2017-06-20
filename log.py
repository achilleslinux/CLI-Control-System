#!usr/bin/python

import os
import time
print("\t\t\t\n\n\n\n")
os.system("tput setaf 1")
print"\t\t\tLogin tasks related terminal"
print"\t\t\t*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"

print "\t\t\t\t\t\t\t\t"
os.system("tput setaf 0")


print"""
Press  1 : To Check The Current Login Name
Press  2 : To Change The Password of a User
Press  3:  To Display The User with Unique ID
Press  4 : To Add a Group In System
Press  5 : To Check The Last Login User Information
Press  6 : To Reboot The system
Press  7 : To Check The Currently Logged In User
Press  8 : To Add The User 
Press  9 : To Delete The User
Press 10 : To Go To Previous Menu
"""
u=raw_input("Enter The Key To Perform The Task Related To Login: ")
if int(u)==1:
     os.system("whoami")
     os.system("tput setaf 10")
     ch=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To  exit : ")
  
    #print ch
   
     if int(ch)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==2:
     upasswd=raw_input("Enter Name Of User For Change Password : ")
     os.system("passwd {0}".format(upasswd))
     os.system("tput setaf 10")
     ch1=raw_input("Enter your Choice.. \t [1] To Continue \t[2] To exit : ")
  
    #print ch1
   
     if int(ch1)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch1)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
     
elif int(u)==3:
     os.system("id")
elif int(u)==4:
     groupadd=raw_input("Enter Your Name Of Group : ")
     os.system("groupadd {0}".format(groupadd))
     os.system("tput setaf 10")
     ch2=raw_input("Enter your Choice.. \t [1] To Continue \t[2] To exit : ")
  
    #print ch2
   
     if int(ch2)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch2)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==5:
     os.system("lastlog ")
     os.system("tput setaf 10")
     ch3=raw_input("Enter your Choice.. \t [1] To Continue \t[2] To exit : ")
  
    #print ch3
   
     if int(ch3)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch3)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==6:
     os.system("reboot")
elif int(u)==7:
     os.system("who -uH")
     os.system("tput setaf 10")
     ch5=raw_input("Enter your Choice \t [1] To Continue \t[2] To exit : ")
  
    #print ch5
   
     if int(ch5)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch5)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==8:
     usadd=raw_input("Enter Your User Name : ")
     os.system("useradd {0}".format(usadd))
     os.system("tput setaf 10")
     ch6=raw_input("Enter your Choice.. \t [1] To Continue \t[2] To exit : ")
  
    #print ch6
   
     if int(ch6)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch6)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==9: 
     usdel=raw_input("Enter the Name of User For Delete : ")
     os.system("userdel -f {0}".format(usdel))
     os.system("tput setaf 10")
     ch7=raw_input("Enter your Choice.. \t [1] To Continue \t[2] To exit : ")
  
    #print ch7
   
     if int(ch7)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch7)==2:
         print "We will exit now. See you soon"
         time.sleep(1)
elif int(u)==10:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')
	

else:
	print"Enter The Valid Key"
os.system("tput setaf 0")


