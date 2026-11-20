from fastapi import FastAPI

app = FastAPI()

@app.post("/webhook")
def receive_webhook(data:dict):
    print("Got it", data)
    return {"status": "received"}

    
