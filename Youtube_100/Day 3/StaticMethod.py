#A static method is a method that is tied to the class instead of the class's object. It is not possible to pass an implicit first argument to a static method. The class state cannot be accessed or changed by this method. It is present in a class because having the method in a class makes sense.

class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b


# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2))

##############################################################################################################
# Instance variables vs Class variables

class Employee:
  companyName = "Apple"  # Class variable
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name # Instance Variable
    self.raise_amount = 0.02 # Instance Variable
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()


######################################################################################################################################################################################333333
## Class Methods :-
class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod # decorator which passes class instead of class
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

##########################################################################################################################################################################################################3
# Class Methods as Alternative Constructors:-
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


person = Person.from_string("John Doe, 30")
print(person.name, person.age)
