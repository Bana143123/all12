class Hi:
    def __init__(self,name):
        self.name=name
    def say(self):
        return f"Good morning {self.name}"
class hello(Hi):
    def tell(self):
        call=super().say()
        return f"{call} what'sup"
    
ob=hello("Shyam")
print(ob.tell())
#extended method: By using this  we can extend the functionality of parent class method in the child class method
