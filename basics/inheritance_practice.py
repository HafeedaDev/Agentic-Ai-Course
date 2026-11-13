class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def greet(self):
        print(f"I am {self.name} working {self.role}")

class SalesAgent(Agent):

    def sell(self):
        print(f"{self.name} is selling")

class SupportAgent(Agent):
    def help(self, customer):
        self.greet()
        print(f"{self.name} is helping {customer}")
      

s1 = SupportAgent("Anu", "Doctor")
s1.greet()
s1.help("Raju")

# s = SalesAgent("Rani", "Lawyer")
# s.greet()
# s.sell()