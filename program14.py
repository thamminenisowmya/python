class person:
    count = 0    # This is a class variable
    def __init__(self, name, age,collegename):
        self.name = name
        # This is an instance variable
        self.age = age
        self.collegename=collegename
        person.count += 1
# Accesing the class variable using the name of the class
person1 = person("Hema", 25,"AWEC")
person2 = person("priya", 30,"AWEC")
print(person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)
