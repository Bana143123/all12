class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())
#when a child class provides a specific implementation of a method that is already defined in a parent class 