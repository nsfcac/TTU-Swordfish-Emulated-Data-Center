

'''
This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.
Author=Elham Hojati
'''




#This code provides a GUI for "Swordfish Emulated Data Center" Application 

import json
from pygments import highlight, lexers, formatters
from tkinter import *    
from tkinter import messagebox
import random 
import time
import datetime
import swedc_create
import swedc_rm
import swedc_expand
import swedc_ip
import swedc_get
import swedc_post
import swedc_patch
import swedc_http_prompt
import swedc_big_node_scenario
root=Tk()
clusterSize=0
removednodenumber=0
network_name="SWEDCnetwork"
network_subnet="172.20.0.0/16"


#part 1: This function is the main function for starting the GUI Env.--------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def main():
    '''
         This function is the main function for runnig the GUI
		 
    '''
    root.geometry("1350x670+0+0")
    root.title("Swordfish Emulated Data Center")
    root.configure(background='cadet Blue')
    create_menuebar(root)
    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------





#part 2: This function is for creating a top level menu----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def create_menuebar(root):
    '''
         This function is for creating a toplevel menu
		 
    '''
    menubar = Menu(root)

#"Update Cluster" menu creates a pulldown menu, and add it to the menu bar, we can Create a cluster, expand or remove it from this menue tab.
    clusterUpdatemenue = Menu(menubar, tearoff=0)
    clusterUpdatemenue.add_command(label="Network Initialization", command=netini)
    clusterUpdatemenue.add_command(label="Create Cluster", command=createc)
    clusterUpdatemenue.add_command(label="Remove Cluster", command=removec)
    clusterUpdatemenue.add_command(label="Expand Cluster", command=expandc)

    clusterUpdatemenue.add_separator()
    clusterUpdatemenue.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Cluster Update", menu=clusterUpdatemenue)

#"Cluster Display" menu creates a pulldown menu, and add it to the menu bar, we can Create a cluster, expand or remove it from this menue tab.
    clusterDisplaymenue = Menu(menubar, tearoff=0)
    clusterDisplaymenue.add_command(label="Cluster Information (IP and Name)",command=display_IP_Name_c)
    clusterDisplaymenue.add_command(label="Nodes List by Name",command=display_IP_Name_c)
    clusterDisplaymenue.add_command(label="Nodes List by IP Address",command=display_IP_Name_c)
    clusterDisplaymenue.add_command(label="Cluster Network Information" ,command=display_net_info)
    clusterDisplaymenue.add_command(label="One Node Information" ,command=display_one_node_info)	
    clusterDisplaymenue.add_command(label="Cluster Size Information",command=display_size)
    clusterDisplaymenue.add_separator()
    clusterDisplaymenue.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Cluster Display", menu=clusterDisplaymenue)
	
#"Run Swordfish Commands" menu is for sending get, post, and patch requests
    commandmenu = Menu(menubar, tearoff=0)
    commandmenu.add_command(label="Get Command", command=getreq )
    commandmenu.add_command(label="Post Command", command=postreq  )
    commandmenu.add_command(label="Patch Command",  command=patchreq   )
    commandmenu.add_command(label="http-prompt Command",  command=http_prompt_req  )	
    menubar.add_cascade(label="Run Swordfish Commands", menu=commandmenu)
	

#"Swordfish Scenario" f1b creates a pulldown menu contains some senarios to change the content of swordfish features and define big nodes	
    scenariomenu = Menu(menubar, tearoff=0)
    scenariomenu.add_command(label="make big nodes", command=big_node_s )
    menubar.add_cascade(label="Swordfish Scenario", menu=scenariomenu)
	
#"Help" menu creates a pulldown menu contains help and about parts
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About" command=about_me)
    helpmenu.add_command(label="Help" command=help_me)
    menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
    root.config(menu=menubar)
#----------------------------------------------------------------------------------------------------------------------





