class Person:
    def __init__(self, name, occ): # It is parametrized constructor!!
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Utkarsh", "Developer")
b= Person("Anuj", "Data analyst")
a.info()
b.info()
