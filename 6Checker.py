import re
import csv
import os; print(os.getcwd())



# Change the working directory
os.chdir(r"C:\Users\Rudradev Arya\Desktop\FancyNumbers")

# Now print the current working directory to verify it has changed
print(os.getcwd())




def digital_root(n):
  # If n is zero, return zero
  if n == 0:
    return 0
  # Otherwise, use the formula
  else:
    return 1 + ((n - 1) % 9)



with open("sortedNum.txt", "r") as data_file:
    # Read the data
    data = data_file.read()


lines = data.split("\n")


with open("finalFancyNum.txt", "w") as f:
    f.write("Digits\tPrices\n")
    
    for line in lines:
        if not line.strip() or "Digits" in line:
            continue
        

        match = re.search(r"(\d{4})\t(\d{4,5})", line)
        
        if match and digital_root(int(match.group(1))) == 6:
            f.write(line + "\n")
