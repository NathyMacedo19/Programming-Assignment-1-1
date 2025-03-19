class Person:
    def __init__(self, name, age):  # Constructor method
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 25)
person1.display()
