#By Hasan Mustafabayli
#Task 27.03

class Borrower():
    
    def __init__(self, n, a, i):
        self._BorrowerName = n
        self._EmailAddress = a
        self._BorrowerID = i
        self._ItemsOnLoan = 0
    
    def GetBorrowerName(self):
        return self._BorrowerName
    
    def GetEmailAddress(self):
        return self._EmailAddress
    
    def GetBorrowerID(self):
        return self._BorrowerID
    
    def GetItemsOnLoan(self):
        return self._ItemsOnLoan
    
    def UpdateItemsOnLoan(self, d):
        self._ItemsOnLoan += d
        
    def PrintDetails(self):
        print("Borrower:             ",     self._BorrowerName)
        print("EmailAddress:         ",     self._EmailAddress)
        print("BorrowerID:           ",       self._BorrowerID)
        print("Items on loan:        ",      self._ItemsOnLoan)
        
Borrower1 = Borrower("Hasan", "hasan@gmail.com", 29301)
Borrower1.UpdateItemsOnLoan(3)
print(Borrower1._ItemsOnLoan)
print(Borrower1.PrintDetails())

        
        
        
    