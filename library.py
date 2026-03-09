class Libray:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return self.books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
def main():
    library = Libray("City Library")
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)

    print(f"Books in {library.name}:")
    for book in library.list_books():
        print(book)
if __name__ == "__main__":
    main()