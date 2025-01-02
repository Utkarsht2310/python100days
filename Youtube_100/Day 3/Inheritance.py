class Employee: # Parent class
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"The name of Employee is {self.name} and id is {self.id}")


class Child(Employee):  # child class it inherit properties of parent class.
    def newinfo(self):
        print("The programming lang is Python")

obj = Child("Utkarsh",1)
obj.newinfo()
obj.showdetails()

################################################################################################################################

# **ACCESS MODIFIERS**
# BY DEFAULT IN PYTHON ALL THE VARIABLES ARE PUBLIC

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

#####################################################################################################################################
# Multiple Inheritance:-
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

##################################################################################################################################
# Multilevel Inheritance:-

# Base class (Parent class)
class Animal:
    def speak(self):
        print("This is an animal speaking.")

# Intermediate class (Child of Animal, Parent of Dog)
class Mammal(Animal):
    def walk(self):
        print("This mammal can walk.")

# Derived class (Child of Mammal)
class Dog(Mammal):
    def bark(self):
        print("The dog barks.")

# Create an object of the derived class
dog = Dog()

# Call methods from all classes
dog.speak()  # Inherited from Animal
dog.walk()   # Inherited from Mammal
dog.bark()   # Defined in Dog

#####################################################################################################################################
# Hybrid Inheritance:-
# Base class
class Animal:
    def speak(self):
        print("Animals make sounds.")

# Derived class 1 (inherits from Animal)
class Mammal(Animal):
    def walk(self):
        print("Mammals can walk.")

# Derived class 2 (inherits from Animal)
class Bird(Animal):
    def fly(self):
        print("Birds can fly.")

# Derived class 3 (inherits from Mammal and Bird)
class Bat(Mammal, Bird):
    def hang(self):
        print("Bats can hang upside down.")

# Create an object of the Bat class
bat = Bat()

# Call methods from all parent classes
bat.speak()  # Inherited from Animal
bat.walk()   # Inherited from Mammal
bat.fly()    # Inherited from Bird
bat.hang()   # Defined in Bat


##################################################################################################################################
# Hierarchical Inheritance: -
# Base class
class Animal:
    def speak(self):
        print("Animals make sounds.")

# Derived class 1 (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dogs bark.")

# Derived class 2 (inherits from Animal)
class Cat(Animal):
    def meow(self):
        print("Cats meow.")

# Create objects of derived classes
dog = Dog()
cat = Cat()

# Call methods
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog

cat.speak()  # Inherited from Animal
cat.meow()   # Defined in Cat

