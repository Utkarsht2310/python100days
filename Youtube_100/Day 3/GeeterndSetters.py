class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self): # this is getter method
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value): # this is setter method
        self._value = new_value / 10


obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

########################################################################################################################################################
# dir, __dict__ and help method ;-

# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object
# __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__)

print(help(Person))

##################################################################################################################################################################3
# Super Keyword:- The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes

class Employee: # Parent class
  def __init__(self, name, id): # Constructor of parent class
    self.name = name
    self.id = id

class Programmer(Employee): # child class
  def __init__(self, name, id, lang): # constructor of child class
    super().__init__( name, id) # calling constructor of parent class using "super" keyword.
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)