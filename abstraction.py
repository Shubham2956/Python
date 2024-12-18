from abc import *
import main

class abs(ABC):
    @abstractmethod
    def add(self): pass
    def sub(self): pass

class show(abs):
    def add(self):
        print("this is from add method")
    def sub(self):
        print("this is from sub")

obj1 = show()
obj1.add()
obj1.sub()


print("_________________________________________________________")
class new(ABC):
    @abstractmethod
    def add(self): pass
    @abstractmethod
    def sub(self):pass
    def mul(self):pass
    @abstractmethod
    def div(self):pass

class show(new):
    def add(self):
        print("this is add method")


    def sub(self):
        print("this is from sub")



class show1(show):
    def div(self):
        print("this is from new method")

obj = show1()
obj.add()
obj.sub()
obj.mul()
obj.div()
