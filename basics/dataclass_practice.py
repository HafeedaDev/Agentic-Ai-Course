from dataclasses import dataclass

@dataclass
class Agent:
    name : str
    role : str ="Helper"
    def greet( self):
        print(f"I am {self.name} working {self.role}")

a = Agent("Anu")
# print(a.name)
print(a)
a.greet()