#part 3: This function is for network initialization-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def netini():
    '''
         This function is for network initialization. It gets the name and the subnet of the bridge and it creates a new bridge.
		 
    '''
    global clusterSize
    global network_name
    global network_subnet
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hint1="You can create your own network bridge for the cluster ( by inserting name & subnet )."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hint1, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left', width=75)
    hintlabel.grid(row=0, column=0)

    hint3="Or by pressing the default button, you can use the default network."
    hint3label=Label(f1a, font=('arial', 14, 'bold') , text=hint3, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left', width=75)
    hint3label.grid(row=1, column=0)

# f1b frame content  		
    net_name=Label(f1b, font=('arial', 14, 'bold') , text=" New Network Bridge Name: ", fg="midnight blue", bd=10,    anchor='w',  justify='left')
    net_name.grid(row=0, column=0,  columnspan=20)
		
    text_Input1=StringVar()
    txtDisplay1=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input1,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay1.grid(row=0, column=30, columnspan=50)

    net_subnet=Label(f1b, font=('arial', 14, 'bold') , text="New Subnet: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    net_subnet.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=30, columnspan=50)


# f2 frame content	
    result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    result.grid(row=0, column=0,  columnspan=200)

#function for creating a Network  
    def createNetwork():
       global network_name
       global network_subnet
       name=text_Input1.get()
       subnet=text_Input2.get()

       try:      
           name_val = str(name)
           subnet_val=str(subnet)
       except ValueError:
           messagebox.showinfo("Warning","The selected name or subnet is not acceptable. ")

       swedc_create.create_network(name_val,subnet_val)	   
       createClusterMessage()
       #result.config(text = "Network "+name_val+" with subnet "+subnet_val+" has been created.")
       result.config(text = "Network has been created.")
       network_name=name_val
       network_subnet=subnet_val

 #function for printing a message after successfully creating a Network. 
    def createClusterMessage():   
        messagebox.showinfo("Creating Network Bridge","Network has been created.")	
	

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input1.set("") 
        text_Input2.set("")   		
        result.config(text ="")
      
#function for creating the default network
    def defaultSetting():
       global network_name
       global network_subnet
       network_name="SWEDCnetwork"
       network_subnet="172.20.0.0/16"

       swedc_create.create_network(network_name,network_subnet)	   
       createClusterMessage()
       #result.config(text = "Network "+network_name+" with subnet "+network_subnet+" has been created.")
       result.config(text = "Network has been created.")

       


	  
# button create  
    btnsend=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Create", background="cadet Blue", command=createNetwork).grid(row=30, column=0,columnspan=8)
      
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=30, column=8,columnspan=8)
	
# button clear    
    btndefault=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Default Setting", background="cadet Blue", command=defaultSetting).grid(row=30, column=16,columnspan=10)
	
#----------------------------------------------------------------------------------------------------------------------





#part 4: This function is for creating a cluster ----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def createc():
    '''
         This function is for creating a cluster. It contains some sub-functions as well.
		 
    '''
    global clusterSize
    global network_name
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 1300, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 1300, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="To create a Swordfish clucter, insert the number of compute nodes:"
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text=" New Cluster Size: ", fg="midnight blue", bd=10,    anchor='w',  justify='left')
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',20,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=4,bg="white", justify='left' )
    txtDisplay.grid(row=0, column=40, columnspan=20)

# f2 frame content	
    result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    result.grid(row=0, column=0,  columnspan=200)

#function for creating a cluster   
    def createCluster():
       global clusterSize
       global network_name
       num=text_Input.get()
       val=100
       try:      
           val = int(num)
       except ValueError:
           messagebox.showinfo("Warning","The selected size is not acceptable. it should be a number between 0 to 100. We will use the defult size (100 nodes). ")
           val=100
       m=swedc_create.createContainers(val,network_name)		   
       createClusterMessage(m)
       result.config(text = "The Swrodfish Emulated cluster with "+str(val)+" nodes has been created.")
       clusterSize=val

 #function for printing a message after successfully creating a cluster. 
    def createClusterMessage(m):   
        messagebox.showinfo("Create the Swordfish Emulated Cluster","The Swordfish Emulated Cluster has been created successfully. ")	   

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	   
        result.config(text ="")
      
