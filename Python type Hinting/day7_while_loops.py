# Task 1


def ai_server_retry() -> None:
    attempt = 1
    while attempt <= 5:

        print(f"Attempt {attempt}: Connecting to AI Server...")
        if attempt == 3:
            print("Success: Connected to AI Server")
            break
        attempt += 1


ai_server_retry()


# Task 2


def agent_token_counter() -> None:
    tokens = 10
    while tokens >= 4:
        print(f"Agent running...Remaining tokens:{tokens}")
        if tokens == 4:
            print(f"Critical Warning! Token reached {tokens}. Stopping Agent")
            break
        tokens -= 1


agent_token_counter()


# Task 3

def log_filter() -> None:
    id = 1
    while id <= 5:
        if id == 3:
           print(f"Warning: Data ID {id} is Corrupted! Skipping...")
            # print(f"Warning: Data ID {id} is Corrupted! Skipping...")
           id += 1
           continue


        print(f"Processing Data Id: {id}")
        id += 1



log_filter()
