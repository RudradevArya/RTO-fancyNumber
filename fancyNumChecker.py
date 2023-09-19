import re
import os; print(os.getcwd())



# Change the working directory
os.chdir(r"C:\Users\Rudradev Arya\Desktop\FancyNumbers")

# Now print the current working directory to verify it has changed
print(os.getcwd())


with open("fancyNumList.txt","r") as input:
    data = input.read()
    


lines = data.split("\n")


with open("2new_file.txt", "w") as f:
    f.write("Digits\tPrice\n")
    
  
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        
        match = re.search(r"MH12VX(\d{4})\s+(\d{4,5})", line)
        
        if match:
            f.write(f"{match.group(1)}\t{match.group(2)}\n")
