# OWASP Top 10

![screenshot_owasp](/room_owasp/screenshots/owasp.png?raw=true)


[Here](https://tryhackme.com/room/owasptop10) is the link to the TryHackMe room.

In this write-up, I will include only the answers to the questions and how I've gotten that answer. You can find the explanations on the vulnerabilities in the room.

### Introduction

Learn one of the OWASP vulnerabilities every day for 10 days in a row. A new task will be revealed every day, where each task will be independent from the previous one. These challenges will cover each OWASP topic:


- [Day 1) Injection](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-1-injection)
- [Day 2) Broken Authentication](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-2-broken-authentication)
- [Day 3) Sensitive Data Exposure](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-3-sensitive-data-exposure)
- [Day 4) XML External Entity](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-4-xml-external-entity)
- [Day 5) Broken Access Control](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-5-broken-access-control)
- [Day 6) Security Misconfiguration](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-6-security-misconfiguration)
- [Day 7) Cross-site Scripting](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-7-cross-site-scripting)
- [Day 8) Insecure Deserialization](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-8-insecure-deserialization)
- [Day 9) Components with Known Vulnerabilities](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-9-components-with-known-vulnerabilities)
- [Day 10) Insufficent Logging & Monitoring](https://github.com/pamhrituc/TryHackMe_Writeups/blob/master/OWASP.md#day-10-insufficient-logging--monitoring)


The challenges are designed for beginners and assume no previous knowledge of security.

### Day 1: Injection

Deployed machine IP: 10.10.41.189

1. What strange text file is in the website root directory?

   Command: `ls`

   ![screenshot_ls](/room_owasp/screenshots/day01/ls.png?raw=true)

   > drpepper.txt

2. How many non-root/non-service/non-daemon users are there?

   I check the number of users in the */home* directory.

   ![screenshot_home](/room_owasp/screenshots/day01/home.png?raw=true)

   > 0

3. What user is this app running as?

   Use the `whoami` command.

   ![screenshot_whoami](/room_owasp/screenshots/day01/whoami.png?raw=true)

   > www-data

4. What is the user's shell set as?

   Check the */etc/passwd* file.

  ![screenshot_shell](/room_owasp/screenshots/day01/shell.png?raw=true)

  > /usr/sbin/nologin
 
5. What version of Ubuntu is running?

   Command: `lsb_release -a`

   ![screenshot_release](/room_owasp/screenshots/day01/release.png?raw=true)

   > 18.04.4

6. Print out the MOTD.  What favorite beverage is shown?

   I had to search Google for this one. MOTD stands for Message Of The Day, and is a directory (`/etc/update-motd.d`). More on it [here](http://manpages.ubuntu.com/manpages/eoan/en/man5/update-motd.5.html)

   ![screenshot_motd_1](/room_owasp/screenshots/day01/motd_1.png?raw=true)

   ![screenshot_motd_2](/room_owasp/screenshots/day01/motd_2.png?raw=true)

   > DR PEPPER

### Day 2: Broken Authentication

Machine IP: 10.10.50.243

1. What is the flag that you found in darren's account?

   For today's task, all I had to do was follow the steps the task describes.

   First, I made an account as darren, with a slight modification to the username.

   ![screenshot_darren](/room_owasp/screenshots/day02/darren.png?raw=true)

   Notice the space in front of "darren". After registering as darren-not-darren, I logged in using my registration credentials and voila, we have the flag found in darren's account.

   ![screenshot_flag](/room_owasp/screenshots/day02/flag.png?raw=true)

   > fe86079416a21a3c99937fea8874b667

2. Now try to do the same trick and see if you can login as arthur.

   I did the same thing for arthur as for darren.

   > No answer needed

3. What is the flag that you found in arthur's account?

   > d9ac0f7db4fda460ac3edeb75d75e16e

### Day 3: Sensitive Data Exposure

Machine IP: 10.10.156.59

1. Have a look around the webapp. The developer has left themselves a note indicating that there is sensitive data in a specific directory.

   What is the name of the mentioned directory?

   Going to the source code of the login page, I found the folder */assets*

   > /assets

2. Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?

   I went to the directory and this is what I found:

   ![screenshot_assets](/room_owasp/screenshots/day03/assets.png?raw=true)

   Seems *webapp.db* is the file of interest. I downloaded it to my machine.

   > webapp.db

3. Use the supporting material to access the sensitive data. What is the password hash of the admin user?

   I just followed the supporting material to get the password hash of the admin user.

   ![screenshot_commands](/room_owasp/screenshots/day03/commands.png?raw=true)

   > 6eea9b7ef19179a06954edd0f6c05ceb

4. Crack the hash. What is the admin's plaintext password?

   I used hashcat for this one. Command: `hashcat -m 0 "6eea9b7ef19179a06954edd0f6c05ceb" /usr/share/wordlists/rockyou.txt`

   > qwertyuiop

5. Login as the admin. What is the flag?

   Just log into the deployed machine through the login page (Username: admin; Password: qwertyuiop)

   ![screenshot_flag](/room_owasp/screenshots/day03/flag.png?raw=true)

   > THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}

### Day 4: XML External Entity
### Day 5: Broken Access Control
### Day 6: Security Misconfiguration
### Day 7: Cross-site Scripting
### Day 8: Insecure Deserialization
### Day 9: Components with Known Vulnerabilities
### Day 10: Insufficient Logging & Monitoring
