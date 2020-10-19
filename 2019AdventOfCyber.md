# Advent of Cyber

The link to the room can be found [here](https://tryhackme.com/room/25daysofchristmas). This writeup contains the solutions of the 2019 advent event on TryHackMe.

### Day 1: Inventory Management

Machine IP: 10.10.51.171

1. What is the name of the cookie used for authentication?

   First things first, after iaccessing the login page of the website, I created an account. After logging creating an account, I logged in and checked the cookies value from the Storage tab.

   ![screenshot_authid](/2019AdventOfCyber/screenshots/day01/authid.png?raw=true)

   > authid

2. If you decode the cookie, what is the value of the fixed part of the cookie?

   For this part, I used [Cyberchef](https://gchq.github.io/CyberChef/) to decode the cookie. As you can see, after decoding the cookie (from base64), the string is the username concatinated with the string *v4er9ll1!ss*.

   > v4er9ll1!ss

3. After accessing his account, what did the user mcinventory request?

   To access mcinventory's account, simply encode a new authod using base64, with the fixed part of the cookie and the string *mcinventory*. Change the value of authid with the encoded string. Reload the page and you've accessed mcinventory's account.

   ![screenshot_mcinventory](/2019AdventOfCyber/screenshots/day01/mcinventory.png?raw=true)

   > firewall

### Day 2: Arctic Forum

Machine IP: 10.10.218.103

1. What is the path of the hidden page?

   To answer this question, and generally to find hidden pages on websites, I used gobuster. Command: `gobuster dir -u http://10.10.218.103:3000/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt`

   ![screenshot_gobuster](/2019AdventOfCyber/screenshots/day02/gobuster.png?raw=true)

   > /sysadmin

2. What is the password you found?

   Upon accessing the hidden page on the webserver and checking the source code, I found this comment:

   ![screenshot_source](/2019AdventOfCyber/screenshots/day02/source.png?raw=true)

   So, a quick google search led me to their [github page](https://github.com/ashu-savani/arctic-digital-design), where I found the admin login credentials.

   ![screenshot_credentials](/2019AdventOfCyber/screenshots/day02/credentials.png?raw=true)

   > defaultpass

3. What do you have to take to the 'partay'?

   After using the credentials found on the github page, you can find what you have to bring to the 'partay'.

   ![screenshot_BYOE](/2019AdventOfCyber/screenshots/day02/BYOE.png?raw=true)

   > Eggnog

### Day 3: Evil Elf

For today's challenge we have the *Evil Elf.pcap* file. I opened this with wireshark.

1. Whats the destination IP on packet number 998?

   For this question, just find packet 998 and check its destination IP address.

   ![screenshot_packet_998](/2019AdventOfCyber/screenshots/day03/packet_998.png?raw=true)

   > 63.32.89.195

2. What item is on the Christmas list?

   For this question, filter out any packets that aren't *telnet*. We have 3 telnet packets, out of which observe one of these contains the following:

   ![screenshot_telnet](/2019AdventOfCyber/screenshots/day03/telnet.png?raw=true)

   > ps4

3. Crack buddy's password!

   The second *telnet* packet contains the `cat /etc/shadow` command, meaning that what is returned is the usernames and the hashed passwords. If we check the third *telnet* packet, we can see that this packet indeed contains the users and the hashed passwords. Now all that I need to do is crack the hash. I used hashcat to do this.

   ![screenshot_shadow](/2019AdventOfCyber/screenshots/day03/shadow.png?raw=true)

   Command: `hashcat -m 1800 buddy_hash.txt /usr/share/wordlists/rockyou.txt`

   Soon enough, hashcat cracks the hash and displays the password.

   > rainbow

### Day 4: Training

Machine IP: 10.10.89.60

What we are given, other than tha machine's IP is the following information:

`ssh mcsysadmin@10.10.89.60`

username: mcsysadmin

password: bestelf1234

1. How many visible files are there in the home directory(excluding ./ and ../)?

   Command: `ls`

   > 8

2. What is the content of file5?

   Command: `cat`

   > recipes

3. Which file contains the string ‘password’?

   Command: `grep -l -e "password" -f *`

   > file6

4. What is the IP address in a file in the home folder?

   Command: `cat * | grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"`

   > 10.0.0.05

5. How many users can log into the machine?

   Command: `ls -la /home`

   > 3

6. What is the sha1 hash of file8?

   Command: `sha1sum file8`

   > fa67ee594358d83becdd2cb6c466b25320fd2835

7. What is mcsysadmin’s password hash?

   Command: `find / 2>>/dev/null | grep "shadow.bak"`

   > $6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/

### Day 5: Ho-Ho-Hosint

1. What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019)

   For today's challenge, we are given an image of the grinch. I used `exiftool` to get the image's metadata.

   ![screenshot_metdata](/2019AdventOfCyber/screenshots/day05/metadata.png?raw=true)

   *JLolax1* is the creator of the image, a quick google search of the creator led me to the creator's twitter page.

   ![screenshot_twitter](/2019AdventOfCyber/screenshots/day05/twitter.png?raw=true)

   On Lola's page we can find the answers to this question, as well as questions 2 and 3.

   > December 29, 1900

2. What is Lola's current occupation?

   > Santa's Helper

3. What phone does Lola make?

   > iPhone X

4. What date did Lola first start her photography? Format: dd/mm/yyyy

   For question 4 and 5, I accessed Lola's wordpress page using the link found in her Twitter bio. Next, using the [WayBack Machine](https://web.archive.org/), I went through some of the captures until I found this:

   ![screenshot_wayback](/2019AdventOfCyber/screenshots/day05/wayback.png?raw=true)

   There's the answer for this question!

   > 23/10/2014

5. What famous woman does Lola have on her web page?

   This is the woman whose identity we're looking for.

   ![screenshot_woman](/2019AdventOfCyber/screenshots/day05/woman.png?raw=true)

   Doing a quick reverse search on the image reveals that she's Ada Lovelace.

   ![screeshot_ada](/2019AdventOfCyber/screenshots/day05/ada.png?raw=true)

   > Ada Lovelace

### Day 6: Data Elf-iltration

Another day, another pcap file. Just like in day3, I used wireshark to open and analyze *holidaythief.pcap*.

1. What data was exfiltrated via DNS?

   First, after opening the *holidaythief.pcap* using wireshark, I used the filter to view only DNS packets. This caught my eye.

   ![screenshot_dns](/2019AdventOfCyber/screenshots/day06/dns.png?raw=true)

   I used [CyberChef](https://gchq.github.io/CyberChef/) to decrypt the subdomain and got what I was looking for.

   ![screenshot_cyberchef](/2019AdventOfCyber/screenshots/day06/cyberchef.png?raw=true)

   > Candy Cane Serial Number 8491

2. What did Little Timmy want to be for Christmas?

   Going though the HTTP packets, I noticed a .zip file.

   ![screenshot_zip](/2019AdventOfCyber/screenshots/day06/zip.png?raw=true)

   So, I exported the christmasfiles.zip file and tried to unzip it.

   ![screenshot_password](/2019AdventOfCyber/screenshots/day06/password.png?raw=true)

   It asks for a password, which I don't have. I went through the HTTP packets in wireshark to see if it was there. It wasn't. So that left me to crack it. I used *fcrackzip* to do so. Command: `fcrackzip -b --method 2 -D -p /usr/share/wordlists/rockyou.txt -v christmaslists.zip` (the -b flag means use brute force, the --method means use the method number and not the default one, the -D flag will tell fcrackzip to use dictionary mode, followed by the file which contains the list of possible passwords, -v verifies the password is correct and finally the zip file to crack).

   ![screenshot_fcrackzip](/2019AdventOfCyber/screenshots/day06/fcrackzip.png?raw=true)

   Now, that I have the password, I was able to unzip the file and see what Little Timmy wants to be for Christmas.

   ![screenshot_christmas_lists](/2019AdventOfCyber/screenshots/day06/christmas_lists.png?raw=true)

   > PenTester

3. What was hidden within the file?

   Another file of interest that appeared among the HTTP packets was TryHackMe.jpg. I exported it. `strings TryHackMe.jpg` revealed nothing of interest, so I used steghide (`steghide extract -sf TryHackMe.jpg`). The command wrote the extracted data to christmasmonster.txt, which contained a nice poem and the answer to this question.

   ![screenshot_steghide](/2019AdventOfCyber/screenshots/day06/steghide.png?raw=true)

   > RFC527

### Day 7: Skilling Up

Machine IP: 10.10.26.123

1. how many TCP ports under 1000 are open?

   To answer this question, I simply performed an nmap scan on the machine. Command: `nmap -sV -O 10.10.26.123`. The -sV flag is for detecting the versions of the services run on each port, the -O flag is for enabling OS detection. [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/nmap_scan_results/day7_skillingup.log). Using the scan results, I could answer questions 2 and 3 as well.

   > 3

2. What is the name of the OS of the host?

   > Linux

3. What version of SSH is running?

   > 7.4

4. What is the name of the file that is accessible on the server you found running?

   For this question, I accessed the webserver that in run on the deployed machine, on port 999 (information from the nmap scan results). Once accessed, I could see the name of the file.

   ![screenshot_file](/2019AdventOfCyber/screenshots/day07/file.png?raw=true)

   > interesting.file

### Day 8: SUID Shenanigans

Deploy and SSH into the machine.

Username: holly

Password: tuD@4vt0G\*TU


Machine IP: 10.10.68.225

Scanned using command: `nmap 10.10.68.225 -p 1-65535`

[Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/nmap_scan_results/day8_suid.log)

1. What port is SSH running on?

   > 65534

Logged into machine using SSH: `ssh holly@10.10.68.225 -p 65534`

2. *Find* and run a file as *igor*. Read the file /home/igor/flag1.txt

   Logged into machine using SSH: `ssh holly@10.10.68.225 -p 65534`
   Find command that searches for files that igor owns with read permission, and execute ls: `find / -user igor -perm -4000 -exec ls -ldb {} \; 2>/dev/null`
   Find command that lets us execute cat on the specified file: `find /home/igor/flag1.txt -exec cat '{}' \;`

   > THM{d3f0708bdd9accda7f937d013eaf2cd8}

3. Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?

   For this question, we're going to start by running this command: `find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null`. This command will find all files owned by root, with read permissions. Among the found files, I saw this:

   ![screenshot_find](/2019AdventOfCyber/screenshots/day08/find.png?raw=true)

   system-control

   This binary allows us to use `su` as root.

   ![screenshot_su](/2019AdventOfCyber/screenshots/day08/su.png?raw=true)

   Now that we're root, we can view the contents of /root/flag2.txt

   > THM{8c8211826239d849fa8d6df03749c3a2}

4. If you've finished the challenge and want more practise, checkout the Privilege Escalation Playground room created by SherlockSec: https://tryhackme.com/room/privescplayground

   > No answer needed

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

   First things first, nmap scan the target. The first command I used was `nmap -sV 10.10.24.100`, but it seemed the target was blocking the ping probes, so I used the -Pn flag (`nmap -Pn -sV 10.10.24.100`) [Scan results](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/nmap_scan_results/day13_accumulate.log)

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

1. Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)

   Command used: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.175.104 http-post-form "/login:username=^USER^&password=^PASS^:F=Your username or password is incorrect" -V` (It took more then the first 30 passwords from the rockyou.txt file, so let hydra run for a while.). After hydra finds the password, log into the website using *molly* as the username and the password hydra found. The flag will be displayed after logging in.

   > THM{2673a7dd116de68e85c48ec0b1f2612e}

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

   Command used: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.175.104 -t 4 ssh`. Hydra will return the password, then just log into the deployed machine using SSH, with *molly* as username and the password hydra found. 

   > THM{c8eeb0468febbadea859baeb33b2541b}

### Day 18: ELF JS

1. What is the admin's authid cookie value?

   Accessing the deplayed machine's IP on port 3000 took me to a login page. So, I registered to the website and logged in with the account I made. After loggin in, I checked if there was an XSS vulnerability (as expected, there was).

   So, to get the admin cookie, I posted the following message:

   ![screenshot_message](/2019AdventOfCyber/screenshots/day18/message.png?raw=true)

   This will get all users that load the page to send their cookie to me.

   Next, I opened a *netcat* connection listening on the port inside a while loop and waited. Sure enough, when the admin logged in, their cookie was displayed in the console.

   ![screenshot_nc](/2019AdventOfCyber/screenshots/day18/nc.png?raw=true)

   > 2564799a4e6689972f6d9e1c7b406f87065cbf65

### Day 19: Commands

First things first, I accessed the deplayed machine's website (10.10.51.185:3000). This was the website's contents:

![Screenshot_cookie](/2019AdventOfCyber/screenshots/day19/cookie.png?raw=true)

Next, the task description mentions that '*McSkidy actually found something interesting on the /api/cmd endpoint.*'. Interesting. I accessed http:10.10.51.185:3000/api/cmd and this is what it returns:

![screenshot_cmd](/2019AdventOfCyber/screenshots/day19/cmd.png?raw=true)

Alright. But the file exists for sure. I supplied the `ls` parameter and this is what I got:

![screenshot_ls](/2019AdventOfCyber/screenshots/day19/ls.png?raw=true)

Nice! Now we're getting somewhere. We can do command injection on this webserver by supplying the command we want to execute after /api/cmd. Since we know the flag is in a file named *user.txt*, we're gonna execute the `find -name user.txt` command in order to find where the file is.

Before executing the commands, they need to be URL encoded. We have:

- %20 => space
- %2F => "/"

![screenshot_find](/2019AdventOfCyber/screenshots/day19/find.png?raw=true)

Now that we have the location of the file, all we need to to is execute the `cat` command and we have the flag.

![screenshot_flag](/2019AdventOfCyber/screenshots/day19/flag.png?raw=true)

1. What are the contents of the user.txt file?

   > 5W7WkjxBWwhe3RNsWJ3Q

### Day 20: Cronjob Privilege Escalation

1. What port is SSH running on?

   This question can be answered simply by running an nmap scan on the target's machine (`nmap -sV 10.10.158.199`).

   > 4567

2. Crack sam's password and read flag1.txt

   For this one, I used hydra (`hydra -l sam -P /usr/share/wordlists/rockyou.txt 10.10.158.199 -t 4 ssh -s 4567`). Once hydra gave me the password, I logged into the machine through ssh (`ssh sam@10.10.158.199 -p 4567`). After I logged in, I could easily view the flag1.txt file.

   > THM{dec4389bc09669650f3479334532aeab}

3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?

   Running `cronjob -l` shows us that user *sam* doesn't have any cronjobs running. Doing an `ls -la /home` shows us an interesting folder owned by *root*. Doing an `ls -la /home/scripts` shows us a file named *clean_up.sh*. Smells like a cronjob to me.

   ![screenshot_home](/2019AdventOfCyber/screenshots/day20/home.png?raw=true)

   ![screenshot_scripts](/2019AdventOfCyber/screenshots/day20/scripts.png?raw=true)

   To find where flag2 is, I ran the `find / -name "flag2*" 2>>/dev/null` command. After finding the location of flag2, I added the following command to clean_up.sh: `chmod 404 /home/ubuntu/flag2.txt`, which gives other users reading permissions to the file. After waiting a minute, I could see the contents of flag2.txt

   > THM{b27d33705f97ba2e1f444ec2da5f5f61}

### Day 21: Reverse Elf-ineering

*The questions below are regarding the challenge1 binary file.*

I'll admit, I've never done reverse engineering before. So this task was a real learning experience for me. I followed the guide linked in the challenge, [here](https://drive.google.com/file/d/1maTcdquyqnZCIcJO7jLtt4cNHuRQuK4x/view). It was really helpful.

As shown in the guide, I downloaded and installed [radare2](https://rada.re/n/radare2.html). I ran challenge1, which didn't print anything to the console, so next, I ran the following command: `r2 -d challenge1`. This command opens the challenge1 binary in debugging mode. Run the `aa` command, to tell r2 to analyze the program. Next, to examine the assembly code, I typed in the following command: `pdf @ main` (pdf = print disassembly function). Running the command on the challenge1 binary gave me this:

![screenshot_r2_main](/2019AdventOfCyber/screenshots/day21/r2_main.png?raw=true)

Now, we just gotta check the assembly instructions to get the answers to the three questions.

1. What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?

   > 1

2. What is the value of eax when the imull instruction is called?

   > 6

3. What is the value of local_4h before eax is set to 0?

   > 6

### Day 22: If Santa, Then Christmas

Day 22 seems to be similar to day 21. I ran if2, then I used the command `r2 -d if2` to open the if2 binary in debugging mode. Next, I ran `aa` for *r2* to analyze the program, then I ran `pdf @ main` to examine the assembly code.

What is different in this challenge than day 21's, is that now we're dealing with `if` statements, which in assembly code translates to compare and jump instructions.

![screenshot_r2_if](/2019AdventOfCyber/screenshots/day22/r2_if.png?raw=true)

In this case, after local_8h and local_4h are assigned the values 8 and 2 respectively, local_8h's value is moved into the eax register. Then the value currently in eax is compared to the value of local_4h. Following the `cmp` instruction, we have the `jle` instrution, meaning the jump will be done if the first value is less or equal to the second value, in more detail, if the value of eax is less than or equal to the value of var_4h, the jump is done. Since the condition isn't true, the addition is done (the value 1 is added to the value of var_8h), and the jump after that is done.

I've written the equivalent [c code](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/2019AdventOfCyber/day22/if2.c) for better understanding.

1. what is the value of local_8h before the end of the main function?

   > 9

2. what is the value of local_4h before the end of the main function?

   > 2

### Day 23: LapLANd (SQL Injection)

Machine IP: 10.10.249.7

1. Which field is SQL injectable? Use the input name used in the HTML code.

   For this question, I accessed the website using the deployed machine's IP address. Then I checked the HTML code using *Inspect Element*. Since we are directed to the login page, we have 2 fields: E-mail and password. For the names of the fields check the HTML code.

   > log_email

2. What is Santa Claus' email address?

   To get Santa Claus' email address, I used sqlmap. As a general idea, we're looking for a table that contains E-mails and passwords, which will most likely be found in a table named users.

   Command #1: `sqlmap --batch -u http://10.10.249.7/ --forms --dbs`

   Databases returned:

   ![screenshot_dbs](/2019AdventOfCyber/screenshots/day23/dbs.png?raw=true)

   Now, we wanna dive in deeper into a database (or databases) to find the *users* table. The social table seems like a good start. Command used: `sqlmap --batch -u http://10.10.249.7/ --forms -D social --tables`

   Tables returned:

   ![screenshot_tables](/2019AdventOfCyber/screenshots/day23/tables.png?raw=true)

   Observe that one of the tables is named *users*. The information we're looking for is here. I used this command to dump it: `sqlmap --batch -u http://10.10.249.7/ --forms -D social -T users --dump`

   ![screenshot_users](/2019AdventOfCyber/screenshots/day23/users.png?raw=true)

   > bigman@shefesh.com
   
3. What is Santa Claus' plaintext password?

   I used hashcat to find the password. Command: `hashcat -m 0 "f1267830a78c0b59acc06b05694b2e28" /usr/share/wordlists/rockyou.txt`

   > saltnpepper

4. Santa has a secret! Which station is he meeting Mrs Mistletoe in?

   I logged into the forum using Santa's E-mail address and password obtained in the previous 2 questions. Then I went through the messages to find what what I was looking for.

   ![screenshot_messages](/2019AdventOfCyber/screenshots/day23/messages.png?raw=true)

   Yikes!

   > Waterloo

5. Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/

   Just like in day 18, I opened a connection in nc, uploaded the php-reverse-shell.phtml file and voila. We're in.

   ![screenshot_flag](/2019AdventOfCyber/screenshots/day23/flag.png?raw=true)

   > THM{SHELLS_IN_MY_EGGNOG}

### Day 24: Elf Stalk
### Day 25: Challenge-less

1. Complete another room on TryHackMe.

   No answer needed
