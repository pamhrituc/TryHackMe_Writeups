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
