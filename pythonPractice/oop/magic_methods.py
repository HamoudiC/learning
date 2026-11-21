# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__ 
#                 They are automatically called by many of Pythons built-in operations
#                 They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):

        self.title = title
        self.author = author
        self.num_pages = num_pages

    #string
    def __str__(self):
        return f"{self.title} by '{self.author}'."
    
    #equal to
    def __eq__(self, other_book):
        return self.title == other_book.title and self.author == other_book.author
    

    #less than
    def __lt__(self, other_book):
        return self.num_pages < other_book.num_pages
    
    #greater than
    def __gt__(self, other_book):
        return self.num_pages > other_book.num_pages
    
    #add
    def __add__(self, other_book):
        return f"{self.num_pages + other_book.num_pages} pages" 
    
    #iterates through words in the title or author and returns true or false
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    #get the attribute and returns title or author, number of pages in the book
    def __getitem__(self,key):

        if key == "title":
            return self.title
        
        elif key == "author":
            return self.author
        
        elif key == "num_pages":
            return self.num_pages
        
        else:
            return f"Key '{key}' is not found."

    

book1 = Book("Magnus Chase", "Rick Rioridan", 500)
book2 = Book("Harry Potter and The Prizoner of Azkaban", "J.K Rowling", 450)
book3 = Book("Inkheart", "Cornelia Funke", 800)

print("BOOK LIST:")
print(book1)

# Returns false because the parameters that I set (author and book name) do not match
print(book1 == book2)

#Prints true because the parameter that I set (number of pages) matches the equation
print(book2 < book1)
print(book1 > book2)

print("TOTAL PAGES")
print(book1 + book2)

#search for word in this book
print("Azkaban" in book2)

#search for attribute
print(book1['author'])

