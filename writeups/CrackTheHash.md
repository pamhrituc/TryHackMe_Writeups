# Crack the hash

[Room](https://tryhackme.com/room/crackthehash)

### Task 1: Level 1

Can you complete the level 1 tasks by cracking the hashes?

1. 48bb6e862e54f2a795ffc4e541caed4d

   The hint says this is an md5 hash. Command to crack the hash: `hashcat -m 0 hash1_1.txt /usr/share/wordlists/rockyou.txt --show`

   > easy

2. CBFDAC6008F9CAB4083784CBD1874F76618D2A97

   The hint says this is a sha.. hash. Since hashcat can crack only 4 types of sha hashes, I tried all of them until one was successful. Turns out it was a SHA1 hash. Command to crack the hash : `hashcat -m 100 hash1_2.txt /usr/share/wordlists/rockyou.txt --show`

   > password123

3. 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

   The hint says this is a sha.. hash. Same strategy used in the previous question. Turns out it was a SHA256 hash. Command used to crack the hash: `hashcat -m 1400 hash1_3.txt /usr/share/wordlists/rockyou.txt --show`

   > letmein

4. $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

   The hint says this is a bcrypt hash. Command used to crack the hash: `hashcat -m 3200 hash1_4.txt /usr/share/wordlists/rockyou.txt`

   > bleh

5. 279412f945939ba78ce0758d3fd83daa

   The hint says this is a md4 hash. I tried using the following command used to crack the hash: `hashcat -m 900 hash1_5.txt /usr/share/wordlists/rockyou.txt`, yet hashcat didn't find the password in the rockyou.txt file, so I used the following online tool to crack the hash: [link](https://md5decrypt.net/en/Md4/).

   > Eternity22

### Task 2: Level 2

This task increases the difficulty. All of the answers will be in the classic [rock you](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) password list.

You might have to start using hashcat here and not online tools. It might also be handy to look at some example hashes on [hashcats page](https://hashcat.net/wiki/doku.php?id=example_hashes).

1. Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

   It seems this is a SHA256 hash. Command used to crack the hash: `hashcat -m 1400 hash2_1.txt /usr/share/wordlists/rockyou.txt`

   > paule

2. Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

   Salt: aReallyHardSalt

   Rounds: 5

   The hint says this is a NTLM hash. Command used to crack the hash: `hashcat -m 1000 hash2_2.txt /usr/share/wordlists/rockyou.txt`

   > n63umy8lkf4i

3. Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

   Salt: tryhackme

   This one seems to be a SHA-512(Unix) hash. Command used to crack the hash: `hashcat -m 1800 hash2_3.txt /usr/share/wordlists/rockyou.txt`

   > waka99

4. Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

   Salt: tryhackme

   The hint says this one is a HMAC-SHA1 hash. Command used to crack the hash: `hashcat -m 160 hash2_4.txt /usr/share/wordlists/rockyou.txt`.

   > 481616481616
