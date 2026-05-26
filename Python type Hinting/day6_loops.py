
# task 1
for i in range(1,6):
    print(i)

# task 2

users = ["Mini", "Reena", "Rinu", "Manju"]
for user in users:
    print(f"Notification sent to {user}: AI Model Update is Ready") 

# Task 3

def find_error_text(texts:list)->str:
    for text  in texts:
     if "Error" in text:
        print(f"{text}")
log_list = ["Success:Login","Error:Database Timeout","Success Upload","Error:Api Failure"]    
find_error_text(log_list)

# Task 4


def check_odd_even()->None:
    for i in range(1,10):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
check_odd_even()

# Task 5

for i in range(11,20):
 status = "Even" if i %2 == 0 else "Odd"
 print(f"{i} is{status}")


