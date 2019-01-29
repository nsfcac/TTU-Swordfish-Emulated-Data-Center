# TTU-Swordfish-Emulated-Data-Center

# Swordfish Emulated Data Center (SW-EDC) documentation

Swordfish Emulated Data Center is a project which provides an emulated testbed cluster using Docker containerization [1] technique for testing the scalability of Swordfish-API-Emulator [2].
Using this tool it is possible to create a network bridge, create a cluster contains some swordfish enabled nodes, expand the cluster, remove the cluster, or some of the nodes of that. Also it is possible to send get, post, and patch requests to the nodes. It also contains some scenarios for expanding the size of an emulated node by adding some Storage Systems, or Storage Services into that node. 
This project is suitable for testing the scalability of Swordfish-API-Emulator by expanding the testbed. To do that, you can add the number of compute nodes, or you can make a big node which contains thousands of storage systems, or storage services. You can modify information related to Swordfish API for each node using the tool. 
Also this tool provides a connection between Swordfish project and HTTP Prompt project [3], by adding this feature to the SW-EDC tool. So using the tool you can easily send HTTP prompt requests to each of the nodes of the cluster.

Using containerization technique it is possible to have a light weight cluster, which can be built, shipped and run easily. Because of using Docker technology gives SW-EDC (Swordfish Emulated Data Center) the following advantages. 
-	Scalability is one of the advantages of SW-EDC. You can use 
-	Portability is another advantage of the project. It is a portable cluster that you can have it in any host node you want.
-	SW-EDC has a great provisioning time compare to other environments such as bare-metal or virtual machine, which is another advantage of the project. 
-	Security of usage is another feature of SW-EDC.  You can run any command you want against the cluster. If you messed up something related to one or some of the nodes you can simply remove them and create them again without having any damage against any real compute node.
-	 Simplicity of setup, usage, configuration, expand, destroy and rebuild 
-	Speed
-	Fast developing
-	Fast provisioning  and building
-	Fast testing
-	Fast deploying
-	Fast update 
-	Fast recover
-	density

	Bare metal	Virtual machine	Container
Provisioning 			
Portability			
Performance			
Flexibility in reconfiguring process			
Scalability			

# User guideline

##  1- Setup the environment

For setup the environment, you need to have access to a host machine, and install Docker CE in that node. 
Please visit the following links, if you use Windows operating system on your host machine:

https://hub.docker.com/editions/community/docker-ce-desktop-windows

https://docs.docker.com/docker-for-windows/

Please visit the following links, if you use Mac operating system on your host machine:

https://hub.docker.com/editions/community/docker-ce-desktop-mac

https://docs.docker.com/docker-for-mac/#install-shell-completion

https://docs.docker.com/docker-for-mac/troubleshoot/

The best and easiest way for using Docker is installing that in Linux operating system. Docker was made for Linux. In Mac and windows Docker runs of a small Linux virtual machine in the background, but for Linux host, Docker runs directly on the host operating system.
Please visit the following links, if you use Centos operating system on your host machine:

https://docs.docker.com/install/linux/docker-ce/centos/

https://get.docker.com/

Run the following commands from the link above to install the newest version of Docker.

   $ curl -fsSL https://get.docker.com -o get-docker.sh
   
   $ sh get-docker.sh
   
  $ sudo usermode –aG docker your-username
  
  $ sudo docker version
  
  $ systemctl start docker
  
  Then install Docker machine and Docker compose and check if they installed correctly:
  
https://github.com/docker/machine/releases

https://github.com/docker/compose/releases

  $ docker-machine version
  
  $ docker-compose version

## 2- Installation

SW-EDC (Swordfish Emulated Data Center) is a python program. To use it, you need to install python and the following packages (using pip or conda)
-	python -m pip  install subprocess   
- python -m pip  install os   
-	python -m pip  install socket   
-	python -m pip  install ipaddress   
-	python -m pip  install json   
-	python -m pip  install datetime   
-	python -m pip  install random   
-	python -m pip  install time   
-	python -m pip  install threading   
-	python -m pip  install sys   
-	python -m pip  install colorama    
-	python -m pip  install termcolor   
-	python -m pip  install pyfiglet   
-	python -m pip  install cs    
-	python -m pip  install tkinter   
-	python -m pip  install pygments    
-	python -m pip  install requests

This application is a GUI python application. If you want to run it in Windows operating system, you need to install an X Server program such as Xming, or Cygwin/X which are free X Servers.  X Server is installed in Linux/ UNIX or Mac operating Systems by default. Visit the following link to install Xming program.

http://www.straightrunning.com/XmingNotes/

## 3- Running Tests

Please visit the following link and check the videos which show how to use the application.

https://www.youtube.com/watch?v=BgkLgPYybzk&feature=youtu.be

https://drive.google.com/drive/folders/1OQpM2YkFtX-xD8tCkVPSVF-Sfaky116b?usp=sharing 

# Acknowledgments

This research is supported by the Cloud and Autonomic Computing site and High Performance Computing Center at Texas Tech University and the collaboration with Dell Inc., SNIA and DMTF.   Many thanks to Mr. [Jon Hass](https://github.com/JonHass) , Ms. [Richelle Ahlvers](https://github.com/rahlvers) , Mr. [Don Deel](https://github.com/ddeel) , Dr. [Alan Sill](https://github.com/alansill), and Dr. [Yong Chen](https://www.depts.ttu.edu/cs/faculty/yong_chen/index.php)  for their guidance, help and support. 
# References

[1] https://www.docker.com/.

[2] https://github.com/SNIA/Swordfish-API-Emulator.

[3] http://http-prompt.com/.





