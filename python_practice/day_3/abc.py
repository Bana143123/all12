from abc import ABC, abstractmethod
class Animal(ABC):# Define an abstract base class
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):# Define a subclass
    def speak(self):
        return "Woof!"

    def move(self):
        return "Run"

class Bird(Animal):# Define another subclass
    def speak(self):
        return "Tweet!"

    def move(self):
        return "Fly"

# Try to create an instance of Animal (will raise an error)
# animal = Animal()  # This will raise TypeError: Can't instantiate abstract class Animal with abstract methods move, speak


dog = Dog()# Creating instances of subclasses
bird = Bird()

print(dog.speak())
print(dog.move()) 
print(bird.speak()) 
print(bird.move())  