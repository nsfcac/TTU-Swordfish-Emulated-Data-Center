

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''



#This code is for sending  get requests

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


#part 1: getting IP by sending shell command --------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def get_ip_onecontainer(s,i,o,network_name):
    '''
         This function is for getting IP, by sending shell command.
		 
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

		

		      		
 
#part 2: getting IP of one node ---------------------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def getIPone(n,network_name):
    '''
         This function is for getting IP of one node.
		 
    '''


    #n=int(input("How many nodes you have in your cluster: "))          

    if (network_name=="SWEDCnetwork"):
        s= "docker inspect --format '{{.NetworkSettings.Networks.SWEDCnetwork.IPAddress}}' sw-node"+str(n)
    else:
        s= "docker inspect --format '{{.NetworkSettings.Networks."+network_name+".IPAddress}}' "+network_name+"-sw-node"+str(n)	
    o=get_ip_onecontainer(s,n,2, network_name)
	
    return(o)
	
	 
#initSWEM()
#showIPS()
#----------------------------------------------------------------------------------------------------------------------	





#part 3: running the requested get command ----------------------------------------------------------------------------   	 
#----------------------------------------------------------------------------------------------------------------------
def run_get_command(num,uri,network_name):
    '''
         This function is for runnig the requested get command.
		 
    '''
    
    
    ip=getIPone(num,network_name)

    s= "curl -k http://"+ip+":5000/"+uri
    try:
         (output, err) = subprocess.Popen(s, stdout=subprocess.PIPE, shell=True).communicate()
         output=str( output)[2:-3]
    except:
         print("Handle shell processes.......")

	
    return(output)
#----------------------------------------------------------------------------------------------------------------------


