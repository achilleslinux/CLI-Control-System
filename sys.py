#!usr/bin/python

import os
import time
print("\t\t\n\n\n\n")
os.system("tput setaf 6")
print "\t\t\t System task related Terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!"
print " \t\t\t\t\t\t"
os.system("tput setaf 0")
print"""
Press  1 : To Check The Login Name
Press  2:  To Check The List Of User To Currrently Logged IN 
Press  3 : To Check Today's Date
Press  4 : To Check the Persent Time
Press  5 : To Check the month 's CALENDER
Press  6 : To Check The kernel Information
Press  7 : To Check The CPU Information
Press  8 : To Open The Manual
Press  9 : To Check The Disk Usage
Press 10 : To Check The Directory Space Usage 
Press 11 : To Show The Free Space
Press 12 : To Go To Main Menu
Press 13 : To Exit
"""
f=raw_input("Press The Button To Be Perform The Task With File : ")
if int(f)==1:
     os.system(" whoami")
     ch=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch
   
     if int(ch)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==2:
     os.system(" who ")
     ch1=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch1
   
     if int(ch1)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch1)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==3:
     os.system(" date ")
     ch2=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch2
   
     if int(ch2)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch2)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==4:
     os.system("uptime")
     ch3=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch3
   
     if int(ch3)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch3)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==5:
     os.system("cal")
     ch4=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch4
   
     if int(ch4)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch4)==2:
         print "We Will Exit Now"
         time.sleep(1)

elif int(f)==6:
     os.system("uname -a ")
     ch6=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch6
   
     if int(ch6)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch6)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==7:
     CPU=raw_input("Enter The Keyword for get Info About the CPU: ")
     os.system("cat /proc/cpuinfo {0}".format(CPU))
     ch7=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch7
   
     if int(ch7)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch7)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==8:
     manual=raw_input("Enter the Key word for looking in Manual : ")
     os.system("man {0}".format(manual))
       
 
     ch9=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch9
   
     if int(ch9)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch9)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==9:
     os.system("df" )
     ch10=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch10
   
     if int(ch10)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch10)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==10:
     os.system("du")
     ch11=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch11
   
     if int(ch11)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch11)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==11:
     os.system("free")
     ch12=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch12
   
     if int(ch12)==1:
         print "Ok"
         os.system("python sys.py")

     elif int(ch12)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==12:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')     
elif int(f)==13:
	print"Thanks For Using The Service."
	time.sleep(2)
	exit()
else:
    print "Enter the valid key"

os.system("tput setaf 0")
