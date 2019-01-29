

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''






#This code is for creating a new Swordfish Emulated Data Center with n nodes

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
BMCpass='redfish'
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





#part 1: creating the network bridge ----------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def create_network(network_name,ip_range):
    '''
         This function is for creating the network bridge.
		 
    '''
    s="docker network create "+network_name+"  --subnet  "+ip_range         		 
    try:
           (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
           print("Handle shell processes for creating network bridge (use the default network).......")
#----------------------------------------------------------------------------------------------------------------------





#part 2: Displaying network information -------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def display_network_info(network_name):
    '''
         This function is for diisplaying network information.
		 
    '''

    s="docker network inspect "+network_name 
    output=""	 
    try:
           (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
           output=str( output)[2:-3]
            
    except:
           print("It cannot find network information")
           output="It cannot find network information."
    return(output)
#----------------------------------------------------------------------------------------------------------------------		

	


	
#part 3: Display docker information of a container --------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------	
def display_all_one_node_info(network_name,num):
    '''
         This function is for displaying docker information of a container.
		 
    '''


    s="docker container inspect "+network_name+"-sw-node"+str(num)
    if (network_name=="SWEDCnetwork"):
                s="docker container inspect sw-node"+str(num)
    output=""	 
    try:
           (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
           output=str( output)[2:-3]
            
    except:
           print("It cannot find node information")
           output="It cannot find node information."
    return(output)
		
#----------------------------------------------------------------------------------------------------------------------





#part 4: sending a command request for creating a container -----------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------

def createonecontainer(s):
    '''
         This function is for sending a command request for creating a container.
		 
    '''
    try:
        (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("Handle shell processes.......")
		
#----------------------------------------------------------------------------------------------------------------------	





#part 5: creating a container -----------------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def createContainers(n,network_name):
    '''
         This function is for creating a container.
		 
    '''
    print (network_name)
    n=int(n)        
    threads = []
    for i in range(n):
        if (network_name=="SWEDCnetwork"):
                
                s= "docker container run -d -p "+str(5001+i)+":5000 --name sw-node"+str(i+1)+" --network SWEDCnetwork elham1296/sw-from-dockerfile:v2"	
        else:
                s= "docker container run -d -p "+str(5001+i)+":5000 --name "+network_name+"-sw-node"+str(i+1)+" --network "+network_name+" elham1296/sw-from-dockerfile:v2"	
        print(s)
        t = Thread(target=createonecontainer, args=(s,))
        t.daemon = True
        threads.append(t)
        t.start()
    for t in threads:    
          t.join()
    return("done! ")		  
       
#----------------------------------------------------------------------------------------------------------------------	


#initSWEM()
#print(createContainers(5))







