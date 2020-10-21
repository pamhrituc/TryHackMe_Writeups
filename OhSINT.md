# OhSINT

This is the walkthrough for the [OhSINT room](https://tryhackme.com/room/ohsint) on TryHackMe.

### Task 1: OhSINT

All I have is a photo. I used exiftool to see what starting information I could get of the photo. (`exiftool WindowsXP.jpg`).

![screenshot_exiftool](/room_oshint/screenshots/exiftool.png?raw=true)

Notice that the Copyright value is OWoodflint. Next, I searched good ol' google to see what I could find on OWoodflint.

I found their twitter page (answering question 1),

![screenshot_twitter](/room_oshint/screenshots/twitter.png?raw=true)

their blog (answering questions 6 & 7, if you inspect the blog's HTML),

![screenshot_blog](/room_oshint/screenshots/blog.png?raw=true)

and their github (answering questions 2, 4 & 5).

![screenshot_github](/room_oshint/screenshots/github.png?raw=true)

1. What is this user's avatar of?

   > cat

2. What city is this person in?

   > London

3. What's the SSID of the WAP he connected to?

   The hint for question 2 mentions *BSSID + Wigle.net*. So, I accessed [Wigle.net](https://wigle.net/) and, plugging in the BSSID found OWoodflint's twitter page, I found the exact location of the WAP and its SSID. Yikes!

   ![screenshot_wigle](/room_oshint/screenshots/wigle.png?raw=true)

   *Notice the purple circle on the map and zoom in really really close on it.*

   > UnileverWiFi

4. What is his personal email address?

   > OWoodflint@gmail.com

5. What site did you find his email address on?

   > github

6. Where has he gone on holiday?

   > New York

7. What is this persons password?

   > pennYDr0pper.!
