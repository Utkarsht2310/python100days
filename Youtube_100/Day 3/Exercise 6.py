class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBooks(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showDetail(self):
        print(f"There are {self.noBooks} books in the library")

l1 = Library()
l1.addBooks("Biopic")
l1.addBooks("Biopic2")
l1.addBooks("Biopic3")
l1.showDetail()

