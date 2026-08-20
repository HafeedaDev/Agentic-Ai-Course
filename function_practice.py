
def check_voting_eligiblity(name,age):
    if age >= 18:
        return{"name":name, "is_eligible":True}
    else:
        return{"name":name ,"is_eligible": False}
    
data = check_voting_eligiblity("Hari",13)
if data["is_eligible"]==True:
    print(f"Hi {data['name']}: You are eligible to vote")
else:
    print("You are not eligible to vote")
 

# --------------------------------------------------------------------------
def calculate_student_result(name,mark1,mark2):
    total = mark1+mark2
    avarage = total/2
    
    if avarage >= 40:
        return name, avarage, True
    else:
        return name, avarage,False
student_name, avg_mark, is_passed = calculate_student_result("Hari",12,56)
print(f"Name:{student_name}")
print(f"Total Average: {avg_mark}")


if is_passed:
    print("result: You are win in exam")
else:
    print("result:You are fail in exam") 



# -----------------------------------------------
def create_prompt(role, task, text):
    return f"You are a {role} Your task is {task} Here is the input text: {text}"

system_role = input("Your Job: ")
user_talk = input("What work should be assigned here?: ")
data_text = input("Write your text ")

prompt_data = create_prompt(system_role,user_talk,data_text)
print(prompt_data)


# ------------------------------------------------------------------------

def clean_ai_text(raw_text):
    clear_data = raw_text.strip().lower()
    return clear_data

dirty_text = input("Write your text")
final_data = clean_ai_text(dirty_text)
print(final_data)

 
# ---------------------------------------------------------
    
agent_response={
        "agent_name": "WebScraper",
        "status": "completed",
        "result": {
            "items_found": 15
        }
    } 
def extract_agent_info(agent_data):
   return f"Agent {agent_data["agent_name"]} found {agent_data["result"]["items_found"]}"

   
extract_data = extract_agent_info(agent_response)
print(extract_data)

# ------------------------------------------------
def chunk_text(text,chunk_size):
    words = text.split()
    chunks = []

    for i in range(0, len(words),chunk_size):
        current_chunk = words[i:i + chunk_size]
        chunks.append(current_chunk)
    return chunks

simple_text = "Python is an amazing language for AI Automation Engineers"
result = chunk_text(simple_text, chunk_size=3)
print(result)
