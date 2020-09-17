# Advent of Cyber

The link to the room can be found [here](https://tryhackme.com/room/25daysofchristmas). This writeup contains the solutions of the 2019 advent event on TryHackMe.

### Day 1: Inventory Management
### Day 2: Arctic Forum
### Day 3: Evil Elf
### Day 4: Training
### Day 5: Ho-Ho-Hosint
### Day 6: Data Elf-iltration
### Day 7: Skilling Up
### Day 8: SUID Shenanigans
### Day 9: Requests

I wrote a script that resolves this challenge. This script can be found in the [2019AdventOfCyber](https://github.com/pamhrituc/TryHackMe_Writeups/tree/master/2019AdventOfCyber) folder, under the name of [day9_requests.py](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/day9_requests.py).

First, the script accesses the IP address, 10.10.169.100. Next, the response is saved in the res variable, which contains the JSON object. Then, the IP address is accessed iteratively, until the value of the `next` key in the response is *end*. The flag is built with every iteration, adding the value of the `value` key to the `flag` variable until the *end* value is reached.

### Day 10: Metasploit-a-ho-ho-ho

First things first. We need to start Metasploit. Either you're using Kali and Metasploit is pre-install or you need to download and install [Metasploit](https://github.com/rapid7/metasploit-framework) yourself.

Once it's installed on your system, the `msfconsole` command will start the Metasploit Framework console interface.

The first thing I've done was use nmap to scan the machine for services said machine runs and the services. [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/nmap_scan_results/day10_metaploit.log)

The service that is of interest to us is Apache-Coyote 1.1. After doing some research, the vulnerability we're interested in is [CVE-2017-5638](https://www.exploit-db.com/exploits/41614).

Now that we know what cve we want to exploit, we search for struts2 in the msf database (`search struts2`).

![Screenshot_of_struts2](/2019AdventOfCyber/screenshots/day10/struts2.png?raw=true)

We use the `use exploit/multi/http/struts2_namespace_ognl` command to select that we want to exploit the machine using the struts2_namespace_ognl module. After selecting the module, the command `show options` will display what parameters are required to exploit the machine. The parameters can be set using the `set <name> <value>`.

In this case, we need to give the RHOSTS parameter the IP of the vulnerable machine (`set RHOSTS 10.10.118.185`). We also need to set the RPORT to 80 (`set RPORT 80`), the TARGETURI to *showcase.action* (`set TARGETURI showcase.action`).

![Screenshot_of_options](/2019AdventOfCyber/screenshots/day10/options.png?raw=true)

After setting the required parameters, we can run the exploit. This can be done using the `exploit` command or `run` command.

If the parameters and payload have been correctly configured, metasploit should open a reverse shell.

![Screenshot_of_reverse_shell](/2019AdventOfCyber/screenshots/day10/reverse_shell.png?raw=true)

After upgrading the shell (`script -qc /bin/bash /dev/null`), I search the flag using the following command: `find / -name "*[Ff][Ll][Aa][Gg]1*"`. The result of the find says the flag is in */usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt*. The `cat /usr/local/tomcat/webapps/ROOT/ThisIsFlag1.txt` command reveals the value of the flag.

I found Santa's SSH password in the /home directory (/home/santa/).

Next, I logged in as Santa using SSH (`ssh santa@10.10.118.185`), since his SSH password was found in the ssh-creds.txt file in Santa's home directory.

As Santa, the `ls -la` command reveals two files, *naughty_list.txt* and *nice_list.txt*.

I used the `cat -n naughty_list.txt | grep 148` command to find who is on line 148 of the naughty list and `cat -n nice_list.txt | grep 52` to see who is on line 52 of the nice list.

1. Compromise the web server using Metasploit. What is flag1?

   > THM{3ad96bb13ec963a5ca4cb99302b37e12}

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?

   > rudolphrednosedreindeer

3. Who is on line 148 of the naughty list?

   > Melisa Vanhoose

4. Who is on line 52 of the nice list?

   > Lindsey Gaffney

### Day 11: Elf Applications

1. What is the password inside the creds.txt file?

   First things first. I scanned the deployed machine using the following command: `nmap -sV 10.10.128.198`. [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/nmap_scan_results/day11_elf_apps.log). As seen in the scan results, the NFS service runs on port 2049. Since NFS is running on the deployed machine, I checked to see if any shares are available using `showmount -e ip-address` command. This command lists all the shared exported by NFS.

   The scan returns a single result: /opt/files. Next, I tried to mount the shares to my file system: `mount 10.10.128.198:/opt/files /local/file/path`. Once the files have been successfully mounted, I checked the local/file/path to see that a file named creds.txt has been mounted. This file contains the answer to this question.

   Finally, I unmounted the file system using the following command: `umount /local/file/path`

   > securepassword123

2. What is the name of the file running on port 21?

   For this question, I connected to the deployed machine through FTP (`ftp 10.10.128.198`), using the *anonymous* credentials (username: anonymous, password: anonymous). After connecting, I checked the contents of the current directory, finding a file named file.txt. Using the `get file.txt` command, I retreived the file to my system, where I checked its contents.

   ![screenshot_file](/2019AdventOfCyber/screenshots/day11/file.png?raw=true)

   Nice!

   > file.txt

3. What is the password after enumerating the database?

   I used mysql to get into the database using the credentials obtained in the previous question, using the following command: `mysql -h 10.10.128.198 -u root -p`. I entered the password when it was prompted.

   ![screenshot_mysql](/2019AdventOfCyber/screenshots/day11/mysql.png?raw=true)

   Now that I've successfully connected to the database, I checked to see what databases we have.

   ![screenshot_db](/2019AdventOfCyber/screenshots/day11/db.png?raw=true)

   We're interested in the *data* database, so let's select it. Next, let's see what tables we have in the database.

   ![screenshot_tables](/2019AdventOfCyber/screenshots/day11/tables.png?raw=true)

   Alright! Now we want to see all entries in the USER table.

   ![screenshot_users](/2019AdventOfCyber/screenshots/day11/users.png?raw=true)

   Awesome! We can see that user *admin* has the password *bestpassword*.

   > bestpassword

### Day 12: Elfcryption
### Day 13: Accumulate
### Day 14: Unknown Storage
### Day 15: LFI
### Day 16: File Confusion
### Day 17: Hydra-ha-ha-haa
### Day 18: ELF JS
### Day 19: Commands
### Day 20: Cronjob Privilege Escalation
### Day 21: Reverse Elf-ineering
### Day 22: If Santa, Then Christmas
### Day 23: LapLANd (SQL Injection)
### Day 24: Elf Stalk
### Day 25: Challenge-less