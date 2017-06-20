#!usr/bin/python

import commands
import os
import time
print("\t\t\n\n\n\n")
os.system("tput setaf 2")
print "\t\t\t File tasks related terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!"
print " \t\t\t\t\t\t"
os.system("tput setaf 0")
print"""
Press  1 : To Create a File
Press  2 : To Check The Inode Number of File
Press  3 : To Check The Size Of File In Human Readable Format
Press  4 : To See The Hidden Files
Press  5 : To See The output Contents of File
Press  6 : To Check the Output of first 10 Lines
Press  7 : To Check the Output of Last 10 Lines
Press  8 : To Update A file Contents
Press  9 : To Delete A file
Press 10 : To Delete A File Fastly
Press 11 : To Copy A file Contents
Press 12 : To Move A File From One Place To Another Place
Press 13 : To Go To Main Menu
Press 14 : To Exit 
"""
f=raw_input("Press The Button To Perform A Task With File : ")
if int(f)==1:
   fname=raw_input("enter your file name : ")
   os.system("touch {0}".format(fname))
   ch=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch
   
   if int(ch)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch)==2:
        print "We Will Proceed"
        time.sleep(1)
   
   
elif int(f)==2:
   os.system("ls -i")
   ch1=raw_input("Enter your Choice  [1] To Continue it \t\t[2] To exit : ")
  
  #print ch1
   
   if int(ch1)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch1)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==3:
   os.system("ls -lh")
   ch2=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch2
   
   if int(ch2)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch2)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==4:
   os.system("ls -al")
   ch3=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch3
   
   if int(ch3)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch3)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==5:
   fname11=raw_input("Enter the name of file for output contents file :")
   os.system("more {0}".format(fname11))
   ch5=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch5
   
   if int(ch5)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch5)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==6:
   fname10=raw_input("Enter the files name for shown first 10 lines : ")
   os.system("head {0}".format(fname10))
   ch6=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch6
   
   if int(ch6)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch6)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==7:
   fname8=raw_input("Enter the files name for shown last 10 output:")
   os.system("tail {0}".format(fname8))
   ch7=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch7
   
   if int(ch7)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch7)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==8:
   fname0=raw_input("Enter the file thats you want to be update:")
   os.system("gedit {0}".format(fname0))
   ch8=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch8
   
   if int(ch8)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch8)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==9:
   fname=raw_input("Enter The Exitsing File Name For Delete")
   os.system("rm -rvf {0}".format(fname))
   ch9=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch9
   
   if int(ch9)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch9)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==10:
   fname4=raw_input("Enter The File Name That's you want to be Remove Fastly : ")
   os.system("rm -rf {0}".format(fname4))
   ch10=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch10
   
   if int(ch10)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch12)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==11:
   x=raw_input("Enter the file name you want to crete\t")
   print "You have entered the name as \t %s" %(x)
   os.system("touch " + x)
   print " All right we've created a file."
   y=raw_input("Enter the name of file to be copied\t")
   print "You have entered the following data \t %s" %(y)
   os.system("cp %s /home/Desktop/Project/" %(y))
  
  #print ch11
   
   if int(ch11)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch11)==2:
        print "We Will Proceed"
        time.sleep(1)
   
elif int(f)==12:
   fname6=raw_input("Enter The Name Of File To Be Want To Move :")
   os.system("mv file file {0 0}".format(fname6))
   ch12=raw_input("Enter your Choice  [1] To Continue \t\t[2] To exit : ")
  
  #print ch12
   
   if int(ch12)==1:
        print "Ok"
        os.system("python file.py")

   elif int(ch12)==2:
        print "We Will Proceed"
        time.sleep(1)
elif int(f)==13:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')
  
elif int(f)==14: 
      print"We Will Proceed"
      time.sleep(2)
      os.system("Thanks for using Have a nice Day !!")
      exit()
else :


	print"Not Supported"


raw_input("Enter To close it .. ")
os.system("tput setaf 6")
time.sleep(2)
print("\t\tThank you for using Have a Nice Day")
os.system("tput setaf 0")
exit()

