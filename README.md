**A Note for the Reader**: The final version of this project that was deployed to an EC2 instance was tweaked quite heavily and is not hosted online. This project got increasingly difficult to maintain due to Instagram's strict policies against automated posting.

**Future plans**: To build a scalable system for short form videos following a similar idea of content redistribution (with credit) across multiple platforms using the knowledge I have acquired since. This project is currently in the R&D phase.

---

# Reddit to Instagam Automation
This repository consist of two different ways to automate the process of downloading posts from Reddit and uploading them to Instagram as posts. 

Both the methods use Selenium which is an open source web based automation tool. 
* The first one uses an AppleScript that is called through python, which works only with MacOS, which may be obvious. This is the primary method I use.
* The second one uses pyautogui which can be configured to work with any system with minor edits to the code. 

Read the requirements.txt for both the different methods and check out the [examples](https://github.com/Vaansh/Reddit-to-Instagam-Automation/tree/master/resize%20image%20examples) of the size imaging to find out how the algorithm to resize the image works.

Python version used: 3.7.7
OS used: macOS Catalina (Version 10.15.6)