# button create  
    btnsend=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Create", background="cadet Blue", command=createCluster).grid(row=30, column=0,columnspan=8)
      
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=30, column=15,columnspan=8)

#----------------------------------------------------------------------------------------------------------------------
 


 

#part 5: This function is for removing a cluster ----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def removec():
    '''
         This function is for removing a cluster. It contains some sub-functions as well.
		 
    '''
    global clusterSize
    global removednodenumber
    global network_name
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 1300, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 1300, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Press the Remove key to remove the cluster. Warning: This process is going to remove all data in compute nodes!!!!"
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text=" Compute-Node Number: ", fg="midnight blue", bd=10,    anchor='w',  justify='left')
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',20,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=4,bg="white", justify='left' )
    txtDisplay.grid(row=0, column=40, columnspan=20)

 
# f2 frame content 
    result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    result.grid(row=0, column=0,  columnspan=200)

#function for creating a cluster   
    def rmCluster():
       global clusterSize
       global removednodenumber	
       global network_name	   
       swedc_rm.rmContainers(clusterSize+removednodenumber,network_name)
       if(network_name!="SWEDCnetwork")	:
            swedc_rm.rm_bridge(network_name)	   
       showClusterMessage()
       result.config(text = "The Swrodfish Emulated cluster with "+str(clusterSize)+" nodes has been removed completely.")
       clusterSize=0
       removednodenumber=0

#function for creating a cluster   
    def rmCluster_fast():
       global clusterSize
       global removednodenumber	   
       swedc_rm.rm_Container_fast()		   

       result.config(text = "All the containers have been removed completely.")
       clusterSize=0	   
	   
	   
#function for printing a message after successfully removing a cluster. 
    def showClusterMessage():
        global clusterSize	
        messagebox.showinfo("Remove Cluster","The Cluster with "+str(clusterSize)+" compute nodes has been removed successfully.")	   

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	   
        result.config(text ="")     

    def rmNode():
       global clusterSize
       global removednodenumber
       num=text_Input.get()
       val=1
       notnum=False
       try:      
           val = int(num)
       except ValueError:
           messagebox.showinfo("Warning","The number is not acceptable. ")
           notnum=True
           val=-1
       if (val==0 or val>clusterSize+removednodenumber or val <0):
                if( not notnum):
	                            messagebox.showinfo("Error","The number is not an acceptable number.")
       else:
	                            swedc_rm.rm_Container_by_number(val,network_name)                               								
	                            createClusterMessage2(val)
	                            result.config(text = "Compute Node sw-node"+str(val)+" has been removed")
	                            clusterSize=clusterSize-1
	                            removednodenumber=removednodenumber+1
	   
#function for printing a message after successfully removing a node. 
    def createClusterMessage2(n):
        global clusterSize	
        messagebox.showinfo("Remove node","Compute Node sw-node"+str(n)+" has been removed successfully.")	   

      
# button remove one node    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Remove Selected Node", background="cadet Blue", command=rmNode).grid(row=30, column=0,columnspan=22)
		
# button remove  
    btnrm=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Remove Cluster", background="cadet Blue", command=rmCluster).grid(row=30, column=30,columnspan=15)
	  
 # button remove all fast  
    btnrm=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Remove all", background="cadet Blue", command=rmCluster_fast).grid(row=30, column=48,columnspan=15)    
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=30, column=68,columnspan=22)

#----------------------------------------------------------------------------------------------------------------------
 



 
#part 6: This function is for updating the size of the cluster  -------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def expandc():
    '''
         This function is for expanding a cluster. It contains some sub-functions as well.
		 
    '''
    global clusterSize
    global removednodenumber
    global network_name
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 1300, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 1300, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="To expand the Swordfish clucter, insert the number of compute nodes you want to add:"
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Cluster Expand Size: ", fg="midnight blue", bd=10,    anchor='w',  justify='left')
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',20,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=4,bg="white", justify='left' )
    txtDisplay.grid(row=0, column=40, columnspan=20)

