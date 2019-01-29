

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''



#This code is for expanding the cluster

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
from threading import Thread
from colorama import init	   
BMCpass=''
from threading import Timer


#part 0: initializing--------------------------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------

def initSWEM():
    '''
         This function is for expanding the cluster from the command line.
		 
    '''
    CHAR_PER_LINE=40
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")	 

    cprint(figlet_format('SW-E-DC ' , font='starwars'),
            'yellow', 'on_blue', attrs=['bold'])
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    CHAR_PER_LINE=80
    print("\n")
    cprint("Welcome to Swordfish Emulated DataCenter".center(CHAR_PER_LINE-2), 'white','on_blue')
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)
    print("...............................................................................")
    time.sleep(1)  
     	 
#----------------------------------------------------------------------------------------------------------------------





#part 1: Creating one container ---------------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def createonecontainer(s):
    '''
         This function is for creating one container.
		 
    '''
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("Handle shell processes.......")
			
	
#----------------------------------------------------------------------------------------------------------------------	





#part 2: Creating a requested number of nodes -------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def createContainers(n1,n2,n3,network_name):
    '''
         This function is for creating a requested number of nodes.
		 
    '''
   # n=int(input("How many nodes you need in your cluster: "))   
       
    threads = []
    for i in range(n2):
        if (network_name=="SWEDCnetwork"):
                    s= "docker container run -d -p "+str(5001+i+n1+n3)+":5000 --name sw-node"+str(i+n1+1+n3)+" --network SWEDCnetwork elham1296/sw-from-dockerfile:v3"	
        else:
                    s= "docker container run -d -p "+str(5001+i+n1+n3)+":5000 --name "+network_name+"-sw-node"+str(i+n1+1+n3)+" --network "+network_name+" elham1296/sw-from-dockerfile:v3"	       
        t = Thread(target=createonecontainer, args=(s,))
        threads.append(t)
        t.start()
    for t in threads:    
          t.join()     
 #----------------------------------------------------------------------------------------------------------------------	      
		

#initSWEM()
#createContainers()






