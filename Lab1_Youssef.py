'''
Jack Youssef
1/28/2023 

This program holds the Book, Patron, and Library classes. The main function is used to test them by creating books and patrons, 
adding them to a library. and checking out / returning a book.
'''

from collections import deque

class Book(object):
    '''
    This class will represent all kinds of Books at a library.
    '''

    def getBookOwner(self):
        return self._patronOwner

    def queueLength(self):
        return len(self._patronQueue)

    def getPatronQueue(self):
        return self._patronQueue

    #Pre-condition: book and patron exists
    #Post-condition: 1. patron borrows the book if not currently out on loan and
    #                 nobody is waiting
    #                 or if not currently out on loan and patron is next in the
    #                 queue; add the book to the patron's list of books;
    #                 return True
    #                2. patron is added to the book's queue; return False
    #                3. patron isn't allowed to borrow more than max books (3);
    #                 return False
    def borrow(self, patron):
        '''Finish'''
        if not self._patronOwner and not self._patronQueue:
            if patron.addBook(self):
                print("Book is available. Borrow to " + patron.getName())
                self._patronOwner = patron
                return True
            else:
                return False
        elif not self._patronOwner and self._patronQueue[0] == patron:
            if patron.addBook(self):
                print("Book is available. Borrow to " + patron.getName())
                self._patronOwner = patron
                self._patronQueue.popleft()
                return True
            else:
                return False
        elif patron in self._patronQueue:
            print(patron.getName() + " is not next in the queue to borrow")
            return False
        else:
            self._patronQueue.append(patron)
            print("Book is not available. Add: " + patron.getName() + "to the queue.")
            return False
            

    #Pre-condition: book and patron exists
    #Post-condition: 1. book is removed from patron's list of books,
    #                 if book is in care of patron; current owner of the book is
    #                 set to None
    #                2. book is not returned because patron doesn't have it in the
    #                 first place   
    def returnBook(self, patron):
        '''Finish'''
        if self._patronOwner == patron:
            if patron.removeBook(self):
                print("Returned: " + self._title + ", " + self._author + " in care of: " + patron.getName() + " has " + str(len(patron.getBooks())) + " Books.")
                self._patronOwner = None
                return True
            else:
                print(patron.getName() + " does not have " + self._title + " currently checked out..")
                return False
        else:
            print(patron.getName() + " does not have " + self._title + " currently checked out")
            return False
        
    def getTitle(self):
        """ Returns book's title. """
        return self._title
    
    def __init__(self, title, author):
        '''
        Constructor
        '''
        self._patronQueue = deque() #use append and popleft for queue operations
        self._title = title
        self._author = author
        self._patronOwner = None

    def __str__(self):
        if self._patronOwner != None:
            s = self._title + ", " + self._author + " in care of: " + \
                str(self._patronOwner)
        else:
            s = self._title + ", " + self._author + " and has not been borrowed.\n"
        
        s += "Waiting:\n"
        count = 1
        for item in self._patronQueue:
            s += str(count) + ". " + str(item)
            count += 1
        s += "\n"
        return s
    
class Patron(object):
    '''
    This class will represent all kinds of Books at a library.
    '''
    
    #Pre-condition: book exists
    #Post-condition: 1. book is removed from the patron's list of books;
    #                 the number of books the patron has checked out is decremented by 1
    #                2. a message is displayed stating the patron does not have the
    #                 book checked out
    
    def removeBook(self, book):
        '''Finish'''
        if book in self._books:
            self._numBooks -= 1
            self._books.remove(book)
            return True
        else:
            print(self._name + " does not currently have " + book + " checked out.")
            return False
    
    #Pre-condition: book exists
    #Post-condition: 1. book is added the patron's list of books,
    #                 as long as the patron has less than 3 books checked out;
    #                 the number of books the patron has checked out is incremented
    #                 by 1; return True
    #                2. a message is displayed stating the patron has reached their
    #                 max and can't borrow anymore books; return False
    
    def addBook(self, book):
        '''Finish'''
        if self._numBooks < 3:
            self._books.append(book)
            self._numBooks += 1
            return True
        else:
            print(self._name + " Can't borrow more books--MAX REACHED!")
            return False
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
        self._numBooks = 0
        self._books = []
        
    def __str__(self):
        s = self._name + " has " + str(self._numBooks) + " books.\n"
        return s
    
    def getBooks(self):
        return self._books

    def getName(self):
        return self._name


