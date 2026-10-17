class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed {self.title}")
        else:
            print(f"Sorry, {self.title} is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned {self.title}")
        else:
            print(f"{self.title} was not borrowed")

    def steel(self):
        self.is_borrowed = True
        print(f"You stole {self.title}")

book1 = Book("Python Basics", "John Smith")
book2 = Book("Learn OOP", "Jane Doe")

book1.borrow()
book1.return_book()
book1.steel()