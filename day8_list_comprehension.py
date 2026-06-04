
# feature  1: List Comprehension
# ------------------------------

token_counts = [100, 250, 500, 1000]

doubled_tokens = [token * 2 for token in token_counts]

print("--Feature 1: List Comprehension---")

print("old token list", token_counts)

print("double token list", doubled_tokens)


# Feature 2: Chat Memory Slicing
# ------------------------------------

chat_history = [
    "User: Hi",
    "AI: Hello",
    "User: What is AI",
    "AI: Artificial Intelligence",
    "User: Super, teach me Python!"
]

recent_memory = chat_history[-3:]
print("/n----Feature 2:Chat Memory Slicing---")
print("Full Chat History", chat_history)
print("Last three items to take AI Memory", recent_memory)


# Task 1:

user_prompts = [ "HELLO", "Write Python", "SPAM TEXT","CrewAI"]
cleaned_prompts = [prompts.lower() for prompts in user_prompts]
print("All prompts to LowerCase", cleaned_prompts)


# Task 2:

all_tokens = [50, 450, 120, 300, 80, 600, 200]

big_tokens = [token for token in all_tokens if token >= 200]
print(big_tokens)     

# Task 3:

long_chat = [ "User: Hi","AI: Hello","User: Day 8","AI: Done","User: Next","AI: Ready"]

get_last_three_chat = long_chat[-3:]

print(get_last_three_chat)

# Task 4:

api_responses = [200, 404, 200, 500, 200, 401]
get_api_responses = [token for token in api_responses if token == 200] 
print(get_api_responses)

# Task 5:

chat_memory = [
    "User: Day 1 done",
    "AI: Great job",
    "User: Day 7 done",
    "AI: Awesome",
    "User: Need Day 8 tasks",
    "AI: Here are your tasks"
]

get_chat_memory = chat_memory[-2:]
print(get_chat_memory)

# Task 6:

base_tokens = [100, 150, 200,350]
add_base_tokens = [token + 50 for token in base_tokens  ]
print(add_base_tokens)

