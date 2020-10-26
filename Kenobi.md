# Kenobi

This is a writeup for the [Kenobi](https://tryhackme.com/room/kenobi) TryHackMe room.

### Task 1: Deploy the vulnerable machine

![darth_vader](/room_kenobi/dv.gif)

This room will cover accessing a Samba share, manipulating a vulnerable version of proftpd to gain initial access and escalate your privileges to root via an SUID binary.

1. Make sure you're connected to our network and deploy the machine

   Machine IP: 10.10.220.207

   > No answer needed

2. Scan the machine with nmap, how many ports are open?

   Command: `nmap -sV -p- 10.10.220.207`. [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/room_kenobi/nmap_scans/scan_results.log)

   > 7

   (*I know there's more than 7 ports open according to the scan results, but I took the ports open with the number less than 10000*)

### Task 2: Enumerating Samba for shares

![samba](/room_kenobi/samba.png?raw=true)

Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often refereed to as a network file system.

Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network.

1. Using nmap we can enumerate a machine for SMB shares.

   Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!

   `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.220.207`

   SMB has two ports, 445 and 139.

   ![ports](/room_kenobi/ports.png?raw=true)

   Using the nmap command above, how many shared have been found?

   [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/room_kenobi/nmap_scans/smb_scan.log)

   > 3

2. On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.

   `smbclient //10.10.220.207/anonymous`

   Using your machine, connect to the machines network share.

   ![smbclient](/room_kenobi/screenshots/smbclient.png?raw=true)

   Once you're connected, list the files on the share. What is the file can you see?

   > log.txt

3. You can recursively download the SMB share too. Submit the username and password as nothing.

   `smbget -R smb://10.10.220.207/anonymous`

   Open the file on the share. There is a few interesting things found.

   - Information generated for Kenobi when generating an SSH key for the user
   - Information about the ProFTPD server.

   What port is FTP running on?

   *You can find the answer to this one either from the log.txt file, either in the nmap scan results.*

   > 21

4. Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just an server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve.

   In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

   `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.220.207`

   [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/room_kenobi/nmap_scans/nfs_scan.log)

   What mount can we see?

   > /var

### Task 3: Gain initial access with ProFtpd

![proftpd](/room_kenobi/proftpd.png?raw=true)

ProFtpd is a free and open-source FTP server, compatible with Unix and Windows systems. Its also been vulnerable in the past software versions.

1. Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port.

   What is the version?

   Command: `nc 10.10.220.207 21`

   ![screenshot_nc](/room_kenobi/screenshots/nc.png?raw=true)

   > 1.3.5

2. We can use searchsploit to find exploits for a particular software version.

   Searchsploit is basically just a command line search tool for exploit-db.com.

   How many exploits are there for the ProFTPd running?

   ![screenshot_searchsploit](/room_kenobi/screenshots/searchsploit.png?raw=true)

   > 3

3. You should have found an exploit from ProFtpd's [mod_copy module](http://www.proftpd.org/docs/contrib/mod_copy.html).

   The mod_copy module implements SITE CPFR and SITE CPTO commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.

   We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user.

   > No answer needed

4. We're now going to copy Kenobi's private key using SITE CPFR and SITE CPTO commands.

   ![screenshot_site](/room_kenobi/screenshots/site.png?raw=true)

   We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.

   > No answer needed

5. Lets mount the /var/tmp directory to our machine

   ```
   mkdir /mnt/kenobiNFS
   mount machine_ip:/var /mnt/kenobiNFS
   ls -la /mnt/kenobiNFS
   ```

   ![screenshot_mount](/room_kenobi/screenshots/mount.png?raw=true)

   We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.

   ![screenshot_ssh](/room_kenobi/screenshots/ssh.png?raw=true)

   What is Kenobi's user flag (*/home/kenobi/user.txt*)?

   > d0b0f3f53b6caa532a83915e19224899

### Task 4: Priviledge Escalation with Path Variable Manipulation

![perm](/room_kenobi/perm.png?raw=true)

Lets first understand what SUID, SGID and Sticky Bits are.

![perms](/room_kenobi/perms.png?raw=true)

1. SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.

   To search the a system for these type of files run the following: `find / -perm -u=s -type f 2>/dev/null`

   What file looks particularly out of the ordinary?

   ![screenshot_find](/room_kenobi/screenshots/find.png?raw=true)

   > /usr/bin/menu

2. Run the binary, how many options appear?

   ![screenshot_menu](/room_kenobi/screenshots/menu.png?raw=true)

   > 3

3. Strings is a command on Linux that looks for human readable strings on a binary.

   ![curl](/room_kenobi/curl.png?raw=true)

   This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname).

   As this file runs as the root users privileges, we can manipulate our path to gain a root shell.

   ![screenshot_pe](/room_kenobi/screenshots/pe.png?raw=true)

   We copied the /bin/sh shell, called it curl, gave it the correct permissions and then put its location in our path. This meant that when the /usr/bin/menu binary was run, its using our path variable to find the "curl" binary.. Which is actually a version of /usr/sh, as well as this file being run as root it runs our shell as root!

   > No answer needed

4. What is the root flag (/root/root.txt)?

   ![screenshot_flag](/room_kenobi/screenshots/flag.png?raw=true)

   > 177b3cd8562289f37382721c28381f02
