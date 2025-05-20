class Book:
    total_books = 0


    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

        
if __name__ == "__main__":
    book1 = Book()
    book2 = Book()
    
    Book.increment_book_count()
    Book.increment_book_count()
    
    print(f"Total books: {Book.total_books}")


