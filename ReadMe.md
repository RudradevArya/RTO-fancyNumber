Now I get the programming humour memes
>How to Automate a task by putting 2 hours of work in it which could have been done with 15 minutes of manual labour


# Tasklist
- [x] Understand Digital root 
  * ex - 4232 = 4+2+3+2 = 11 = 1+1 = 2
- [x] Get all available fancy numers
- [x] Sort by only digits and their prices
- [x] Sort by only digital root and their prices
- [x] ✨**ENJOY** - ✨


---
---

# What this repo is?
### Some background
1. going to buy a new vehicle soon and family wanted a fancy number plate with digitalRoot as 6 
2. so worked on the **digitalRoot.py**

3. then after research found out that there are limited number of fancy numbers which are auctioned 
therefore went to [this guide](https://onlineservicess.in/fancy-number-for-vehicle-in-pune/) where i could see the available fancy numbers
4. then copied all the current numbers in the fancyNumList.txt
5. using regex `match = re.search(r"MH12VX(\d{4})\s+(\d{4,5})", line)` I sorted the digits and the prices from the raw data into a new file **sortedNum.txt**
6. Then using the regex `match = re.search(r"(\d{4})\t(\d{4,5})", line)` in the **6Checker.py** i sorted all the available fancy numbers in a new file called **finalFancyNum.txt** where only the digits with digitalRoot 6 and their prices are sorted