class Library(object):
    """
    Represents a Library that manages book and patron objects.
    """
    def __init__(self, books):
        """ Constructor """
        self._books = books
        self._patrons = []
        
    def __str__(self):
        books = ""
        patrons = ""
        for book in self._books:
            books += str(book)
        for patron in self._patrons:
            patrons += str(patron)
        return books + patrons
    
    def addBook(self, book):
        """ Adds book to Library object. """
        self._books.append(book)
        
    def addPatron(self, patron):
        """ Adds patron to Library object. """ 
        self._patrons.append(patron)       
        
    def removeBook(self, book):
        """ Removes book from Library object. """
        if book in self._books:
            self._books.remove(book)
        else:
            print(book.getTitle(), " book not found in Library to remove.")
        
    def removePatron(self, patron):
        """ Removes patron from Library object. """
        if patron in self._patrons:
            self._patrons.remove(patron)
        else:
            print(patron.getName(), " patron not found in Library to remove.")
        
    def findBook(self, book):
        """ Finds book in Library object. """
        if book in self._books:
            print(book.getTitle(), " book found in library.")
            return book
        else:
            print(book.getTitle(), " book NOT found in library.")
            return False
        
    def findPatron(self, patron):
        """ Finds patron in Library object. """
        if patron in self._patrons:
            print(patron.getName(), " patron found in library.")
            return patron
        else:
            print(patron.getName(), " patron NOT found in library.")
            return False

    def borrowBook(self, book, patron):
        """ Borrows book from Library to patron. """
        if book not in self._books:
            print(book.getTitle(), " book not in Library to borrow.")
            return False
        if patron not in self._patrons:
            print(patron.getName(), " patron not in Library to borrow to.")
            return False
        if self._books[self._books.index(book)].getBookOwner() != None:
            print(book.getTitle(), " book already checked out.")
            return False
        if book in self._patrons[self._patrons.index(patron)].getBooks():
            print(book.getTtile(), " already checked out to ", patron)
            return False
        self._books[self._books.index(book)].borrow(patron)    
        
    def returnBook(self, book, patron):
        """ Returns book from patron to Library. """
        if book not in self._books:
            print(book.getTitle(), " book not in Library to borrow.")
            return False
        if patron not in self._patrons:
            print(patron.getName(), " patron not in Library to borrow to.")
            return False
        if self._books[self._books.index(book)].getBookOwner() == None:
            print(book.getTitle(), " book not checked out.")
            return False
        if book in self._patrons[self._patrons.index(patron)].getBooks():
            self._books[self._books.index(book)].returnBook(patron)


def main():
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984", "Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest", "Kesey")
    libraryBooks = []
    libraryBooks.append(book1)
    libraryBooks.append(book2)
    libraryBooks.append(book3)
    libraryBooks.append(book4)
    patron1 = Patron("Ivan")
    patron2 = Patron("Jimmy")
    patron3 = Patron("Bob")
    myLibrary = Library(libraryBooks)
    myLibrary.addPatron(patron1)
    myLibrary.addPatron(patron2)
    myLibrary.addPatron(patron3)
    print(str(myLibrary))
    myLibrary.borrowBook(book1, patron2)
    myLibrary.borrowBook(book1, patron3)
    print(str(myLibrary))
    myLibrary.returnBook(book1, patron2)
    print(str(myLibrary))
    
if __name__ == '__main__':
    main()

