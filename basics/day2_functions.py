# task1
#1. create function with type hinting
def createPlanOfAi(agent_name: str, task: str, task_duration: int) -> str:
     plan = f"Agent {agent_name} is assigned to : {task}.Estimated Time: {task_duration}"
     return plan

# calling the function and storing the result
agentReport = createPlanOfAi("Hafeeda", "Analyze market trends using Ai", 3)

 # printing final output
print(agentReport)

# task2


# # .create function with type hinting
def calculate_remaining_budget(total_budget: float, used_amount: float) -> float:

    remainingBudget =  total_budget -  used_amount
 # to get ruturn value
    return remainingBudget

 # calling the function and storing the result
budgetReport = calculate_remaining_budget(500.5, 200.4)

 # printing final output
print(budgetReport)


# Task 3

 # .create function with type hinting
def checkAgentStatus(agent_name: str, is_active: bool) -> str:

 #  function checking
    if is_active == True :
       return f"Agent {agent_name} is Active"
        
    else:
        return f"Agent {agent_name} is not Active"
        
# calling the function with storing the result
checkStatus = checkAgentStatus("Ravi" ,True)

print(checkStatus)

# Task 4

 # a fuction create and type hinting
def totalExecutionTime(task1hour: int, task2hour:int, task3hour:int)->int:
#     #  add three hour
     totalHour = task1hour + task2hour + task3hour
     return totalHour
     
 # calling function and storing result
hourcheck = totalExecutionTime(2,3,4)

print(f"This take {hourcheck}")


# task5
# create a function and type hinting
def count_agent_task (task:list) -> int:

    return len(task)
 #  call the  functio and store the value
count = count_agent_task (["Web Scraping", "Data Cleaning", "Report Generation"])
# final result
print(f"there is {count} task")


# task 6
# create a function with typehinting
def optimize_speed(current_time: int) -> float:
    return current_time/2

# calling and store the value
balance = optimize_speed(10)
# final result
print(f"it take {balance}")