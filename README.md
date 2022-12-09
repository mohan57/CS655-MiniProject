# CS655-MiniProject

create a structure using the RSpec file provided 
reserve your desired resources we have used Cornell InstaGeni
on the node-1 and node-2 run the Packages.sh to install the required packages to run the code and build the graph
on Server run the Serverside.sh to configure it
after running the above file on server a notepad is open and you are supposed to add below lines to avoid the issues with regular port : 
-> type i and move the cursor near the files to add the below lines

 CONFIG proxy.config.url_remap.remap_required INT 0
  CONFIG proxy.config.reverse_proxy.enabled INT 0


->After adding the line , enter ESC 
->Now type :wq and press enter to save the file

- now on the node-1 upload the withoutCache.py file using scp and run the py file using : python withoutCache.py 

TO run withCache.py file :-
- on the Server run the following commands:
	cd /usr/bin
	sudo ./traffic_server start
- on the node-2 upload the withCache.py file and run : python withCache.py
