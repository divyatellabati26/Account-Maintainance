import sys
class Library:
    def __init__(self,list_of_books):
         self.availablebooks=list_of_books
    def displayAvailablebooks(self):
        print("the books available in the library are")
        for book in self.availablebooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("issue the book")
        else:
            print("sorry book is not available")
    def addBook(self,returnBook):
        self.availablebooks.append(returnedBook)
        print("thanks for returning the book")
class Student:
    def requestBook(self):
        print("enter the name of book you requested")
        self.book=input()
        return self.book
    def returnBook(self):
        print("enter the name of the book you returned")
        self.book=input()
        return self.book
def main():
    library=Library(["Ugrasen Suman","Core Python"])
    student=Student()
    done=True
    while done==True:
        print("Library Menu,1.display all available books,2.request a book,3.return a book,4.exit")
        choice=int(input("enter choice"))
        if choice==1:
            library.displayAvailablebooks()
        elif choice==2:
            library.lendBook(student.requestBook())
        elif choice==3:
            library.addBook(student.returnBook())
        elif choice==4:
            sys.exit()
main()