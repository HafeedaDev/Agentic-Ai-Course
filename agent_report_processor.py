

print("Data Write to  a file")
with open("agent_activity.log", "w")as file:
    file.write("[INFO] ResearcherAgent initiated task.\n")
    file.write("[SUCCESS] ResearchAgent generated summary report.\n")
    file.write("[INFO] ValidatorAgent started validation.\n")
    

print("Data add to File")
with open("agent_activity.log", "a")as file:
    file.write("[SUCCESS] ValidatorAgent validation completed.\n")

print("Read Data")
with open("agent_activity.log", "r")as file:
 print(file.read())

print("Read first line")
with open("agent_activity.log", "r")as file:
   print(file.readline())

print("data to convert List")   
with open("agent_activity.log", "r")as file:
   lines = file.readlines()
   for line in lines:
      print(line.strip())


