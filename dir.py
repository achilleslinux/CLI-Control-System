#!usr/bin/python

import os
import time

print("\t\t\n\n\n\n")
os.system("tput setaf 3")
print "\t\t\t Directory task related Terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!"
print " \t\t\t\t\t\t"
os.system("tput setaf 0")
print"""
Press  1: To Create a Directory
Press  2: To Change the Home Directory
Press  3: To Show the Current Working Directory
Press  4: To Remove The Directory
Press  5: To List The Directory
Press  6: To Long Listing of root Directory
Press  7: To List of All Hidden Directory
Press  8: To Go to The Root Directory
Press  9: To Change The /etc Directory
Press 10: To Delete The Directory
Press 11: To Move Home Directory Form Anywhere
Press 12: To Change Current Directory To Parent Directory
Press 13: To Go To Main Menu
Press 14: To Exit
"""
d=raw_input("Press The Key To Perform The Task with Diectory :")
if int(d)==1:
   dname=raw_input("Enter your directory name : ")
   os.system("mkdir {0}".format(dname))
   t=raw_input("Please Enter..\t[1] To Continue  \t [2] To Exit ")
   #print t
   if int(t)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t)==2:
	print" \tYour Request Is In Process Please Wait For A While !! "
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==2:
   os.system("cd ")
   t1=raw_input("Please Enter..\t[1] To Continue  \t [2] To Exit ")
   #print t1
   if int(t1)==1:
	print"Your Request Is In Process Please Wait For A While !! "
	time.sleep(2)
	os.system("python dir.py")
   elif int(t1)==2:
	print" \tYour Request Is In Process Please Wait For A While !! !! "
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==3:
   os.system("pwd")
   t2=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t2
   if int(t2)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t2)==2:
	print" \tYour Request Is In Process Please Wait For A While !! "
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==4:
   dname1=raw_input("Enter The Name Of Directory For ReMove: ")
   os.system("rm -rf dir {0}".format(dname1))
   t4=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t4
   if int(t4)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t4)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==5:
   os.system("ls")
   t5=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t5
   if int(t5)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t5)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==6:
   os.system("ls -l")
   t6=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t6
   if int(t6)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t6)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==7:
   os.system("ls -al ~")
   t7=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t7
   if int(t7)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t7)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==8:
   os.system("cd /")
   t8=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t8
   if int(t8)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t8)==2:
	print"\tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==9:
   os.system("cd /etc")
   t9=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t9
   if int(t9)==1:
	print"Your Request Is In Process Please Wait For A While !!!!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t9)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==10:
   dname2=raw_input("Enter The Name of Delete Directory :")
   os.system("rm -r dir".format(dname2))
   t10=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t10
   if int(t10)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t10)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==11:
   os.system("cd ~ ")
   t11=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t11
   if int(t11)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t11)==2:
	print" \tYour Request Is In Process Please Wait For A While !! "
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==12:
   os.system("cd.. ")
   t12=raw_input("Please Enter..\t[1]For Continue  \t [2] For Exit ")
   #print t12
   if int(t12)==1:
	print"Your Request Is In Process Please Wait For A While !!"
	time.sleep(2)
	os.system("python dir.py")
   elif int(t12)==2:
	print" \tYour Request Is In Process Please Wait For A While !!"
	time.sleep(1)
	os.system("exit")
	print"\t\tThanks for Using Service Have A Nice Day !!"
elif int(d)==13:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')
elif int(d)==14:
	print"Your Request Is In Process Please Wait For A While !!"
        time.sleep(3)
	print" Thanks for Having Patience  "
        print"\tThanks For Using Have a Nice Day"
	exit()
else:
	print "Enter The Valid Key "

os.system("tput setaf 0")

