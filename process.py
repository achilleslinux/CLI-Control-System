#!usr/bin/python

import os
import time

print("\t\t\n\n\n\n")
os.system("tput setaf 4")
print "\t\t\t Process task related Terminal"
os.system("tput setaf 0")
print "\t\t\t!!**!!**!!**!!**!!**!!**!!**!!**!!**!!**!!"
print " \t\t\t\t\t\t"
os.system("tput setaf 0")
print"""
Press 1  : To Display The Currently Working Processes
Press 2  : To Display All The Running Processes
Press 3  : To Kill The Process With Process ID
Press 4  :To Kill ALL The Processes 
Press 5  : To Kill The Process With The Pattern Matchinng
Press 6  : To Stop Background JOBS
Press 7  : To Bring The Most Recent Jobs to Foreground
Press 8  : To Bring A Jobs n To The Foreground
Press 9  : To Go To Main Menu
Press 10 : To Exit
"""
os.system("tput setaf 5")
p=raw_input("Press The Key To Perform Task With Processes : ")
if int(p)==1:
    os.system(" ps ")
    time.sleep(2)
    p1=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p1
    
    if int(p1)==1:
	print"Ok"
        os.system(" python process.py")
    elif int(p1)==2 :
	print "Thank You"
        time.sleep(1)
elif int(p)==2:
    os.system(" top -n")
    time.sleep(2)
    p2=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p2
  
    if int(p2)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p2)==2:
        print "Thank You"       
elif int(p)==3:
    os.system(" kill pid ")
    time.sleep(2)
    p3=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p3
  
    if int(p3)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p3)==2:
        print "Thank You"      
 
elif int(p)==4:
    
    kp=raw_input("Enter The process name that you want to be killed : ")
   
    #print kp
    if int(kp)==1:
        print"Please Wait "
    os.system(" killall")
    time.sleep(2)
    os.system("\t\t")
    p4=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p4
  
    if int(p4)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p4)==2:
        print "Thank You"      
elif int(p)==5:
    os.system(" pkill ")
    p5=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p5
  
    if int(p5)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p5)==2:
        print "Thank You"      
    time.sleep(2)
elif int(p)==6:
    os.system(" bg ")
    time.sleep(2)
    p6=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p6
  
    if int(p6)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p6)==2:
        print "Thank You"      
elif int(p)==7:
    os.system(" fg ")
    time.sleep(2)
    p7=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p7
  
    if int(p7)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p7)==2:
        print "Thank You"      
elif int(p)==8:
    os.system(" fg n")
    time.sleep(2) 
    p8=raw_input("Enter Your Choice [1] To Continue \t\t [2] To Exit..")
    
    #print p8
  
    if int(p8)==1:
        print"Ok"
        os.system("python process.py")
    elif int(p8)==2:
        print "Thank You" 
elif int(p)==9:
	print "We're redirecting you. Please Wait...."
	time.sleep(3)
	os.system('python //root/Desktop/RedhatLinux/option.py')     
elif int(p)==10:
	print"Thanks For Using The Service."
	time.sleep(2)
	exit()
else:  
	print"Enter the valid key to execute it "
os.system("tput setaf 0")
