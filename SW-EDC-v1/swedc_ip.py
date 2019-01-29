

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''



#This code is for getting IP information

import subprocess
import os
import requests
import socket
import ipaddress
import json
import datetime
import random
import time
import threading
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import cs 
import time
import sys
from threading import Thread
from colorama import init
BMCpass=''
from threading import Timer


#part 0: initializing from the command line ---------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------

def initSWEM():
    '''
         This function is for initializing the process from the command line.
		 
    '''
    CHAR_PER_LINE=40
    print("...............................................................................")
    time.sleep(1)
   # print("...............................................................................")
    #time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")	 

    cprint(figlet_format('SW-E-DC ' , font='starwars'),
            'yellow', 'on_blue', attrs=['bold'])
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    #print("...............................................................................")
    #time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    CHAR_PER_LINE=80
    print("\n")
    cprint("IP of  nodes from Swordfish Emulated DataCenter".center(CHAR_PER_LINE-2), 'white','on_blue')
    time.sleep(1)
    print("...............................................................................")
    #time.sleep(1)
    #print("...............................................................................")
    time.sleep(1)  
     	 
#----------------------------------------------------------------------------------------------------------------------



#part 1: finding IP of one containr -----------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def showIPonecontainer(s,i,o,network_name):
    '''
         This function is for finding IP of one containr.
		 
    '''

    out1=""
    out2=""
    out3=""
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
         output=str( output)[2:-3]
         out1="IP of node sw-node"+str(i)+"= "+output
         out2=output
         out3="sw-node"+str(i)
         if(network_name!="SWEDCnetwork"):
                   out1="IP of node "+network_name+"-sw-node"+str(i)+"=  "+output
                   out3=network_name+"-sw-node"+str(i)
    except:
         print("Handle shell processes.......")

    if (o==1 or  o==5 ):	 
       return(out1)
    if (o==2 or o==6):	 
       return(out2)	
    if (o==3 or o==7):	 
       return(out3)	   
			
#----------------------------------------------------------------------------------------------------------------------	

		

#part 2: finding IP of n containrs ------------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------		
def showIPS(n,o,network_name):
    '''
         This function is for finding IP of n containrs.
		 
    '''
    #n=int(input("How many nodes you have in your cluster: "))          
    out1=""

    for i in range(n):
	
        if (network_name=="SWEDCnetwork"):
             s= "docker inspect --format '{{.NetworkSettings.Networks.SWEDCnetwork.IPAddress}}' sw-node"+str(i+1)
        else:
             s= "docker inspect --format '{{.NetworkSettings.Networks."+network_name+".IPAddress}}' "+network_name+"-sw-node"+str(i+1)	
	

        res=showIPonecontainer(s,i+1,o,network_name)
        out1=out1+"\n"+str(res)
		
    return(out1)		
#----------------------------------------------------------------------------------------------------------------------	
      		
 


 
#part 3: finding IP of n containrs. -----------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------	
def showIPone(n,network_name):
    '''
         This function is for finding IP of n containrs.
		 
    '''

    #n=int(input("How many nodes you have in your cluster: "))          
    if (network_name=="SWEDCnetwork"):
        s= "docker inspect --format '{{.NetworkSettings.Networks.SWEDCnetwork.IPAddress}}' sw-node"+str(n)
    else:
        s= "docker inspect --format '{{.NetworkSettings.Networks."+network_name+".IPAddress}}' "+network_name+"-sw-node"+str(n)	


    o=showIPonecontainer(s,n,1, network_name)
	
    return(o)
#----------------------------------------------------------------------------------------------------------------------	
	
#initSWEM()
#showIPS()







