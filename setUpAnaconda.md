1. Get ubuntu server VM from cloud.labs.teradata.com  as below
2. login to your machine with username - root password - TCAMPass123
3. echo '/dev/sdb1       /data   ext4    defaults        0       0' >> /etc/fstab — (This file is used to control what file systems are mounted when the system boots)
4. fdisk /dev/sdb1 - formatting disk space 
   Command (m for help): n
   select Partition type as p
   Command (m for help): w
5. mkfs.ext4 /dev/sdb1 – format partition with ext4 file system
6. mkdir /data 
7. mount /dev/sdb1 /data -  mount /data directory (rest of the work will be done on this directory)
8.  adduser <username>  #You have to give the details like password and the name. Other information can be kept blank.
usermod -aG sudo <username>
9. change permissions of /data directory
   chown <username>
   chgrp <username>
   chmod 777 /data
10. login with your username and password on to the server
11. Get Anaconda package from https://www.anaconda.com/download/#linux. Use the below command to download directly on to your vm
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
#Run the script file with ./Anaconda3-5.3.0-Linux-x86_64.sh. #Please do not run it as root or with sudo command. Just run it as a user. Accept the license
12. while running script it prompts for working directory give it as /data/anaconda3 
Say no when it prompts to install vscode from Microsoft.
13. After installation, logout and login again
14. To check everything is working, run this command on the shell. python -c "from sklearn.metrics import confusion_matrix"
15. You should not see any Exceptions or errors when you run the above command.
