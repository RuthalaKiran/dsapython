class Mobile:
    number = 10
    def __init__(self,brand,battery,ram,camera,price):
        self.brand = brand
        self.battery = battery
        self.ram  = ram
        self.camera =camera
        self.price = price
    def display(self):
        print("Brand :",self.brand)
        print("Brand :",self.battery)
        print("Brand :",self.ram)
        print("Brand :",self.camera)
        print("Brand :",self.price)
        print("class attribute :",self.number)
realme = Mobile("realme",4500,"6gb",'64MP',19000)
# vivo = Mobile("vivo",5000,"8gb",'48MP',15000)
# iphone = Mobile("iphone",4000,"4gb",'32MP',50000)
realme.display()
# vivo.display()
# iphone.display()
print(Mobile.number)


# class Mobile1:
#     def __init__(self):
#         print("this is init")
#     def display(self):
#         print("inside display")
# obj = Mobile1()
# obj.display()