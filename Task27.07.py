import datetime
class Borrower():
    
    def __init__(self, n, a, i):
        self.__BorrowerName = n
        self.__EmailAddress = a
        self.__BorrowerID = i
        self.__ItemsOnLoan = 0
    
    def GetBorrowerName(self):
        return self.__BorrowerName
    
    def GetEmailAddress(self):
        return self.__EmailAddress
    
    def GetBorrowerID(self):
        return self.__BorrowerID
    
    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan
    
    def UpdateItemsOnLoan(self, d):
        self.__ItemsOnLoan += d
    
    def printDetails(self):
        print(self.__BorrowerName, ';', self.__BorrowerID, ';', end='')
        print(self.__EmailAddress, ';', self.__ItemsOnLoan)

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__ItemsOnLoan = 0
    
    def GetTitle(self):
        return(self.__Title)
    #self.__OnLoan = False
    def GetAuthor_Artist(self):
        return(self.__Author_Artist)
    
    def GetItemID(self):
        return(self.__ItemID)
    
    def GetOnLoan(self):
        return(self.__OnLoan)
    
    def GetDueDate(self):
        return(self.__DueDate)
    
    def Borrowing(self,x):
        if  x.GetItemsOnLoan(self) < 5:
            self.__OnLoan = True
            self.__BorrowerID = x.getBorrowerID()
            self.__DueDate = self.__DueDate+datetime.timedelta(weeks=3)
            x.UpdateItemsOnLoan(1)
        else:
            print("too many books on loan")
    
    def Returning(self,x):
        x.__ItemsOnLoan -= 1

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist, end='')
        print(self.__ItemID,'; ', self.__OnLoan,'; ', self.__DueDate)
        print(self.__ItemID, ';', self.__DueDate)



def Menu():
    print('1 - Add a new borrower')
    print('2 - Add a new book')
    print('3 - Add a new CD')
    print('4 - Borrow book')
    print('5 - Return book')
    print('6 - Borrow CD')
    print('7 - Return CD')
    print('8 - Request book')
    print('9 - Print all details')
    print('99 - Exit program')
    print('Enter your menu choice: ')

Menu()

         
class Book(LibraryItem):
    
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    
    def GetIsRequested(self):
        return(self.__IsRequested)
    
    def SetIsRequested(self,i, x):
        self.__IsRequested = True
        self.__RequestedBy = x.getBorrowerID()
    
    def RequestBook(self, x):
        self.__IsRequested = True
        self.__RequestedBy = x.getBorrowerID()
    
    def printDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested, ';', self.__RequestedBy)
    
class CD(LibraryItem):
    
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.Genre = " "
   
    def SetGenre(self, g):
        self.Genre = g
    def printDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.Genre)

Continue = False
Menu()
BorrowerID = 1
BookID = 1
CDID = 1 

while Continue == False:
    a = int(input('Enter your menu choice: '))
    if a == 1:
        Name = input("Please enter your name: ")
        Email = input("Please enter your email address: ")
        ID = BorrowerID
        BorrowerID += 1
        Borrower1 = Borrower(Name, Email, ID)
    elif a == 2:
        Name = input("Please input the name of the book: ")
        Author = input("Please input the name of the author: ")
        ID = BookID
        BookID += 1
        Book1 = Book(Name, Author, ID)
    elif a == 3:
        Name = input("Please input the name of the CD: ")
        Artist = input("Please input the name of the artist: ")
        CID = CDID
        CDID += 1
        CD1 = CD(Name, Artist, CID)
    elif a == 4:
        BorrowerID = input("Please input the borrower ID: ")
        BookID = input("Please input the Book ID: ")
        Book.Borrowing(BookID, Borrower)
    elif a == 5:
        BorrowerID = input("Please input the borrower ID: ")
        BookID = input("Please input the Book ID: ")
        Book.Returning(BookID, Borrower)
    elif a == 6:
        BorrowerID = input("Please input the borrower ID: ")
        CDID = input("Please input the CD ID: ")
        CD.Borrowing(CDID, Borrower)
    elif a == 7:
        BorrowerID = input("Please input the borrower ID: ")
        CDID = input("Please input the CD ID: ")
        CD.Returning(CDID, Borrower)
    elif a == 8:
        BorrowerID = input("Please input the borrower ID: ")
        BookID = input("Please input the Book ID: ")
        Book.RequestBook(BookID, Borrower)
    elif a == 9:
        Borrower1.printDetails()
        Book1.printDetails()
        CD1.printDetails()
    elif a == 99:
        Continue = True
    else:
        print("wrong input")
        
    
    
