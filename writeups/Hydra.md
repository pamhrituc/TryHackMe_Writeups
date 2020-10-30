# Hydra

[Here's](https://tryhackme.com/room/hydra) the link to the TryHackMe room.

### Task 1: Hydra Introduction

#### What is Hydra?

Hydra is a brute force online password cracking program; a quick system login password 'hacking' tool.

We can use Hydra to run through a list and 'bruteforce' some authentication service. Imagine trying to manually guess someones password on a particular service (SSH, Web Application Form, FTP or SNMP) - we can use Hydra to run through a password list and speed this process up for us, determining the correct password.

Hydra has the ability to bruteforce the following protocols: Asterisk, AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP,  HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-POST, HTTP-PROXY, HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTPS-POST, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MYSQL, NCP, NNTP, Oracle Listener, Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, RDP, Rexec, Rlogin, Rsh, RTSP, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5, SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth, VNC and XMPP.

For more information on the options of each protocol in Hydra, read the official Kali Hydra tool page: https://en.kali.tools/?p=220

This shows the importance of using a strong password, if your password is common, doesn't contain special characters and/or is not above 8 characters, its going to be prone to being guessed. 100 million password lists exist containing common passwords, so when an out-of-the-box application uses an easy password to login, make sure to change it from the default! Often CCTV camera's and web frameworks use admin:password as the default password, which is obviously not strong enough.

#### Installing Hydra

If you're using Kali Linux, hydra is pre-installed. Otherwise you can download it here: https://github.com/vanhauser-thc/thc-hydra

If you don't have Linux or the right desktop environment, you can deploy your own Kali Linux machine with all the needed security tools. You can even control the machine in your browser! Do this with our Kali room - https://tryhackme.com/room/kali

1. Read the above and have Hydra at the ready.

   > No answer needed

### Task 2: Using Hydra

Deploy the machine attached to this task, then navigate to http://MACHINE_IP *(this machine can take up to 3 minutes to boot)*

MACHINE_IP: 10.10.139.250

#### Hydra Commands

The options we pass into Hydra depends on which service (protocol) we're attacking. For example if we wanted to bruteforce FTP with the username being user and a password list being passlist.txt, we'd use the following command:

`hydra -l user -P passlist ftp://10.10.139.250`

For the purpose of this deployed machine, here are the commands to use Hydra on SSH and a web form (POST method).

#### SSH

`hydra -l <usernam> -P <full path to pass> 10.10.139.250 -t 4 ssh

- -l: username
- -P: list of password
- -t: number of threads

#### Post Web Form

We can use Hydra to bruteforce web forms too, you will have to make sure you know which type of request its making - a GET or POST methods are normally used. You can use your browsers network tab (in developer tools) to see the request types, of simply view the source code.

Below is an example Hydra command to brute force a POST login form:

`hydra -l <username> -P <wordlist> 10.10.139.250 http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V

- -l => username
- -P => password list
- http-post-form => type of form (post)
- /login url => login page URL
- :username => form field where the username is entered
- ^USER^ => tells Hydra to use the username
- password => form field where the password is entered
- ^PASS^ => tells Hydra to use the password list supplied earlier
- Login => indicated to Hydra the Login failed message
- Login failed => login failure message that the form returns
- F=incorrect => if this word appears on the page, it's incorrect
- -V => verbose output

You should now have enough information to put this to practise and brute-force yourself credentials to the deployed machine!

1. Use Hydra to bruteforce molly's web password. What is flag 1?

   Command used: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.139.250 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V`

   It doesn't take Hydra more than 46 attempts to find molly's password. I then logged into the machine's login page using molly as username and the obtained password. After logging in, I get the flag.

   > THM{2673a7dd116de68e85c48ec0b1f2612e}

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

   Command used: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.139.250 -t 4 ssh` (Since we're trying to get molly's SSH password).

   Once Hydra finds molly's SSH password (*butterfly*), I logged into the machine as molly using ssh (`ssh molly@10.10.139.250`). I check what's in the current folder (a flag2.txt file) and use the `cat flag2.txt` command to see what's in the file.

   ![screenshot_molly_ssh](room_hydra/screenshots/molly_ssh.png?raw=true)

   > THM{c8eeb0468febbadea859baeb33b2541b}
