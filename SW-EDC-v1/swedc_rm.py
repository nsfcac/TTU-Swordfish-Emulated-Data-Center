

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''




#This code is for removing "Swordfish Emulated Data Center" : Nodes, and network Bridges.

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
power=[]


#part 0: initializing the process from command line -------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def initSWEM():
    '''
         This function is for initializing the process from command line.
		 
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
    cprint("Remove nodes from Swordfish Emulated DataCenter".center(CHAR_PER_LINE-2), 'white','on_blue')
    time.sleep(1)
    print("...............................................................................")
    #time.sleep(1)
    #print("...............................................................................")
    time.sleep(1)       	 
#----------------------------------------------------------------------------------------------------------------------





#part 1: sending the command line request -----------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def rmonecontainer(s):
    '''
         This function is for sending the command line request.
		 
    '''
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("Handle shell processes.......")
			
#----------------------------------------------------------------------------------------------------------------------	





#part 2: removing all the containers in the network -------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def rmContainers(n,network_name):
    '''
         This function is for removing all the containers in the network.
		 
    '''
    #n=int(input("How many nodes you have in your cluster: "))
          

    for i in range(n):

        if (network_name=="SWEDCnetwork"):
                                   s= "docker container rm  -f sw-node"+str(i+1)
        else:
                                   s= "docker container rm  -f "+network_name+"-sw-node"+str(i+1)

        rmonecontainer(s)		
#----------------------------------------------------------------------------------------------------------------------	





#part 3: remove one container -----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------		
def rm_Container_by_number(n, network_name):
    '''
         This function is for removing one container.
		 
    '''

    if (network_name=="SWEDCnetwork"):
                                   s= "docker container rm  -f sw-node"+str(n)
    else:
                                   s= "docker container rm  -f "+network_name+"-sw-node"+str(n) 
    rmonecontainer(s)
				
#----------------------------------------------------------------------------------------------------------------------	





#part 4: remove all the containers in the host OS ---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------		
def rm_Container_fast():
    '''
         This function is for removing all the containers in the host OS.
		 
    '''
    s="docker stop $(docker ps -a -q)"
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("stop container problem...")
    s="docker rm $(docker ps -a -q)"
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("stop container problem...")
#----------------------------------------------------------------------------------------------------------------------





#part 5: removing the bridge ------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def rm_bridge(network_name):
    '''
         This function is for removing the bridge.
		 
    '''
    s="docker network rm "+network_name
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("remove bridge problem...")
    s="docker rm $(docker ps -a -q)"
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
    except:
         print("remove bridge problem...")
#----------------------------------------------------------------------------------------------------------------------
		 
#initSWEM()
#rmContainers()







