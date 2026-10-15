
# AI Lead Generation Tracker

business_file = "business_leads.txt"

# part1:Write Mode
with open(business_file, "w")as file:
   file.write("Lead 1: TechMalabar (Trivandrum) - AI Consulting\n")
   file.write("Lead 2: CyberKerala (Kochi) - Web Automation\n")
print("[Success ] create write mode")

# Part 2:Append Mode
with open(business_file, "a")as file:
   file.write("Lead 3: Malappuram_AI_Labs (Tirur) - Agentic Systems")
print("[Append Success]")  

# Part 3:Read More 
with open(business_file, "r")as file:
   read_businees_file  = file.read()
   print(f"[Success Read Mode]{read_businees_file}") 


