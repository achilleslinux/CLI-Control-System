#!usr/bin/python
import os
import time

print("\t\t\n\n\n\n")
os.system("tput setaf 1")
print "\t\t\tWelcome to the Some Other Useful Command Line System"
os.system("tput setaf 2")

print "\t\t\t----------------------------------------------------"
print"""
Press 1: To Open The Command Line Calculator
Press 2: To Monitoring The Current System Status
Press 3: To Open The Desk Calculator
Press 4: To Check The Histroy Of All Executing Commands
Press 5: To Display All Processes in Parse Tree
Press 6: To Display The Graphical Representation of System load in The Terminal
Press 7: To Check The Virtual Memory Details
Press 8: To Exit
"""
u=raw_input("Press The Key To Be Execute Commands")
if int(u)==1:
     os.system("bc")
     ch=raw_input("Enter your Choice.. \t[1] To Continue \t2] To Exit : ")
  
    #print ch
   
     if int(ch)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch)==2:
         print "We Will Exit Now"
         time.sleep(1)
    
elif int(u)==2:
     os.system("collectl")
     ch1=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch1
   
     if int(ch1)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch2)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(u)==3:
     os.system("dc")
     ch2=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch2
   
     if int(ch2)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch2)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(u)==4:
     os.system("history")
     ch3=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch3
   
     if int(ch3)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch3)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(u)==5:
     os.system("pstree")
     ch4=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch4
   
     if int(ch4)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch4)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(u)==6:
     os.system("tload")
     ch5=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch5
   
     if int(ch5)==1:
         print "Ok"
         os.system("python uf.py")

     elif int(ch5)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(u)==7:
     os.system("vmstat")
     ch6=raw_input("Enter your Choice.. \t[1] To Continue \t[2] To Exit : ")
  
    #print ch6
   
     if int(ch6)==1:
         print "Ok"
         os.system("python log.py")

     elif int(ch6)==2:
         print "We Will Exit Now"
         time.sleep(1)
elif int(f)==8:
	print"Thanks For Using The Service."
	time.sleep(2)
	exit()
   
else :
	print"Enter The Valid Key For Execute It"
os.system("tput setaf 0")
