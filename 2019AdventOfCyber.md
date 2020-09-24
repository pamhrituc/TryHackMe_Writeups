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

1. What is the md5 hashsum of the encrypted note1 file?

   After downloading the *tosend.zip* file, I used the `unzip tosend.zip` command to obtain its contents: note1.txt.gpg, note2_encrypted.txt and private.key. To get the mdsum of the encrypted note1 file, I used the following command: `md5sum note1.txt.gpg`

   > 24cf615e2a4f42718f2ff36b35614f8f

2. Where was elf Bob told to meet Alice?

   For this question, we need to decrypt note1.txt.gpg. For this I used the `gpg -d note1.txt.gpg` command (gpg, or GNU Privacy Guard, is an OpenPGP encryption and signing tool. The -d flag is specified for decyption). When prompted for a password, I used the hint given by TryHackMe (*25daysofchristmas*) and obtained the follwoing message: *I will meet you outside Santa's Grotto at 5pm!*

   > Santa's Groto

3. Decrypt note2 and obtain the flag!

   To decrypt note2 I used the following command: `openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out note2.txt`, entered the password given as a hint (*hello*). The flag was found in the contents of note2.txt.

   openssl a command line tool used for various cryptographic functions of OpenSSL's **crypto** library. The *rsautl* flag represents the RSA utility for signing, verification, encryption and decryption. The *-decrypt* flag is specified for decrypting. The *-in* flag is followed by the input file and the *-out* flag by the name of the output file.

   > THM{ed9ccb6802c5d0f905ea747a310bba23}

### Day 13: Accumulate

1. A web server is running on the target. What is the hidden directory which the website lives on?

   First things first, nmap scan the target. The first command I used was `nmap -sV 10.10.24.100`, but it seemed the target was blocking the ping probes, so I used the -Pn flag (`nmap -Pn -sV 10.10.24.100`) [Scan results]()

   According to the scan results, we're dealing with a webserver (http runs on port 80), so let's scan using gobuster (`gobuster dir -u http://10.10.24.100 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt`). Now, we just wait for the results.

   ![screenshot_gobuster](/2019AdventOfCyber/screenshots/day13/gobuster.png?raw=true)

   The first result gobuster returns is */retro*. If we access *http://10.10.24.100/retro*, the browser will display this page.

   ![screenshot_retro](/2019AdventOfCyber/screenshots/day13/retro.png?raw=true)

   > /retro

2. Gain initial access and read the contents of user.txt

   The page seems to be a blog. Going through a couple of posts, I found this:

   ![screenshot_creds](/2019AdventOfCyber/screenshots/day13/creds.png?raw=true)

   Yikes! Seems the author left their credentials out in the open. Using these, we can log into his system. After a little bit of research, I used the *remmina* tool to get initial access to the machine. Use the RDP protocol, type in the target machine's IP address and log in with *wade* as username and *parzival* as the password. Once we're in, notice that the user.txt file is located on the Desktop.

   > THM{HACK_PLAYER_ONE}

### Day 14: Unknown Storage

1. What is the name of the file you found?

   Based on the description of this task, we simple need to access 'http://advent-bucket-one.s3.amazonaws.com/'. The file name appears in plaintext.

   ![screenshot_bucket](/2019AdventOfCyber/screenshots/day14/bucket.png?raw=true)

   > employee_names.txt

2. What is in the file?

   To access the contents of the file, simply append it to the link of the bucket.

   ![screenshot_file](/2019AdventOfCyber/screenshots/day14/file.png?raw=true)

   > mcchef

### Day 15: LFI

1. What is Charlie going to book a holiday to?

   This question can be answered by simply accessing the machine's IP address in a web browser.

   ![screenshot_notes](/2019AdventOfCyber/screenshots/day15/notes.png?raw=true)

   > Hawaii

2. Read /etc/shadow and crack Charlies password.

   Checking the source code of the page, I found this.

   ![screenshot_script](/2019AdventOfCyber/screenshots/day15/script.png?raw=true)

   Seems the page is dynamically loading the notes from the *views/notes/* directory. Let's change the request using Burpsuite. Make sure Burpsuite intercepts the request. Once that is done, go to the Proxy/Intercept tab in Burpsuite and edit the first line of the request so it looks like this:

   ![screenshot_burpsuit](/2019AdventOfCyber/screenshots/day15/burpsuite.png?raw=true)

   Then Forward it to the browser and voila!

   ![screenshot_shadow](/2019AdventOfCyber/screenshots/day15/shadow.png?raw=true)

   We have the contents of */etc/shadow*. Now all we have to do use hashcat to get the password. I saved charlie's password in a .txt file and ran the command: `hashcat -m 1800 charlie.txt /usr/share/wordlists/rockyou.txt`. The *-m* flag is followed by the hash-type we want to check against (check hashcat's manual pages for the numbers). In this case, since we want a UNIX password, we'll use the SHA-512 (UNIX) hash. */usr/share/wordlists/rockyou.txt* is the file containing a list of command passwords.

   Now we run the command and wait. hashcat returns the password soon enough.

   ![screenshot_password](/2019AdventOfCyber/screenshots/day15/password.png?raw=true)

   > password1

3. What is flag1.txt?

   To find the contents of flag1.txt, we will log into charlie's machine using ssh (username: charlie, password: password1, found by solving the previous question). A quick `ls` and `cat flag1.txt` reveals the contents of flag1.txt

   > THM{4ea2adf842713ad3ce0c1f05ef12256d}

### Day 16: File Confusion

Just as mentioned in the task, I wrote a python script to solve all three of the questions. The script is [here](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/day16/day16_file_confusion.py).

I used the *zipfile* library to extract the zip files, going through each extracted zip file from the original zip file, I extracted the files, then check if it contains the password and if its version number is 1.1.

1. How many files did you extract(excluding all the .zip files)

   > 50

2. How many files contain Version: 1.1 in their metadata?

   > 3

3. Which file contains the password?

   > dL6w.txt

### Day 17: Hydra-ha-ha-haa
### Day 18: ELF JS
### Day 19: Commands
### Day 20: Cronjob Privilege Escalation
### Day 21: Reverse Elf-ineering
### Day 22: If Santa, Then Christmas
### Day 23: LapLANd (SQL Injection)
### Day 24: Elf Stalk
### Day 25: Challenge-less
