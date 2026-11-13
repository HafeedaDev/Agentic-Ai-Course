class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def greet(self):
        print(f"Hi, I am {self.name}, a {self.role}")

    def introduce(self):
        self.greet()

    def bye(self):
        print(f"Bye from {self.name}")

    def work(self, task):
        print(f"{self.name} is doing {task}" )

a1 = Agent("Ramu", "Writer")
a2 = Agent("Riya", "Doctor")

a1.work("writing")
a2.work("Driving")

a1.bye()
a2.bye()

# a1.greet()
# a2.greet()

a1.introduce()
a2.introduce()













