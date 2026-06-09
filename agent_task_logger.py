



























# DAY 11: FILE HANDLING PRACTICE (TASK 2)
# Purpose: Creating a file and writing agent roles
# ==========================================

# 1. Storing the file name in a variable
file_name =  "agent_tasks.txt"

print("file name is", file_name);

# 2. Safely opening the file in Write Mode ('w') using 'with'

with open(file_name,"w") as file:
    file.write("Task 1: Scrape data from website\n")
    file.write("Task 2: Clean the collected data\n")
    file.write("Task 3: Save results into database\n")

# 3. Success log messages displayed in the terminal
print(f"[Success] {file_name} hasbeen created Successfully")

# Using read mode and with 

with open(file_name, "r")as file:

    read_file = file.read()

    print(f"[Read Success] {read_file}")








