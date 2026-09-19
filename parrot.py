class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("blu",10)
print("blu is a ", blu.species)
print(f"{ blu.name} is {blu.age} years old")