# f2 frame content	
    result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    result.grid(row=0, column=0,  columnspan=200)

#function for expanding a cluster   
    def expandCluster():
       global clusterSize
       global removednodenumber
       num=text_Input.get()
       val=100
       try:      
           val = int(num)
       except ValueError:
           messagebox.showinfo("Warning","The selected size is not acceptable. it should be a number between 0 to 100. We will use the defult size (100 nodes). ")
           val=100
       swedc_expand.createContainers(clusterSize,val, removednodenumber,network_name)		   
       createClusterMessage()
       result.config(text = "The Swrodfish Emulated cluster has been expanded to "+str(val+clusterSize)+" nodes has been created.")
       clusterSize=clusterSize+val

 #function for printing a message after successfully expandg a cluster. 
    def createClusterMessage():   
        messagebox.showinfo("Expand the Swordfish Emulated Cluster","The Swordfish Emulated Cluster has been expanded successfully. ")	   

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	   
        result.config(text ="")
      
# button create  
    btnsend=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Expand", background="cadet Blue", command=expandCluster).grid(row=30, column=0,columnspan=8)
      
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=30, column=15,columnspan=8)

#----------------------------------------------------------------------------------------------------------------------
 


 
		
#part 7: This function is for Displaying cluster information: list of node name and IP  -------------------------------
#----------------------------------------------------------------------------------------------------------------------
def display_IP_Name_c():
    '''
         This function is for displaying cluster information: list of node name and IP.
		 
    '''
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
    global network_name
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="To display Cluster info, press the related key."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left')
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',20,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=4,bg="white", justify='left' )
    txtDisplay.grid(row=0, column=10, columnspan=40)

# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=80, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")


# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)


	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for Display all info of  a cluster   (Name and IP of nodes)
    def showc(i):
       global clusterSize
       global removednodenumber
       global network_name
       if(i!=0 and i!=4):
                 textres.delete('1.0', END)	   
                 res=swedc_ip.showIPS(clusterSize+removednodenumber,i,network_name)
                 textres.insert(END, res)
	     
       if(i==4):
                 	   
                  num=text_Input.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                              messagebox.showinfo("Error","The number is not an acceptable number.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_ip.showIPone(val,network_name)
                        textres.insert(END, str(t))
                        #messagebox.showinfo("Node Info",str(t))								
	                        


   
	   	   	   

		   
 #Write to the file:
       try:
             if(i==1):
                 f= open("Cluster-All-Info.txt","w+")
                 f.write(res)
                 messagebox.showinfo("Info","The cluster Information (name and IP of nodes) has been written in  in the \"Cluster-All-Info.txt\" file ")
                 f.close()
             if(i==2):
                 f= open("Cluster-IP-Info.txt","w+")
                 f.write(res)
                 messagebox.showinfo("Info","The cluster Information (name and IP of nodes) has been written in  in the \"Cluster-IP-Info.txt\" file ")	
                 f.close()				 
             if(i==3):
                 f= open("Cluster-Name-Info.txt","w+")
                 f.write(res)
                 messagebox.showinfo("Info","The cluster Information (name and IP of nodes) has been written in  in the \"Cluster-Name-Info.txt\" file ")
                 f.close()				             			 
             

       except:
             messagebox.showinfo("Error","Error occurs in writing to the file.")
       if(i==0):
	   
                  num=text_Input.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                        if(not notnum):
                              messagebox.showinfo("Error","The number is not an acceptable number.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_ip.showIPone(val,network_name)
                        textres.insert(END, str(t))
                        messagebox.showinfo("Node Info",str(t))								
	                        
	   	   
	   	   
 
       #result.config(text = "The Swrodfish Emulated cluster has been expanded to "+str(val+clusterSize)+" nodes has been created.")


	   	   
#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	   
        #result.config(text ="")
        textres.delete('1.0', END)
      
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="One Node Info", background="cadet Blue", command=lambda:showc(4)).grid(row=30, column=0)
    btn1=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Show IP & Name         ", background="cadet Blue", command=lambda:showc(5)).grid(row=30, column=10)
    btn2=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Show IP          ", background="cadet Blue", command=lambda:showc(6)).grid(row=30, column=20) 
    btn3=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Show Name                   ", background="cadet Blue", command=lambda:showc(7)).grid(row=30, column=30) 
    	
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=0, column=30, columnspan=8)

	
	
 #button create  
    btn4=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="One Node Info", background="cadet Blue", command=lambda:showc(0)).grid(row=40, column=0,columnspan=8)
    btn5=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Update IP & Name File", background="cadet Blue", command=lambda:showc(1)).grid(row=40, column=10,columnspan=8)
    btn6=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Update IP File", background="cadet Blue", command=lambda:showc(2)).grid(row=40, column=20,columnspan=8) 
    btn7=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Update Node Name File", background="cadet Blue", command=lambda:showc(3)).grid(row=40, column=30,columnspan=8) 
    		
