class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"hi {self.name}"
class Dog(Animal):
    def tell(self):
        return "Namaste"
d=Dog("Dood")
print(d.name)
print(d.speak())
print(d.tell())

