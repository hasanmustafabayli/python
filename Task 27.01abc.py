#by Hasan Mustafabayli
#Task 27.01
#Question2

from datetime import *
class Company:
    
    def __init__(self, x, y):
        self.__CompanyName = x
        self.__EmailAddress = y
        self.__DateOfLastContact = None
    
    def set_DateOfLastContact(self, z):
        self.__DateOfLastContact = z
    
    def get_EmailAddress(self):
        return self.__EmailAddress
    
    def get_CompanyName(self):
        return self.__CompanyName
    
    def get_DateOfLastContact(self):
        return self.__DateOfLastContact
    
Company1 = Company("Test Company", "testcompany@gmail.com")
Company1.set_DateOfLastContact(date(2012,4,8))
print(Company1.get_CompanyName())
print(Company1.get_EmailAddress())
print(Company1.get_DateOfLastContact())
    
        
    