#----------------------------------------------------------------------------------------------------------------------
  
  


  
#part 8: This function is for Displaying Network information: ---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def display_net_info():
    '''
         This function is for displaying Network information.
		 
    '''
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global network_name

# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 24, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="To display Network info, press the key."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		

# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=80, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")


# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)


	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for Display all info of  a cluster   (Name and IP of nodes)


    def is_json(myjson):
       try:

        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True
		
    def shownet():
          global network_name
          textres.delete('1.0', END)	   
          t=swedc_create.display_network_info(network_name)
          t=str(t)
          t=t.replace("\\n","\n")


		
          if (is_json(t)):
                       parsed = json.loads(t)
                       formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                       colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                       print(colorful_json)
                       textres.insert(END, formatted_json)
          else:
                       textres.insert(END, str(t))
                       print(str(t))
                        								
	  
	   	   	   

		   

	   	   
#function for clearing the content of window				
    def contentClear():
        textres.delete('1.0', END)
      
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Network Info", background="cadet Blue", command=shownet).grid(row=0, column=0)

# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue", command=contentClear).grid(row=1, column=0)

	
	
#----------------------------------------------------------------------------------------------------------------------
  

  
  
  
 #part 9: This function is for Displaying cluster information: list of node name and IP  -------------------------------
#----------------------------------------------------------------------------------------------------------------------
def display_one_node_info ():
    '''
         This function is for displaying all information about one node in the cluster
		 
    '''

    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
    global network_name
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Insert node number and network name (default= SWEDCnetwork)"
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Network Name: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)

# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)


	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)	

    def is_json(myjson):
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True
		
    def get_info_command():
                  global network_name
                  num=text_Input.get()
                  network=text_Input2.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                             messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	  
                        if(network==network_name or network==""):						
                               t=swedc_create.display_all_one_node_info(network_name,val)
                        else:
                               messagebox.showinfo("Warning","Network input is not the same as the current network name. ")
                               t=swedc_create.display_all_one_node_info(network,val)
                        t=str(t)
                        t=t.replace("\\n","\n")
                   

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
	  
        
	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Send", background="cadet Blue", justify='left', command=get_info_command).grid(row=2, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=3, column=0)
#----------------------------------------------------------------------------------------------------------------------




		
#part 10: This function is for Displaying cluster information: list of node name and IP  ------------------------------
#----------------------------------------------------------------------------------------------------------------------
def display_size():
    '''
         This function is for displaying the size of the cluster
		 
    '''	
    global clusterSize
    global removednodenumber
    messagebox.showinfo("Cluster Size Info","Cluster Size=  "+str(clusterSize)+"\n Removed Nodes#= "+str(removednodenumber))
    
