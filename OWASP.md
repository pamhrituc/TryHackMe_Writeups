# OWASP Top 10

![screenshot_owasp]()


[Here](https://tryhackme.com/room/owasptop10) is the link to the TryHackMe room.

In this write-up, I will include only the answers to the questions and how I've gotten that answer. You can find the explanations on the vulnerabilities in the room.

### Introduction

Learn one of the OWASP vulnerabilities every day for 10 days in a row. A new task will be revealed every day, where each task will be independent from the previous one. These challenges will cover each OWASP topic:


    Day 1) Injection

    Day 2) Broken Authentication

    Day 3) Sensitive Data Exposure

    Day 4) XML External Entity

    Day 5) Broken Access Control

    Day 6) Security Misconfiguration

    Day 7) Cross-site Scripting

    Day 8) Insecure Deserialization

    Day 9) Components with Known Vulnerabilities

    Day 10) Insufficent Logging & Monitoring


The challenges are designed for beginners and assume no previous knowledge of security.

1. Read the above.

   > No answer needed

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
### Day 3: Sensitive Data Exposure
### Day 4: XML External Entity
### Day 5: Broken Access Control
### Day 6: Security Misconfiguration
### Day 7: Cross-site Scripting
### Day 8: Insecure Deserialization
### Day 9: Components with Known Vulnerabilities
### Day 10: Insufficient Logging & Monitoring
