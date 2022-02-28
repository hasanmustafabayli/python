class CarRecord:
    
    def __init__(self, VehicleId, Registration, DateOfRegistration, EngineSize, PurchaseSize):
        self.VehicleId = VehicleId
        self.Registration = Registration
        self.DateOfRegistration = DateOfRegistration
        self.EngineSize = EngineSize
        self.PurchaseSize = PurchaseSize
    
    
    def UpdateRegistration(self, UpdatedValue):
        self.Registartion = UpdatedValue

Customer = CarRecord(921, 821, 2003, 78, 21)

Customer.EngineSize = 2500
print(Customer.UpdateRegistration(2002))
print(Customer.EngineSize)

