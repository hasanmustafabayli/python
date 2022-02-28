#By Hasan Mustafabayli
#Task 26.01, 26.02 and 26.04

import pickle
from datetime import date

class CarRecord:
    def __init__(self):
        self.VehicleID = "stroke"
        self.Registration = ""
        self.DateOfRegistration = date(2003,7,2)
        self.PurchasePrice = 0.0
        self.EngineSize = 0
        

CarFile = open('CarFile','wb')
for i in range(100):
    pickle.dump(Car[i], CarFile)
CarFile.close()

CarFile = open('CarFile','rb')
Car = []
EoF = False
while not EoF:
    try:
        Car.append(pickle.load(CarFile))
    except:
        EoF = True
        CarFile.close()
return Car
ThisCar = CarRecord()
Car = LoadingProccess()


for x in range(100):
    print(Car[x].VehicleID)
            
ThisCar = CarRecord()
Car = LoadingProccess()
OutputRecords(Car)
n = int(input('Enter the record Number: '))
while n != 0 :
    Car[n].DateOfregistration = (input('Date of registration: '))
    Car[n].Registration = input('registration: ')
    Car[n].EngineSize = int(input('engine size: '))
    Car[n].PurchasePrice = float(input('the price of purchase: '))
    Car[n].VehicleID = input('the vehicle ID: ')
    n = int(input('Is there a subsequent number of the record? '))
    OutputRecords(Car)
    SaveData(Car)
    
            
        