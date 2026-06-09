# ==========================================
# DAY 11: FILE HANDLING PRACTICE (TASK 1)
# Purpose: Creating a file and writing agent roles
# ==========================================

# 1. Storing the file name in a variable
file_name = "my_ai_agents.txt"

print(" Initializing file creation...")

# 2. Safely opening the file in Write Mode ('w') using 'with'
with open(file_name, "w") as file:
    # Writing AI Agent roles 
    file.write("Agent 1: Researcher (Searches for information from the internet)\n")
    file.write("Agent 2: Writer (Writes articles and reports based on research)\n")
    file.write("Agent 3: Validator (Checks for errors and validates output)\n")

# 3. Success log messages displayed in the terminal
print(f" [SUCCESS] '{file_name}' has been created successfully!")
print(" Check the left sidebar in VS Code to see your new file.")

# --Part 3: Appending To A File-----

print("\n Adding a new task to the file--")

with open(file_name, "a") as file:
    file.write("Task 4:Send execution report via email\n")
print("[APPEND SUCCESSFUL] New task has been added without deleting old data!")    