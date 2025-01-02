# Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.

class Employee:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good")

# main.py:-
# from emp import Employee
#
# e = Employee("Harry")
# print(str(e))
# print(repr(e))
# # print(e.name)
# # print(len(e))
# e()

##########################################################################################################################################
# METHOD OVERRIDING :-
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())

##########################################################################################################################################
#Method Overloading:-

# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)