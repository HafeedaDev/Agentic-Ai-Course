class Agent:
    
    def __init__(self, name):
        self.name = name
        self.history = []
    def report(self):
        print(f"{self.name} did {len(self.history)} tasks")

    def show_history(self):
        for item in self.history:
          print(item)

    def think(self, task):
        return f"plan for {task}"

    def act(self, plan):
        print(f"{self.name} doing: {plan}")

    def run(self, task):
        plan = self.think(task)
        self.act(plan)
        self.history.append(task)

class SalesAgent(Agent):
    def think(self, task):
        return f"Sales plan for {task}"

        

# a = Agent("Ramu")
# a.run("write email")
# a.run("book meeting")
# a.report()
# a.show_history()

s=SalesAgent("Rani")
s.run("Call Customer")
# print(a.history)

 