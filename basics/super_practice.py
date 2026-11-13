class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def greet(self):
        print(f"I am {self.name} working {self.role}")

class SalesAgent(Agent):
    def __init__(self, name, role, target):
        super().__init__(name, role)    
        self.target = target

    def greet(self):
        super().greet()
        print(f"My target is {self.target}")

    
    def sell(self):
        print(f"{self.name} must sell {self.target}")

class SupportAgent(Agent):
    def __init__(self, name, role, language):
        super().__init__(name, role)
        self.language = language 
    
    def help(self, customer):
        print(f"{self.name} is helping {customer} in {self.language}")

s = SalesAgent("Ramu", "Sales", 10)
s.greet()
# s.sell()


# s3 = SupportAgent("Anu", "Doctor", "Malayalam")        
# s3.greet()
# s3.help("Raju")



