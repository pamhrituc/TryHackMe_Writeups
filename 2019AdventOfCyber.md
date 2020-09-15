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

I wrote a script that resolves this challenge. This script can be found in the [2019AdventOfCyber] (https://github.com/pamhrituc/TryHackMe_Writeups/2019AdventOfCyber/day9_requests.py).

First, the script accesses the IP address, 10.10.169.100. Next, the response is saved in the res variable, which contains the JSON object. Then, the IP address is accessed iteratively, until the value of the `next` key in the response is *end*. The flag is built with every iteration, adding the value of the `value` key to the `flag` variable until the *end* value is reached.