#----------------------------------------------------------------------------------------------------------------------



		
#part 11: This function is for Displaying cluster information: list of node name and IP  ------------------------------
#----------------------------------------------------------------------------------------------------------------------
def getreq ():
    '''
         This function is for displaying cluster information: list of node name and IP.
		 
    '''
    global network_name
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Insert node name and the requested URI then press the GET Button."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Requested URI: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)

# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)


	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)	

    def is_json(myjson):
	
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True
		
    def getcommand():
                  global network_name
                  num=text_Input.get()
                  uri=text_Input2.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                             messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_get.run_get_command(val,uri,network_name)
                        t=str(t)
                        t=t.replace("\\n","\n")
                   

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
	  
        
	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="GET", background="cadet Blue", justify='left', command=getcommand).grid(row=2, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=3, column=0)
#----------------------------------------------------------------------------------------------------------------------




#part 12: This function is for Displaying cluster information: list of node name and IP  ------------------------------
#----------------------------------------------------------------------------------------------------------------------
def postreq ():
    '''
         This function is for displaying cluster information: list of node name and IP.
		 
    '''

    # Select all the text in textbox
    global network_name
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Insert node number,the requested URI, and the new item, then press the POST Button."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Requested URI: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)

    newitem=Label(f1b, font=('arial', 14, 'bold') , text="New Item:", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    newitem.grid(row=2, column=0,  columnspan=20)
		
    text_Input3=StringVar()
    txtDisplay3=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input3,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay3.grid(row=2, column=20, columnspan=50)
# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)

	

	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)	
    def is_json(myjson):
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True

	   
    def postcommand():
                  num=text_Input.get()
                  uri=text_Input2.get()
                  item=text_Input3.get()
                  global network_name
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                              messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_post.run_post_command(val,uri,item,network_name)
                        t=str(t)
                        t=t.replace("\\n","\n")

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
	  										
	  
        
	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="POST", background="cadet Blue", justify='left', command=postcommand).grid(row=3, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=4, column=0)
#----------------------------------------------------------------------------------------------------------------------
  	



#part 13: This function is for Displaying cluster information: list of node name and IP  ------------------------------
#----------------------------------------------------------------------------------------------------------------------
def patchreq ():
    '''
         This function is for sending patch requests
		 
    '''
    global network_name
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Insert node number,the requested URI, and the new item, then press the POST Button."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Requested URI: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)

    newitem=Label(f1b, font=('arial', 14, 'bold') , text="Key:", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    newitem.grid(row=2, column=0,  columnspan=20)
		
    text_Input3=StringVar()
    txtDisplay3=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input3,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay3.grid(row=2, column=20, columnspan=50)

    newitem=Label(f1b, font=('arial', 14, 'bold') , text="New Value:", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    newitem.grid(row=3, column=0,  columnspan=20)
		
    text_Input4=StringVar()
    txtDisplay4=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input4,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay4.grid(row=3, column=20, columnspan=50)
# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)

	
	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)	


    def is_json(myjson):
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True	  
        
		
    def patchcommand():
                  global network_name
                  num=text_Input.get()
                  uri=text_Input2.get()
                  key=text_Input3.get()
                  value=text_Input4.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                                messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_patch.run_patch_command(val,uri,key, value,network_name)
						
                        t=str(t)
                        t=t.replace("\\n","\n")

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
						
						
                   

	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="PATCH", background="cadet Blue", justify='left', command=patchcommand).grid(row=4, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=5, column=0)
#----------------------------------------------------------------------------------------------------------------------
  	


	
	
