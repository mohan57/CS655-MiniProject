##used to download package information from all configured sources
sudo apt-get update

#high-performance building block for cloud services 
sudo apt-get install trafficserver

#repository for temporary system files that are not needed across system reboots
cd /var/run

#used to make a new directory for trafficserver
sudo mkdir trafficserver

#refers to a folder in the root called etc(bring user to root)
cd /etc/trafficserver/

#vi is used to edit an existing file
#records.config - list of configurable variables used by the Traffic Server software  
sudo vi records.config