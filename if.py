#!/usr/bin/python2
import time,commands,webbrowser
option='''
press 1 to check internet cable on your machine
press 2 to check internet access on your machine
press 3 to check google access 
press 4 to check your os 
'''
print option

choice =raw_input("enter any number")
if choice =="1":
	print "plz wait internet cable being checked.."
	time.sleep(2)
	
	x=commands.getoutput('mii-tool eno1')
	if 'link ok' in x:
		print "the cable is connected"
	else:
		print "cable is not connected"
	
	
elif choice =="2":
	print "plz wait internet accese being checked"
	time.sleep(2)
	y=commands.getoutput('ping 8.8.8.8 -c 4')
	if 'PING' in y:
		print "internet connectivity is successful"
	else :
		print "internet connectivity is not successful"
		
elif choice =="3":
	print "plz wait google accessibility being checked"
	time.sleep(2)
	webbrowser.open_new_tab("https://www.google.com")
elif choice =="4":
	m=commands.getoutput('cat /etc/os-release')
	print "your os is :"+m
	
else:
	print "wrong choice"	