#part 14: This function is for Displaying cluster information: list of node name and IP  ------------------------------
#----------------------------------------------------------------------------------------------------------------------
def big_node_s():
    '''
         This function is for making big nodes by posting a lot of new branches there.
		 
    '''
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global network_name
    global clusterSize
    global removednodenumber
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints= "Insert the node number,the requested URI, new item name,"
    hints2=" and the number of items you want to add, then press the EXPAND button."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left', width=65)
    hintlabel.grid(row=0, column=0)
    hintlabel2=Label(f1a, font=('arial', 14, 'bold') , text=hints2, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left', width=65)
    hintlabel2.grid(row=1, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Requested URI: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)

    newitem=Label(f1b, font=('arial', 14, 'bold') , text="New Item:", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    newitem.grid(row=2, column=0,  columnspan=20)
		
    text_Input3=StringVar()
    txtDisplay3=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input3,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay3.grid(row=2, column=20, columnspan=50)
	
    repnum=Label(f1b, font=('arial', 14, 'bold') , text="How many new item?", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    repnum.grid(row=3, column=0,  columnspan=20)
		
    text_Input4=StringVar()
    txtDisplay4=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input4,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay4.grid(row=3, column=20, columnspan=50)
# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

	
# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)

	
	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')

#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)
		
		
    def is_json(myjson):
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True
		
		
    def make_big_node():
                  global network_name
                  num=text_Input.get()
                  uri=text_Input2.get()
                  item=text_Input3.get()
                  repnum=text_Input4.get()
                  val=1
                  notnum=False
                  try:    
                        repnum=int(repnum)				  
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                     if(not notnum):
                              messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_big_node_scenario.run_sc1(val,uri,item,repnum,network_name)
						



                        t=str(t)
                        t=t.replace("\\n","\n")

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
                        								
	  
        
	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="EXPAND NODE", background="cadet Blue", justify='left', command=make_big_node).grid(row=4, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=5, column=0)

  	
	
























#part 6: This function is for Displaying cluster information: list of node name and IP  -------------------------------
#----------------------------------------------------------------------------------------------------------------------
def http_prompt_req ():
    '''
         This function is for displaying cluster information: list of node name and IP.
		 
    '''
    global network_name
    # Select all the text in textbox
    def select_all(event):
         textres.tag_add(SEL, "1.0", END)
         textres.mark_set(INSERT, "1.0")
         textres.see(INSERT)
         return 'break'

    global clusterSize
    global removednodenumber
# clear the Window
    for widget in root.winfo_children():
        widget.destroy()

# create menubar		
    create_menuebar(root)

# create top menu
    tops=Frame(root,width=1350, height=50, bg="cadet blue",  relief=SUNKEN)
    tops.pack(side=TOP)

# create left menu  
    f1=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f1.pack(side=LEFT)  

# create right menu   
    f2=Frame(root,width=650, height=540, bg="cadet blue", relief=SUNKEN)
    f2.pack(side=RIGHT)

# configure the background of Frames
    f1.configure(background='cadet Blue')
    f2.configure(background='cadet Blue')

# tops frame content
    lbInfo=Label(tops, font=('arial', 28, 'bold') , text="Swordfish Emulated Data Center", fg="midnight blue", background='cadet Blue', anchor='w')
    lbInfo.grid(row=0, column=0)
    localtime=time.asctime(time.localtime(time.time()))
    lbInfo=Label(tops, font=('arial', 10, 'bold') , text=localtime, fg="navy", background='cadet Blue',  anchor='w')
    lbInfo.grid(row=1, column=0)
   
# sub frames for frame f1   
    f1a = Frame(f1, width = 650, height = 100,  relief = SUNKEN)
    f1a.pack(side = TOP)

    f1b = Frame(f1, width = 650, height = 460, bd = 4, relief = SUNKEN)
    f1b.pack(side = BOTTOM)
   
# f1a frame content  
    hints="Insert node name and the requested URI then press the http-prompt Button. Type exit to exit."
    hintlabel=Label(f1a, font=('arial', 14, 'bold') , text=hints, fg="Dark Blue", bd=10, background='cadet Blue',  anchor='w', justify='left')
    hintlabel.grid(row=0, column=0)

# f1b frame content  		
    sizec=Label(f1b, font=('arial', 14, 'bold') , text="Compute Node#: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    sizec.grid(row=0, column=0,  columnspan=20)
		
    text_Input=StringVar()
    txtDisplay=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left', width=40 )
    txtDisplay.grid(row=0, column=20, columnspan=50)
	
	
    uri=Label(f1b, font=('arial', 14, 'bold') , text="Requested URI: ", fg="midnight blue", bd=10,    anchor='w',  justify='left' )
    uri.grid(row=1, column=0,  columnspan=20)
		
    text_Input2=StringVar()
    txtDisplay2=Entry(f1b,font=('arial',17,'bold'),textvariable=text_Input2,bd=4, fg="Dark Blue", insertwidth=6,bg="white", justify='left' , width=40)
    txtDisplay2.grid(row=1, column=20, columnspan=50)
    #'''
# f2 frame content	
   # result=Label(f2, font=('arial', 16, 'bold') , text="", fg="midnight blue",   anchor='w',  justify='left')
    #result.grid(row=0, column=0,  columnspan=200)
	
    textres=Text(f2, width=90, height=35, bg="white", bd=4, font=('arial', 12,'bold'))
    textres.event_generate("<<Cut>>")
    textres.event_generate("<<Paste>>") 
    textres.event_generate("<<Copy>>")

# Add the binding
    textres.bind("<Control-Key-a>", select_all)
    textres.bind("<Control-Key-A>", select_all)


	
    textres.grid(row=0,column=0)

    # create a Scrollbar and associate it with txt
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb = Scrollbar(f2, command=textres.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')
    #'''
#function for clearing the content of window				
    def contentClear():
        global operator
        operator=""
        text_Input.set("") 	 
        text_Input2.set("") 			
        #result.config(text ="")
        textres.delete('1.0', END)	

    def is_json(myjson):
	
       try:
        json_object = json.loads(myjson)
       except ValueError:
             return False
       return True
		
    def httpcommand():
                  global network_name
                  num=text_Input.get()
                  uri=text_Input2.get()
                  val=1
                  notnum=False
                  try:      
                        val = int(num)
                  except ValueError:
                        messagebox.showinfo("Warning","The number is not acceptable. ")
                        notnum=True
                        val=-1
                  if (val==0 or val>clusterSize+removednodenumber or val <0):
                      if(not notnum):
                             messagebox.showinfo("Error","The number is not acceptable.")
                  else:
                        textres.delete('1.0', END)	   
                        t=swedc_http_prompt.find_http_command(val,uri,network_name)
                        t=str(t)
                        t=t.replace("\\n","\n")
                   

                        if (is_json(t)):
                            parsed = json.loads(t)
                            formatted_json=json.dumps(parsed, indent=4, sort_keys=True)
                            colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
                            print(colorful_json)
                            textres.insert(END, formatted_json)
                        else:
                            textres.insert(END, str(t))
                            print(str(t))
                        								
                    	  
                        t=swedc_http_prompt.run_http_command(num,uri,network_name) 
                        print(t)						
	
# button create  
    btn0=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="http-prompt", background="cadet Blue", justify='left', command=httpcommand).grid(row=2, column=0)
# button clear    
    btnclear=Button(f1b,padx=20,pady=16,bd=6,fg="midnight blue", font=('arial', 12, 'bold'),text="Clear", background="cadet Blue",justify='left', command=contentClear).grid(row=3, column=0)
#----------------------------------------------------------------------------------------------------------------------





#part 15: This function is for network initialization-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def about_me():

     messagebox.showinfo("about","This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.Author=Elham Hojati")

#----------------------------------------------------------------------------------------------------------------------





#part 16: This function is for network initialization-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------	
def help_me():

     messagebox.showinfo("help","Please visit https://github.com/elham1296/TTU-Swordfish-Emulated-Data-Center")

#----------------------------------------------------------------------------------------------------------------------




	
#part 17: Call the main function --------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
if __name__== "__main__":
  main()









