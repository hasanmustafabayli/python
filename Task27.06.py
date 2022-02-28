#By Hasan Mustafabayli
#Task 27.06
import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    
    def GetTitle(self):
        return(self.__Title)
    
    def GetAuthor_Artist(self):
        return(self.__Author_Artist)
    
    def GetItemID(self):
        return(self.__ItemID)
    
    def GetOnLoan(self):
        return(self.__OnLoan)
    
    def GetDueDate(self):
        return(self.__DueDate)
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate+datetime.timedelta(weeks=3)
    
    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author_Artist, end='')
        print(self.__ItemID,'; ', self.__OnLoan,'; ', self.__DueDate)

class Book(LibraryItem):
    
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    
    def GetIsRequested(self):
        return(self.__IsRequested)
    
    def SetIsRequested(self,x):
        self.__IsRequested = True
        self.__RequestedBy = x

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        if self.__IsRequested :
          print('This book is requested by', self.__RequestedBy)
        else :
          print('There has been no requests made for this book')
          
class CD(LibraryItem):
    
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.Genre = " "
   
    def SetGenre(self, g):
        self.Genre = g
        
    def GetGenre(self):
        print(self.Genre)

Book1 = Book("Hasan", "Mustafa", "9392")
print(Book1.GetTitle())
print(Book1.GetAuthor_Artist())
print(Book1.GetItemID())
print(Book1.GetOnLoan())
print(Book1.GetDueDate())
print(Book1.Borrowing())
print(Book1.PrintDetails())
print(Book1.GetIsRequested())

CD1 = CD("Hasan", "Rah", "2920")
CD1.SetGenre("Rock")
CD1.GetGenre()
Book1.SetIsRequested(888)
Book1.PrintDetails()


    
 
