# task 1
def check_access(agent_name: str, clearance_level: int) -> str:
    if clearance_level >= 5:
        return f"{agent_name:} Full Access Granted"
    elif clearance_level >= 3:
        return f"{agent_name:} Limited Access Granted"
    else:
        return f"{agent_name:} Access Denied!"


print(check_access("Alpha", 10))
print(check_access("Beta", 5))
print(check_access("Gamma", 2))


# task 2
def route_task(task_type: str, is_urgent: bool) -> str:
    if task_type == "Code" and is_urgent == True:
        return "Route to Developer Agent"
    elif task_type == "Code" and is_urgent == False:
        return "Queue for Review"
    else:
        return "Route to General Support"


print(route_task("Code", True))
print(route_task("Code", False))
print(route_task("Billing", True))


# Task 3
def monitor_system(cpu_usage: int, mem_usage: int) -> str:
    if cpu_usage > 90 or mem_usage > 90:
        return "Alert:  System Overload"
    else:
        return "System Healthy"


print(monitor_system(95, 40))
print(monitor_system(50, 30))


# Task 4


def calculate_discount(bill_amount: float, is_prime: bool) -> int:
    if bill_amount > 5000 and is_prime == True:
        return "25% "
    elif bill_amount > 5000 and is_prime == False:
        return "15% "
    elif 2000 <= bill_amount <= 5000:
        return "10% "
    else:
        return "0% "


print(calculate_discount(6000, True))
print(calculate_discount(6000, False))
print(calculate_discount(3000, False))
print(calculate_discount(1500, True))

# Task 5

def validate_input(user_message: str, message_length: int) -> str:
    if message_length == 0 or message_length > 500:
        return "Rejected: invalid Length"
    elif "spam" in user_message or "hack" in user_message:
        return "Rejected:SecurityRisk"
    else:
        return "Approved"
    
print(validate_input("Hello AI", 8))    
print(validate_input("", 0))   
print(validate_input("This is a spam msg", 18))   



# Task 6

def verify_transaction(country: str, amount: int) -> str:
    if country == "India":
        if amount > 50000 :
            return "OTP Verification Required"
        else:
         return "Approved:Domestic"
    else:   
        if amount > 10000:
            return "BLOCK:High Risk International"
        else:
            return "Approved:International"


print(verify_transaction("India", 60000))     
print(verify_transaction("India", 20000))   
print(verify_transaction("USA", 15000))   
print(verify_transaction("UAE", 5000))   




# Task 7
def select_agent_mode(battery: int, ping:int) -> str:
    if battery < 20:
        return "Power Saver Mode"
    elif battery >= 20 and ping > 200:
        return "Offline Mode"
    elif battery >= 80 and ping <= 50:
        return "Ultra Performance Mode"
    else:
       return"Normal Mode"
print(select_agent_mode(15, 30))      
print(select_agent_mode(50, 250))    
print(select_agent_mode(90, 40))    
print(select_agent_mode(50, 60))    